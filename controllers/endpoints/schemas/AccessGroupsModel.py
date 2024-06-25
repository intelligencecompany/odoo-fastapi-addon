
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class AccessGroupsModel(BaseModel):
    id: Optional[int] = Field(None, title="ID", description="")
    name: str = Field("", title="Name", description="")
    category_id: Optional[int] = Field(None, title="Application", description="")
    implied_ids: Optional[List[int]] = Field(None, title="Inherits", description="Users of this group automatically inherit those groups")
    trans_implied_ids: Optional[List[int]] = Field(None, title="Transitively inherits", description="")
    users: Optional[List[int]] = Field(None, title="Users", description="")
    model_access: Optional[List[int]] = Field(None, title="Access Controls", description="")
    rule_groups: Optional[List[int]] = Field(None, title="Rules", description="")
    menu_access: Optional[List[int]] = Field(None, title="Access Menu", description="")
    view_access: Optional[List[int]] = Field(None, title="Views", description="")
    comment: Optional[Any] = Field(None, title="Comment", description="")
    color: Optional[int] = Field(None, title="Color Index", description="")
    full_name: Optional[str] = Field(None, title="Group Name", description="")
    share: Optional[bool] = Field(None, title="Share Group", description="Group created to set access rights for sharing data with some users.")
    display_name: Optional[str] = Field(None, title="Display Name", description="")
    create_uid: Optional[int] = Field(None, title="Created by", description="")
    create_date: Optional[str] = Field(None, title="Created on", description="")
    write_uid: Optional[int] = Field(None, title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, title="Last Updated on", description="")

