
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class PartnerTagsModel(BaseModel):
    id: Optional[int] = Field(None, title="ID", description="")
    name: str = Field("", title="Tag Name", description="")
    parent_id: Optional[int] = Field(None, title="Parent Category", description="")
    child_ids: Optional[List[int]] = Field(None, title="Child Tags", description="")
    partner_ids: Optional[List[int]] = Field(None, title="Partners", description="")
    color: Optional[int] = Field(None, title="Color", description="")
    active: Optional[bool] = Field(None, title="Active", description="The active field allows you to hide the category without removing it.")
    parent_path: Optional[str] = Field(None, title="Parent Path", description="")
    display_name: Optional[str] = Field(None, title="Display Name", description="")
    create_uid: Optional[int] = Field(None, title="Created by", description="")
    create_date: Optional[str] = Field(None, title="Created on", description="")
    write_uid: Optional[int] = Field(None, title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, title="Last Updated on", description="")

