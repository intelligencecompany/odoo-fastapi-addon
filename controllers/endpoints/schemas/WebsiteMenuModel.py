
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class WebsiteMenuModel(BaseModel):
    id: Optional[int] = Field(None, title="ID", description="")
    name: str = Field("", title="Menu", description="")
    page_id: Optional[int] = Field(None, title="Related Page", description="")
    controller_page_id: Optional[int] = Field(None, title="Related Model Page", description="")
    website_id: Optional[int] = Field(None, title="Website", description="")
    parent_id: Optional[int] = Field(None, title="Parent Menu", description="")
    child_id: Optional[List[int]] = Field(None, title="Child Menus", description="")
    theme_template_id: Optional[int] = Field(None, title="Theme Template", description="")
    url: Optional[str] = Field(None, title="Url", description="")
    new_window: Optional[bool] = Field(None, title="New Window", description="")
    sequence: Optional[int] = Field(None, title="Sequence", description="")
    parent_path: Optional[str] = Field(None, title="Parent Path", description="")
    is_visible: Optional[bool] = Field(None, title="Is Visible", description="")
    is_mega_menu: Optional[bool] = Field(None, title="Is Mega Menu", description="")
    mega_menu_content: Optional[Any] = Field(None, title="Mega Menu Content", description="")
    mega_menu_classes: Optional[str] = Field(None, title="Mega Menu Classes", description="")
    display_name: Optional[str] = Field(None, title="Display Name", description="")
    create_uid: Optional[int] = Field(None, title="Created by", description="")
    create_date: Optional[str] = Field(None, title="Created on", description="")
    write_uid: Optional[int] = Field(None, title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, title="Last Updated on", description="")

