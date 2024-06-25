
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class EmailresendwizardModel(BaseModel):
    id: Optional[int] = Field(None, title="ID", description="")
    mail_message_id: Optional[int] = Field(None, title="Message", description="")
    partner_ids: Optional[List[int]] = Field(None, title="Recipients", description="")
    notification_ids: Optional[List[int]] = Field(None, title="Notifications", description="")
    can_cancel: Optional[bool] = Field(None, title="Can Cancel", description="")
    can_resend: Optional[bool] = Field(None, title="Can Resend", description="")
    partner_readonly: Optional[bool] = Field(None, title="Partner Readonly", description="")
    display_name: Optional[str] = Field(None, title="Display Name", description="")
    create_uid: Optional[int] = Field(None, title="Created by", description="")
    create_date: Optional[str] = Field(None, title="Created on", description="")
    write_uid: Optional[int] = Field(None, title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, title="Last Updated on", description="")

