
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class ResendNotificationModel(BaseModel):
    id: Optional[int] = Field(None, title="ID", description="")
    sms_resend_id: int = Field(0, title="Sms Resend", description="")
    notification_id: int = Field(0, title="Notification", description="")
    partner_id: Optional[int] = Field(None, title="Partner", description="")
    resend: Optional[bool] = Field(None, title="Try Again", description="")
    failure_type: Optional[Any] = Field(None, title="Error Message", description="")
    partner_name: Optional[str] = Field(None, title="Recipient Name", description="")
    sms_number: Optional[str] = Field(None, title="Phone Number", description="")
    display_name: Optional[str] = Field(None, title="Display Name", description="")
    create_uid: Optional[int] = Field(None, title="Created by", description="")
    create_date: Optional[str] = Field(None, title="Created on", description="")
    write_uid: Optional[int] = Field(None, title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, title="Last Updated on", description="")

