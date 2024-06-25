
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class OutgoingSMSModel(BaseModel):
    id: Optional[int] = Field(None, title="ID", description="")
    state: Any = Field(None, title="SMS Status", description="")
    partner_id: Optional[int] = Field(None, title="Customer", description="")
    mail_message_id: Optional[int] = Field(None, title="Mail Message", description="")
    sms_tracker_id: Optional[int] = Field(None, title="SMS trackers", description="")
    uuid: Optional[str] = Field(None, title="UUID", description="Alternate way to identify a SMS record, used for delivery reports")
    number: Optional[str] = Field(None, title="Number", description="")
    body: Optional[Any] = Field(None, title="Body", description="")
    failure_type: Optional[Any] = Field(None, title="Failure Type", description="")
    to_delete: Optional[bool] = Field(None, title="Marked for deletion", description="Will automatically be deleted, while notifications will not be deleted in any case.")
    display_name: Optional[str] = Field(None, title="Display Name", description="")
    create_uid: Optional[int] = Field(None, title="Created by", description="")
    create_date: Optional[str] = Field(None, title="Created on", description="")
    write_uid: Optional[int] = Field(None, title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, title="Last Updated on", description="")

