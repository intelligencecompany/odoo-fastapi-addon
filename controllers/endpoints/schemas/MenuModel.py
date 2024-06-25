
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class MenuModel(BaseModel):
    id: Optional[int] = Field(None, title="ID", description="")
    name: str = Field("", title="Menu", description="")
    child_id: Optional[List[int]] = Field(None, title="Child IDs", description="")
    parent_id: Optional[int] = Field(None, title="Parent Menu", description="")
    groups_id: Optional[List[int]] = Field(None, title="Groups", description="If you have groups, the visibility of this menu will be based on these groups. If this field is empty, Odoo will compute visibility based on the related object's read access.")
    active: Optional[bool] = Field(None, title="Active", description="")
    sequence: Optional[int] = Field(None, title="Sequence", description="")
    parent_path: Optional[str] = Field(None, title="Parent Path", description="")
    complete_name: Optional[str] = Field(None, title="Full Path", description="")
    web_icon: Optional[str] = Field(None, title="Web Icon File", description="")
    action: Optional[Any] = Field(None, title="Action", description="")
    web_icon_data: Optional[Any] = Field(None, title="Web Icon Image", description="")
    display_name: Optional[str] = Field(None, title="Display Name", description="")
    create_uid: Optional[int] = Field(None, title="Created by", description="")
    create_date: Optional[str] = Field(None, title="Created on", description="")
    write_uid: Optional[int] = Field(None, title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, title="Last Updated on", description="")

