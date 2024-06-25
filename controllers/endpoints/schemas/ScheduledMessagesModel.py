
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class ScheduledMessagesModel(BaseModel):
    id: Optional[int] = Field(None, title="ID", description="")
    scheduled_datetime: str = Field("", title="Scheduled Send Date", description="Datetime at which notification should be sent.")
    mail_message_id: int = Field(0, title="Message", description="")
    notification_parameters: Optional[Any] = Field(None, title="Notification Parameter", description="")
    display_name: Optional[str] = Field(None, title="Display Name", description="")
    create_uid: Optional[int] = Field(None, title="Created by", description="")
    create_date: Optional[str] = Field(None, title="Created on", description="")
    write_uid: Optional[int] = Field(None, title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, title="Last Updated on", description="")

