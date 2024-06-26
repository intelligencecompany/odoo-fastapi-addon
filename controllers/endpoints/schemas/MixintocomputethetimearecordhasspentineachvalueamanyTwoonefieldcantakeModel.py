
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class MixintocomputethetimearecordhasspentineachvalueamanyTwoonefieldcantakeModel(BaseModel):

    duration_tracking: Optional[Any] = Field(None, alias="duration_tracking", title="Status time", description="JSON that maps ids from a many2one field to seconds spent")

    class ConfigDict:
        from_attributes = True

    @classmethod
    def from_execute_kw(cls, item:dict[str, any]) -> 'MixintocomputethetimearecordhasspentineachvalueamanyTwoonefieldcantakeModel':
        filtered_item = {}
        schema = MixintocomputethetimearecordhasspentineachvalueamanyTwoonefieldcantakeModel.model_json_schema()

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
    def list_from_execute_kw(cls, data:List[dict], fields:List[str] = []) -> List['MixintocomputethetimearecordhasspentineachvalueamanyTwoonefieldcantakeModel']:
        transformed = []
        schema = MixintocomputethetimearecordhasspentineachvalueamanyTwoonefieldcantakeModel.model_json_schema()
        
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
