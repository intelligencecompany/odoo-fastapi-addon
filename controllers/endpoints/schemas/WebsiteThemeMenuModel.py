
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class WebsiteThemeMenuModel(BaseModel):
    id: Optional[int] = Field(None, title="ID", description="")
    name: str = Field("", title="Name", description="")
    page_id: Optional[int] = Field(None, title="Page", description="")
    parent_id: Optional[int] = Field(None, title="Parent", description="")
    copy_ids: Optional[List[int]] = Field(None, title="Menu using a copy of me", description="")
    url: Optional[str] = Field(None, title="Url", description="")
    new_window: Optional[bool] = Field(None, title="New Window", description="")
    sequence: Optional[int] = Field(None, title="Sequence", description="")
    mega_menu_content: Optional[Any] = Field(None, title="Mega Menu Content", description="")
    mega_menu_classes: Optional[str] = Field(None, title="Mega Menu Classes", description="")
    use_main_menu_as_parent: Optional[bool] = Field(None, title="Use Main Menu As Parent", description="")
    display_name: Optional[str] = Field(None, title="Display Name", description="")
    create_uid: Optional[int] = Field(None, title="Created by", description="")
    create_date: Optional[str] = Field(None, title="Created on", description="")
    write_uid: Optional[int] = Field(None, title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, title="Last Updated on", description="")

