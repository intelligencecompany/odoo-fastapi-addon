
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class UserPresenceModel(BaseModel):
    id: Optional[int] = Field(None, title="ID", description="")
    user_id: Optional[int] = Field(None, title="Users", description="")
    guest_id: Optional[int] = Field(None, title="Guest", description="")
    last_poll: Optional[str] = Field(None, title="Last Poll", description="")
    last_presence: Optional[str] = Field(None, title="Last Presence", description="")
    status: Optional[Any] = Field(None, title="IM Status", description="")
    display_name: Optional[str] = Field(None, title="Display Name", description="")

