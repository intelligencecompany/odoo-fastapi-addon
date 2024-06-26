
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class UTMMixinModel(BaseModel):

    campaign_id: Optional[int] = Field(None, alias="campaign_id", title="Campaign", description="This is a name that helps you keep track of your different campaign efforts, e.g. Fall_Drive, Christmas_Special")
    source_id: Optional[int] = Field(None, alias="source_id", title="Source", description="This is the source of the link, e.g. Search Engine, another domain, or name of email list")
    medium_id: Optional[int] = Field(None, alias="medium_id", title="Medium", description="This is the method of delivery, e.g. Postcard, Email, or Banner Ad")

    class Config:
        from_attributes = True

    @classmethod
    def from_execute_kw(cls, data:List[dict], fields:List[str] = []) -> List['UTMMixinModel']:
        transformed = []
        schema = UTMMixinModel.model_json_schema()
        
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
