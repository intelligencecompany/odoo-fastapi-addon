
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class SMSResendModel(BaseModel):
    id: Optional[int] = Field(None, title="ID", description="")
    mail_message_id: int = Field(0, title="Message", description="")
    recipient_ids: Optional[List[int]] = Field(None, title="Recipients", description="")
    can_cancel: Optional[bool] = Field(None, title="Can Cancel", description="")
    can_resend: Optional[bool] = Field(None, title="Can Resend", description="")
    has_insufficient_credit: Optional[bool] = Field(None, title="Has Insufficient Credit", description="")
    has_unregistered_account: Optional[bool] = Field(None, title="Has Unregistered Account", description="")
    display_name: Optional[str] = Field(None, title="Display Name", description="")
    create_uid: Optional[int] = Field(None, title="Created by", description="")
    create_date: Optional[str] = Field(None, title="Created on", description="")
    write_uid: Optional[int] = Field(None, title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, title="Last Updated on", description="")

