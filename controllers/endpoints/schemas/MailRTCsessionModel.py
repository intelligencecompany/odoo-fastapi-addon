
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class MailRTCsessionModel(BaseModel):
    id: Optional[int] = Field(None, title="ID", description="")
    channel_member_id: int = Field(0, title="Channel Member", description="")
    channel_id: Optional[int] = Field(None, title="Channel", description="")
    partner_id: Optional[int] = Field(None, title="Partner", description="")
    guest_id: Optional[int] = Field(None, title="Guest", description="")
    write_date: Optional[str] = Field(None, title="Last Updated On", description="")
    is_screen_sharing_on: Optional[bool] = Field(None, title="Is sharing the screen", description="")
    is_camera_on: Optional[bool] = Field(None, title="Is sending user video", description="")
    is_muted: Optional[bool] = Field(None, title="Is microphone muted", description="")
    is_deaf: Optional[bool] = Field(None, title="Has disabled incoming sound", description="")
    display_name: Optional[str] = Field(None, title="Display Name", description="")
    create_uid: Optional[int] = Field(None, title="Created by", description="")
    create_date: Optional[str] = Field(None, title="Created on", description="")
    write_uid: Optional[int] = Field(None, title="Last Updated by", description="")

