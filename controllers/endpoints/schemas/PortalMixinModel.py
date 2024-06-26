
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class PortalMixinModel(BaseModel):

    access_url: Optional[str] = Field(None, alias="access_url", title="Portal Access URL", description="Customer Portal URL")
    access_token: Optional[str] = Field(None, alias="access_token", title="Security Token", description="")
    access_warning: Optional[Any] = Field(None, alias="access_warning", title="Access warning", description="")

    class Config:
        from_attributes = True

    @classmethod
    def from_execute_kw(cls, data:List[dict], fields:List[str] = []) -> List['PortalMixinModel']:
        transformed = []
        schema = PortalMixinModel.model_json_schema()
        
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

            transformed.append(cls(**filtered_item))
        return transformed
