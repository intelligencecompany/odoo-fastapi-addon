
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class WebsiteMenuModel(BaseModel):
    id: Optional[int] = Field(None, alias="id", title="ID", description="")
    name: str = Field("", alias="name", title="Menu", description="")
    page_id: Optional[int] = Field(None, alias="page_id", title="Related Page", description="")
    controller_page_id: Optional[int] = Field(None, alias="controller_page_id", title="Related Model Page", description="")
    website_id: Optional[int] = Field(None, alias="website_id", title="Website", description="")
    parent_id: Optional[int] = Field(None, alias="parent_id", title="Parent Menu", description="")
    child_id: Optional[List[int]] = Field(None, alias="child_id", title="Child Menus", description="")
    theme_template_id: Optional[int] = Field(None, alias="theme_template_id", title="Theme Template", description="")
    url: Optional[str] = Field(None, alias="url", title="Url", description="")
    new_window: Optional[bool] = Field(None, alias="new_window", title="New Window", description="")
    sequence: Optional[int] = Field(None, alias="sequence", title="Sequence", description="")
    parent_path: Optional[str] = Field(None, alias="parent_path", title="Parent Path", description="")
    is_visible: Optional[bool] = Field(None, alias="is_visible", title="Is Visible", description="")
    is_mega_menu: Optional[bool] = Field(None, alias="is_mega_menu", title="Is Mega Menu", description="")
    mega_menu_content: Optional[Any] = Field(None, alias="mega_menu_content", title="Mega Menu Content", description="")
    mega_menu_classes: Optional[str] = Field(None, alias="mega_menu_classes", title="Mega Menu Classes", description="")
    display_name: Optional[str] = Field(None, alias="display_name", title="Display Name", description="")
    create_uid: Optional[int] = Field(None, alias="create_uid", title="Created by", description="")
    create_date: Optional[str] = Field(None, alias="create_date", title="Created on", description="")
    write_uid: Optional[int] = Field(None, alias="write_uid", title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, alias="write_date", title="Last Updated on", description="")

    class Config:
        from_attributes = True

    @classmethod
    def from_execute_kw(cls, data:List[dict], fields:List[str] = []) -> List['WebsiteMenuModel']:
        transformed = []
        schema = WebsiteMenuModel.model_json_schema()
        
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
