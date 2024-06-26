
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class EmailAliasesMixinModel(BaseModel):

    alias_defaults: Any = Field(None, alias="alias_defaults", title="Default Values", description="A Python dictionary that will be evaluated to provide default values when creating new records for this alias.")
    alias_id: int = Field(0, alias="alias_id", title="Alias", description="")
    alias_domain_id: Optional[int] = Field(None, alias="alias_domain_id", title="Alias Domain", description="")
    alias_name: Optional[str] = Field(None, alias="alias_name", title="Alias Name", description="The name of the email alias, e.g. 'jobs' if you want to catch emails for <jobs@example.odoo.com>")
    alias_domain: Optional[str] = Field(None, alias="alias_domain", title="Alias Domain Name", description="Email domain e.g. 'example.com' in 'odoo@example.com'")
    alias_email: Optional[str] = Field(None, alias="alias_email", title="Email Alias", description="")

    class ConfigDict:
        from_attributes = True

    @classmethod
    def from_execute_kw(cls, data:List[dict], fields:List[str] = []) -> List['EmailAliasesMixinModel']:
        transformed = []
        schema = EmailAliasesMixinModel.model_json_schema()
        
        for item in data:
            filtered_item = {}

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
