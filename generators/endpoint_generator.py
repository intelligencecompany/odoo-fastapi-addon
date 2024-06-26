import xmlrpc.client
import json
import re
from typing import Any, Dict
import os

ODOO_URL = 'https://dataruba.com'
ODOO_DB = 'azureuser'
ODOO_USERNAME = 'admin'
ODOO_PASSWORD = '63bcb94e2c7c53f508c723a5b827c189dca26733'

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

def generate_endpoint(model: str = "", model_name: str = "DynamicModel") -> str:
    model_name = rename_digits(re.sub(r'\W|^(?=\d)', '', model_name))
    model_name_lower = model_name.lower()
    endpoint_definition = f"""
import json
import xmlrpc.client
from fastapi import APIRouter, Depends, HTTPException, Query
from fastapi.security import APIKeyHeader
from typing import List, Optional, Dict, Any
from .schemas import {model_name}Model as Model

router = APIRouter()

ODOO_URL = 'http://127.0.0.1:8069'
ODOO_DB = 'azureuser'
ODOO_USERNAME = 'admin'

api_key_header = APIKeyHeader(name='x-key')

def get_connection(api_key: str):
    common = xmlrpc.client.ServerProxy(f'{{ODOO_URL}}/xmlrpc/2/common')
    uid = common.authenticate(ODOO_DB, ODOO_USERNAME, api_key, {{}})
    models = xmlrpc.client.ServerProxy(f'{{ODOO_URL}}/xmlrpc/2/object')
    return uid, models

@router.get("/api/{model}", response_model=List[Model.{model_name}Model], tags=["{model.split('.')[0]}"])
async def get_{model_name_lower}(fields:str = '', offset:int = 0, limit:int = 1000, api_key:str = Depends(api_key_header)):
    uid, models = get_connection(api_key)
    field_list = [x.strip() for x in fields.split(',') if x != '']

    if uid:
        results = models.execute_kw(ODOO_DB, uid, api_key, '{model}', 'search_read', [[]], {{'fields': field_list, 'offset': offset, 'limit': limit}})
        if results is None:
            return json.dumps([])
        
        results = Model.{model_name}Model.from_execute_kw(results, field_list)
        return results
    else:
        return json.dumps({{'status': 'Connection failed'}})

@router.put("/api/{model}/{{post_id}}", response_model=Dict[str, str], tags=["{model.split('.')[0]}"])
async def put_{model_name_lower}(post_id:int, fields:Dict[str, Any], api_key:str = Depends(api_key_header)):
    uid, models = get_connection(api_key)

    print(post_id)
    print(fields)

    if uid:
        result = models.execute_kw(ODOO_DB, uid, api_key, '{model}', 'write', [[post_id], fields])
        print(result)

        return json.dumps({{'success': 'Post updated successfully.'}})
    else:
        return json.dumps({{'status': 'Connection failed'}})
"""

    return endpoint_definition

def save_to_file(model_definition: str, filename: str):
    filename = rename_digits(re.sub(r'\W|^(?=\d)', '', filename))
    os.makedirs('controllers/endpoints', exist_ok=True)
    file_path = os.path.join('controllers/endpoints', f'{filename}.py')
    with open(file_path, 'w') as f:
        f.write(model_definition)

def generate_endpoint_route(endpoint):
    endpoint_route = f"""app.include_router({endpoint}.router)"""
    return endpoint_route

def generate_init_fastapi_server(json_data: Dict[str, Any]):
    import_names = []
    endpoint_definitions = []
    for model in json_data:
        model_name = rename_digits(re.sub(r'\W|^(?=\d)', '', model['name']))
        import_names.append(f'from . import {model_name}')
        endpoint_definition = generate_endpoint_route(model_name)
        endpoint_definitions.append(endpoint_definition)

    import_body = "\n".join(import_names)
    
    body = "\n".join(endpoint_definitions)

    endpoint_definition = f"""from fastapi import FastAPI

{import_body}

app = FastAPI()

{body}
"""

    return endpoint_definition

common = xmlrpc.client.ServerProxy(f'{ODOO_URL}/xmlrpc/2/common')
uid = common.authenticate(ODOO_DB, ODOO_USERNAME, ODOO_PASSWORD, {})
models = xmlrpc.client.ServerProxy(f'{ODOO_URL}/xmlrpc/2/object')

model_ids = models.execute_kw(ODOO_DB, uid, ODOO_PASSWORD, 'ir.model', 'search', [[]])
model_names = models.execute_kw(ODOO_DB, uid, ODOO_PASSWORD, 'ir.model', 'read', [model_ids, ['model', 'name']])

for model in model_names:
    fields = models.execute_kw(ODOO_DB, uid, ODOO_PASSWORD, model['model'], 'fields_get', [], {'attributes': ['string']})
    filtered_names = {key: value for key, value in fields.items() if not key.startswith('_') and key != 'global'}

    if len(filtered_names) > 0:
        model_definition = generate_endpoint(model['model'], model['name'])
        save_to_file(model_definition, f"{model['name']}")
    else:
        model_names = [item for item in model_names if item["model"] != model['model']]

init_definition = generate_init_fastapi_server(model_names)
save_to_file(init_definition, f"__init__")
