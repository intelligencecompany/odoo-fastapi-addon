
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class MessageNotificationsModel(BaseModel):
    id: Optional[int] = Field(None, title="ID", description="")
    notification_type: Any = Field(None, title="Notification Type", description="")
    author_id: Optional[int] = Field(None, title="Author", description="")
    mail_message_id: int = Field(0, title="Message", description="")
    mail_mail_id: Optional[int] = Field(None, title="Mail", description="Optional mail_mail ID. Used mainly to optimize searches.")
    res_partner_id: Optional[int] = Field(None, title="Recipient", description="")
    sms_id: Optional[int] = Field(None, title="SMS", description="")
    letter_id: Optional[int] = Field(None, title="Snailmail Letter", description="")
    sms_tracker_ids: Optional[List[int]] = Field(None, title="SMS Trackers", description="")
    notification_status: Optional[Any] = Field(None, title="Status", description="")
    is_read: Optional[bool] = Field(None, title="Is Read", description="")
    read_date: Optional[str] = Field(None, title="Read Date", description="")
    failure_type: Optional[Any] = Field(None, title="Failure type", description="")
    failure_reason: Optional[Any] = Field(None, title="Failure reason", description="")
    display_name: Optional[str] = Field(None, title="Display Name", description="")
    sms_id_int: Optional[int] = Field(None, title="SMS ID", description="")
    sms_number: Optional[str] = Field(None, title="SMS Number", description="")

