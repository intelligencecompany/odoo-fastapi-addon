
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class LinkSMStomailingsmstrackingmodelsModel(BaseModel):
    id: Optional[int] = Field(None, title="ID", description="")
    sms_uuid: str = Field("", title="SMS uuid", description="")
    mail_notification_id: Optional[int] = Field(None, title="Mail Notification", description="")
    display_name: Optional[str] = Field(None, title="Display Name", description="")
    create_uid: Optional[int] = Field(None, title="Created by", description="")
    create_date: Optional[str] = Field(None, title="Created on", description="")
    write_uid: Optional[int] = Field(None, title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, title="Last Updated on", description="")

