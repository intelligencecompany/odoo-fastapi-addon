
from pydantic import BaseModel, Field
from typing import Optional, List, Any, Dict

class ResourceMixinModel(BaseModel):

    resource_id: int = Field(0, alias="resource_id", title="Resource", description="")
    company_id: Optional[int] = Field(None, alias="company_id", title="Company", description="")
    resource_calendar_id: Optional[int] = Field(None, alias="resource_calendar_id", title="Working Hours", description="")
    tz: Optional[Any] = Field(None, alias="tz", title="Timezone", description="This field is used in order to define in which timezone the resources will work.")

    class ConfigDict:
        from_attributes = True

    @classmethod
    def from_execute_kw(cls, item:dict) -> 'ResourceMixinModel':
        filtered_item = {}
        schema = ResourceMixinModel.model_json_schema()

        for key in item.keys():
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
    def list_from_execute_kw(cls, data:List[dict], fields:List[str] = []) -> List['ResourceMixinModel']:
        transformed = []
        schema = ResourceMixinModel.model_json_schema()
        
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
