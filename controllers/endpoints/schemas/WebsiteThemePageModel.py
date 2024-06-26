
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class WebsiteThemePageModel(BaseModel):
    id: Optional[int] = Field(None, alias="id", title="ID", description="")
    view_id: int = Field(0, alias="view_id", title="View", description="")
    copy_ids: Optional[List[int]] = Field(None, alias="copy_ids", title="Page using a copy of me", description="")
    url: Optional[str] = Field(None, alias="url", title="Url", description="")
    website_indexed: Optional[bool] = Field(None, alias="website_indexed", title="Page Indexed", description="")
    is_published: Optional[bool] = Field(None, alias="is_published", title="Is Published", description="")
    header_overlay: Optional[bool] = Field(None, alias="header_overlay", title="Header Overlay", description="")
    header_color: Optional[str] = Field(None, alias="header_color", title="Header Color", description="")
    header_visible: Optional[bool] = Field(None, alias="header_visible", title="Header Visible", description="")
    footer_visible: Optional[bool] = Field(None, alias="footer_visible", title="Footer Visible", description="")
    display_name: Optional[str] = Field(None, alias="display_name", title="Display Name", description="")
    create_uid: Optional[int] = Field(None, alias="create_uid", title="Created by", description="")
    create_date: Optional[str] = Field(None, alias="create_date", title="Created on", description="")
    write_uid: Optional[int] = Field(None, alias="write_uid", title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, alias="write_date", title="Last Updated on", description="")

    class ConfigDict:
        from_attributes = True

    @classmethod
    def from_execute_kw(cls, item:dict) -> 'WebsiteThemePageModel':
        filtered_item = {}
        schema = WebsiteThemePageModel.model_json_schema()

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
    def list_from_execute_kw(cls, data:List[dict], fields:List[str] = []) -> List['WebsiteThemePageModel']:
        transformed = []
        schema = WebsiteThemePageModel.model_json_schema()
        
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
