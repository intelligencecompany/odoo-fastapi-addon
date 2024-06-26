import xmlrpc.client
import json
import re
from typing import Any, Dict
import os


ODOO_URL = 'https://dataruba.com'
ODOO_DB = 'azureuser'
ODOO_USERNAME = 'admin'
ODOO_PASSWORD = '63bcb94e2c7c53f508c723a5b827c189dca26733'

def remove_leading_special_chars(s):
    return re.sub(r'^[^a-zA-Z0-9]+', '', s)

def rename_digits(text):
    # Define a dictionary mapping digits to their text names
    digit_names = {
        '0': 'Zero', '1': 'One', '2': 'Two', '3': 'Three', '4': 'Four',
        '5': 'Five', '6': 'Six', '7': 'Seven', '8': 'Eight', '9': 'Nine'
    }
    
    # Initialize an empty list to collect transformed characters
    transformed_chars = []
    
    # Iterate through each character in the input text
    for char in text:
        # Check if the character is a digit and if its text name exists in the dictionary
        if char.isdigit() and char in digit_names:
            # Append the corresponding text name to the transformed list
            transformed_chars.append(digit_names[char])
        else:
            # Append the original character if it's not a digit or if no mapping is found
            transformed_chars.append(char)
    
    # Join the transformed characters into a new string and return it
    transformed_text = ''.join(transformed_chars)
    return transformed_text

def generate_field(field_name: str, field_info: Dict[str, Any]) -> str:
    field_type = field_info["type"]
    help_text = field_info.get("help", "")
    string = field_info.get("string", "")
    required = field_info.get("required", False)
    
    
    field_type_mapping = {
        "char": "str",
        "many2one": "int",
        "boolean": "bool",
        "date": "str",
        "datetime": "str",
        "one2many": "List[int]",
        "many2many": "List[int]",
        "integer": "int",
        "monetary": "float"
    }

    default_values = {
        "char": '""',
        "many2one": "0",
        "boolean": "False",
        "date": '""',
        "datetime": '""',
        "one2many": "[]",
        "many2many": "[]",
        "integer": "0",
        "monetary": "0.0"
    }

    python_type = field_type_mapping.get(field_type, "Any")  
    default_value = default_values.get(field_type, "None")
    
    if help_text and len(help_text) > 0:
        help_text = json.dumps(help_text.strip())
    else:
        help_text = '""'

    if field_name.startswith('model_'):
        field_name = f'x_{field_name}'

    if required:
        field_definition = f'    {field_name}: {python_type} = Field({default_value}, alias="{field_name}", title="{string}", description={help_text})'
    else:
        optional_field = f"Optional[{python_type}]"
        field_definition = f'    {field_name}: {optional_field} = Field(None, alias="{field_name}", title="{string}", description={help_text})'
    
    
    return field_definition

def generate_pydantic_model(json_data: Dict[str, Any], model_name: str = "DynamicModel") -> str:
    model_name = rename_digits(re.sub(r'\W|^(?=\d)', '', model_name))

    id_field = ""
    id_fields = []
    ids_fields = []
    required_fields = []
    other_fields = []
    
    for field_name, field_info in json_data.items():
        field_definition = generate_field(field_name, field_info)
        if field_name == "id":
            id_field = field_definition
        elif field_name.endswith("_id"):
            id_fields.append(field_definition)
        elif field_name.endswith("_ids"):
            ids_fields.append(field_definition)
        elif 'required' in field_info and field_info['required'] == True:
            required_fields.append(field_definition)
        else:
            other_fields.append(field_definition)
    
    # Combine id fields and other fields
    model_fields = [id_field] + required_fields + id_fields + ids_fields + other_fields
    model_body = "\n".join(model_fields)
    
    model_definition = f"""
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class {model_name}Model(BaseModel):
{model_body}

    class ConfigDict:
        from_attributes = True

    @classmethod
    def from_execute_kw(cls, item:dict[str, any]) -> '{model_name}Model':
        filtered_item = {{}}
        schema = {model_name}Model.model_json_schema()

        for key in item:
            value = item[key]
            model_type = 'any'

            if 'anyOf' in schema['properties'][key] and 'type' in schema['properties'][key]['anyOf'][0]:
                model_type = schema['properties'][key]['anyOf'][0]['type']
            elif 'type' in schema['properties'][key]:
                model_type = schema['properties'][key]['type']

            if isinstance(value, list) and model_type != 'array':
                value = value[0] if item[key] else None
            
            if isinstance(value, bool) and model_type == 'string':
                value = ''

            if value is not None:
                filtered_item[key] = value

        return cls(**filtered_item).model_dump(by_alias=True)

    @classmethod
    def list_from_execute_kw(cls, data:List[dict], fields:List[str] = []) -> List['{model_name}Model']:
        transformed = []
        schema = {model_name}Model.model_json_schema()
        
        for item in data:
            filtered_item = {{}}

            if len(fields) == 0:
                fields = item.keys()

            for key in fields:
                if key in item:
                    value = item[key]
                    model_type = 'any'

                    if 'anyOf' in schema['properties'][key] and 'type' in schema['properties'][key]['anyOf'][0]:
                        model_type = schema['properties'][key]['anyOf'][0]['type']
                    elif 'type' in schema['properties'][key]:
                        model_type = schema['properties'][key]['type']

                    if isinstance(value, list) and model_type != 'array':
                        value = value[0] if item[key] else None
                    
                    if isinstance(value, bool) and model_type == 'string':
                        value = ''

                    if value is not None:
                        filtered_item[key] = value

            transformed.append(cls(**filtered_item).model_dump(by_alias=True))
        return transformed
"""
    return model_definition

def save_model_to_file(model_definition: str, filename: str):
    filename = re.sub(r'\W|^(?=\d)', '', filename)
    os.makedirs('controllers/endpoints/schemas', exist_ok=True)
    file_path = os.path.join('controllers/endpoints/schemas', f'{filename}.py')
    with open(file_path, 'w') as f:
        f.write(model_definition)

def generate_init_(json_data: Dict[str, Any]):
    import_names = []
    for model in json_data:
        model_name = rename_digits(re.sub(r'\W|^(?=\d)', '', model['name']))
        import_names.append(f'from . import {model_name}Model')

    import_body = "\n".join(import_names)

    endpoint_definition = f"""{import_body}"""

    return endpoint_definition


common = xmlrpc.client.ServerProxy(f'{ODOO_URL}/xmlrpc/2/common')
uid = common.authenticate(ODOO_DB, ODOO_USERNAME, ODOO_PASSWORD, {})
models = xmlrpc.client.ServerProxy(f'{ODOO_URL}/xmlrpc/2/object')

model_ids = models.execute_kw(ODOO_DB, uid, ODOO_PASSWORD, 'ir.model', 'search', [[]])
# model_ids = models.execute_kw(ODOO_DB, uid, ODOO_PASSWORD, 'ir.model', 'search', [[]], { 'offset': 0, 'limit': 3 })
model_names = models.execute_kw(ODOO_DB, uid, ODOO_PASSWORD, 'ir.model', 'read', [model_ids, ['model', 'name']])

for model in model_names:
    fields = models.execute_kw(ODOO_DB, uid, ODOO_PASSWORD, model['model'], 'fields_get', [], {'attributes': ['string', 'help', 'type', 'required']})

    # hier verder gaan...filteren van columns beginnen met _
    filtered_names = {key: value for key, value in fields.items() if not key.startswith('_') and key != 'global' }

    if len(filtered_names) > 0:
        model_definition = generate_pydantic_model(filtered_names, model['name'])
        save_model_to_file(model_definition, f"{rename_digits(model['name'])}Model")
    else:
        model_names = [item for item in model_names if item["model"] != model['model']]

init_definition = generate_init_(model_names)
save_model_to_file(init_definition, f"__init__")