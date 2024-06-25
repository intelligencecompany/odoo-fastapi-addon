
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class MessageReactionModel(BaseModel):
    id: Optional[int] = Field(None, title="ID", description="")
    content: str = Field("", title="Content", description="")
    message_id: int = Field(0, title="Message", description="")
    partner_id: Optional[int] = Field(None, title="Reacting Partner", description="")
    guest_id: Optional[int] = Field(None, title="Reacting Guest", description="")
    display_name: Optional[str] = Field(None, title="Display Name", description="")

