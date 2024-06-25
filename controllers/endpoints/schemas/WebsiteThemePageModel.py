
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class WebsiteThemePageModel(BaseModel):
    id: Optional[int] = Field(None, title="ID", description="")
    view_id: int = Field(0, title="View", description="")
    copy_ids: Optional[List[int]] = Field(None, title="Page using a copy of me", description="")
    url: Optional[str] = Field(None, title="Url", description="")
    website_indexed: Optional[bool] = Field(None, title="Page Indexed", description="")
    is_published: Optional[bool] = Field(None, title="Is Published", description="")
    header_overlay: Optional[bool] = Field(None, title="Header Overlay", description="")
    header_color: Optional[str] = Field(None, title="Header Color", description="")
    header_visible: Optional[bool] = Field(None, title="Header Visible", description="")
    footer_visible: Optional[bool] = Field(None, title="Footer Visible", description="")
    display_name: Optional[str] = Field(None, title="Display Name", description="")
    create_uid: Optional[int] = Field(None, title="Created by", description="")
    create_date: Optional[str] = Field(None, title="Created on", description="")
    write_uid: Optional[int] = Field(None, title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, title="Last Updated on", description="")

