
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class PortalUserConfigModel(BaseModel):
    id: Optional[int] = Field(None, title="ID", description="")
    wizard_id: int = Field(0, title="Wizard", description="")
    partner_id: int = Field(0, title="Contact", description="")
    user_id: Optional[int] = Field(None, title="User", description="")
    email: Optional[str] = Field(None, title="Email", description="")
    login_date: Optional[str] = Field(None, title="Latest Authentication", description="")
    is_portal: Optional[bool] = Field(None, title="Is Portal", description="")
    is_internal: Optional[bool] = Field(None, title="Is Internal", description="")
    email_state: Optional[Any] = Field(None, title="Status", description="")
    display_name: Optional[str] = Field(None, title="Display Name", description="")
    create_uid: Optional[int] = Field(None, title="Created by", description="")
    create_date: Optional[str] = Field(None, title="Created on", description="")
    write_uid: Optional[int] = Field(None, title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, title="Last Updated on", description="")

