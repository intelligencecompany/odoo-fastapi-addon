
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class PartnerwithadditionalinformationformailresendModel(BaseModel):
    id: Optional[int] = Field(None, title="ID", description="")
    notification_id: int = Field(0, title="Notification", description="")
    partner_id: Optional[int] = Field(None, title="Partner", description="")
    resend_wizard_id: Optional[int] = Field(None, title="Resend wizard", description="")
    name: Optional[str] = Field(None, title="Recipient Name", description="")
    email: Optional[str] = Field(None, title="Email Address", description="")
    failure_reason: Optional[Any] = Field(None, title="Failure Reason", description="")
    resend: Optional[bool] = Field(None, title="Try Again", description="")
    message: Optional[str] = Field(None, title="Error message", description="")
    partner_readonly: Optional[bool] = Field(None, title="Partner Readonly", description="")
    display_name: Optional[str] = Field(None, title="Display Name", description="")
    create_uid: Optional[int] = Field(None, title="Created by", description="")
    create_date: Optional[str] = Field(None, title="Created on", description="")
    write_uid: Optional[int] = Field(None, title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, title="Last Updated on", description="")

