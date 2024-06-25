
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class EmailTemplatePreviewModel(BaseModel):
    id: Optional[int] = Field(None, title="ID", description="")
    mail_template_id: int = Field(0, title="Related Mail Template", description="")
    model_id: Optional[int] = Field(None, title="Targeted model", description="")
    attachment_ids: Optional[List[int]] = Field(None, title="Attachment", description="")
    partner_ids: Optional[List[int]] = Field(None, title="Recipients", description="")
    resource_ref: Optional[Any] = Field(None, title="Record", description="")
    lang: Optional[Any] = Field(None, title="Template Preview Language", description="")
    no_record: Optional[bool] = Field(None, title="No Record", description="")
    error_msg: Optional[str] = Field(None, title="Error Message", description="")
    subject: Optional[str] = Field(None, title="Subject", description="")
    email_from: Optional[str] = Field(None, title="From", description="Sender address")
    email_to: Optional[str] = Field(None, title="To", description="Comma-separated recipient addresses")
    email_cc: Optional[str] = Field(None, title="Cc", description="Carbon copy recipients")
    reply_to: Optional[str] = Field(None, title="Reply-To", description="Preferred response address")
    scheduled_date: Optional[str] = Field(None, title="Scheduled Date", description="The queue manager will send the email after the date")
    body_html: Optional[Any] = Field(None, title="Body", description="")
    display_name: Optional[str] = Field(None, title="Display Name", description="")
    create_uid: Optional[int] = Field(None, title="Created by", description="")
    create_date: Optional[str] = Field(None, title="Created on", description="")
    write_uid: Optional[int] = Field(None, title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, title="Last Updated on", description="")

