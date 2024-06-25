
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class GrantPortalAccessModel(BaseModel):
    id: Optional[int] = Field(None, title="ID", description="")
    partner_ids: Optional[List[int]] = Field(None, title="Partners", description="")
    user_ids: Optional[List[int]] = Field(None, title="Users", description="")
    welcome_message: Optional[Any] = Field(None, title="Invitation Message", description="This text is included in the email sent to new users of the portal.")
    display_name: Optional[str] = Field(None, title="Display Name", description="")
    create_uid: Optional[int] = Field(None, title="Created by", description="")
    create_date: Optional[str] = Field(None, title="Created on", description="")
    write_uid: Optional[int] = Field(None, title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, title="Last Updated on", description="")

