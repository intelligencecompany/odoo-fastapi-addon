
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class MultiWebsitePublishedMixinModel(BaseModel):

    website_id: Optional[int] = Field(None, alias="website_id", title="Website", description="Restrict publishing to this website.")
    website_published: Optional[bool] = Field(None, alias="website_published", title="Visible on current website", description="")
    is_published: Optional[bool] = Field(None, alias="is_published", title="Is Published", description="")
    can_publish: Optional[bool] = Field(None, alias="can_publish", title="Can Publish", description="")
    website_url: Optional[str] = Field(None, alias="website_url", title="Website URL", description="The full URL to access the document through the website.")

    class ConfigDict:
        from_attributes = True

    @classmethod
    def from_execute_kw(cls, data:List[dict], fields:List[str] = []) -> List['MultiWebsitePublishedMixinModel']:
        transformed = []
        schema = MultiWebsitePublishedMixinModel.model_json_schema()
        
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
