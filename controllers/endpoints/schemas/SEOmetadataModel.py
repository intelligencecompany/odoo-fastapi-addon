
from pydantic import BaseModel, Field
from typing import Optional, List, Any, Dict

class SEOmetadataModel(BaseModel):

    is_seo_optimized: Optional[bool] = Field(None, alias="is_seo_optimized", title="SEO optimized", description="")
    website_meta_title: Optional[str] = Field(None, alias="website_meta_title", title="Website meta title", description="")
    website_meta_description: Optional[Any] = Field(None, alias="website_meta_description", title="Website meta description", description="")
    website_meta_keywords: Optional[str] = Field(None, alias="website_meta_keywords", title="Website meta keywords", description="")
    website_meta_og_img: Optional[str] = Field(None, alias="website_meta_og_img", title="Website opengraph image", description="")
    seo_name: Optional[str] = Field(None, alias="seo_name", title="Seo name", description="")

    class ConfigDict:
        from_attributes = True

    @classmethod
    def from_execute_kw(cls, item:Dict[str, Any]) -> 'SEOmetadataModel':
        filtered_item = {}
        schema = SEOmetadataModel.model_json_schema()

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
    def list_from_execute_kw(cls, data:List[dict], fields:List[str] = []) -> List['SEOmetadataModel']:
        transformed = []
        schema = SEOmetadataModel.model_json_schema()
        
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
