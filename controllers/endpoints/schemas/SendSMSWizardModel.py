
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class SendSMSWizardModel(BaseModel):
    id: Optional[int] = Field(None, title="ID", description="")
    composition_mode: Any = Field(None, title="Composition Mode", description="")
    body: Any = Field(None, title="Message", description="")
    res_id: Optional[int] = Field(None, title="Document ID", description="")
    template_id: Optional[int] = Field(None, title="Use Template", description="")
    res_ids: Optional[str] = Field(None, title="Document IDs", description="")
    res_model: Optional[str] = Field(None, title="Document Model Name", description="")
    res_model_description: Optional[str] = Field(None, title="Document Model Description", description="")
    res_ids_count: Optional[int] = Field(None, title="Visible records count", description="Number of recipients that will receive the SMS if sent in mass mode, without applying the Active Domain value")
    comment_single_recipient: Optional[bool] = Field(None, title="Single Mode", description="Indicates if the SMS composer targets a single specific recipient")
    mass_keep_log: Optional[bool] = Field(None, title="Keep a note on document", description="")
    mass_force_send: Optional[bool] = Field(None, title="Send directly", description="")
    mass_use_blacklist: Optional[bool] = Field(None, title="Use blacklist", description="")
    recipient_valid_count: Optional[int] = Field(None, title="# Valid recipients", description="")
    recipient_invalid_count: Optional[int] = Field(None, title="# Invalid recipients", description="")
    recipient_single_description: Optional[Any] = Field(None, title="Recipients (Partners)", description="")
    recipient_single_number: Optional[str] = Field(None, title="Stored Recipient Number", description="")
    recipient_single_number_itf: Optional[str] = Field(None, title="Recipient Number", description="Phone number of the recipient. If changed, it will be recorded on recipient's profile.")
    recipient_single_valid: Optional[bool] = Field(None, title="Is valid", description="")
    number_field_name: Optional[str] = Field(None, title="Number Field", description="")
    numbers: Optional[str] = Field(None, title="Recipients (Numbers)", description="")
    sanitized_numbers: Optional[str] = Field(None, title="Sanitized Number", description="")
    display_name: Optional[str] = Field(None, title="Display Name", description="")
    create_uid: Optional[int] = Field(None, title="Created by", description="")
    create_date: Optional[str] = Field(None, title="Created on", description="")
    write_uid: Optional[int] = Field(None, title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, title="Last Updated on", description="")

