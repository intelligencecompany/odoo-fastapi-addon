
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class SMSTemplatePreviewModel(BaseModel):
    id: Optional[int] = Field(None, title="ID", description="")
    sms_template_id: int = Field(0, title="Sms Template", description="")
    model_id: Optional[int] = Field(None, title="Applies to", description="The type of document this template can be used with")
    lang: Optional[Any] = Field(None, title="Template Preview Language", description="")
    body: Optional[str] = Field(None, title="Body", description="")
    resource_ref: Optional[Any] = Field(None, title="Record reference", description="")
    no_record: Optional[bool] = Field(None, title="No Record", description="")
    display_name: Optional[str] = Field(None, title="Display Name", description="")
    create_uid: Optional[int] = Field(None, title="Created by", description="")
    create_date: Optional[str] = Field(None, title="Created on", description="")
    write_uid: Optional[int] = Field(None, title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, title="Last Updated on", description="")

