
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class PortalSharingModel(BaseModel):
    id: Optional[int] = Field(None, title="ID", description="")
    res_model: str = Field("", title="Related Document Model", description="")
    res_id: int = Field(0, title="Related Document ID", description="")
    partner_ids: List[int] = Field([], title="Recipients", description="")
    resource_ref: Optional[Any] = Field(None, title="Related Document", description="")
    note: Optional[Any] = Field(None, title="Note", description="Add extra content to display in the email")
    share_link: Optional[str] = Field(None, title="Link", description="")
    access_warning: Optional[Any] = Field(None, title="Access warning", description="")
    display_name: Optional[str] = Field(None, title="Display Name", description="")
    create_uid: Optional[int] = Field(None, title="Created by", description="")
    create_date: Optional[str] = Field(None, title="Created on", description="")
    write_uid: Optional[int] = Field(None, title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, title="Last Updated on", description="")

