
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class MailTrackingValueModel(BaseModel):
    id: Optional[int] = Field(None, title="ID", description="")
    field_id: Optional[int] = Field(None, title="Field", description="")
    currency_id: Optional[int] = Field(None, title="Currency", description="Used to display the currency when tracking monetary values")
    mail_message_id: int = Field(0, title="Message ID", description="")
    field_info: Optional[Any] = Field(None, title="Removed field information", description="")
    field_groups: Optional[str] = Field(None, title="Field Groups", description="")
    old_value_integer: Optional[int] = Field(None, title="Old Value Integer", description="")
    old_value_float: Optional[Any] = Field(None, title="Old Value Float", description="")
    old_value_char: Optional[str] = Field(None, title="Old Value Char", description="")
    old_value_text: Optional[Any] = Field(None, title="Old Value Text", description="")
    old_value_datetime: Optional[str] = Field(None, title="Old Value DateTime", description="")
    new_value_integer: Optional[int] = Field(None, title="New Value Integer", description="")
    new_value_float: Optional[Any] = Field(None, title="New Value Float", description="")
    new_value_char: Optional[str] = Field(None, title="New Value Char", description="")
    new_value_text: Optional[Any] = Field(None, title="New Value Text", description="")
    new_value_datetime: Optional[str] = Field(None, title="New Value Datetime", description="")
    display_name: Optional[str] = Field(None, title="Display Name", description="")
    create_uid: Optional[int] = Field(None, title="Created by", description="")
    create_date: Optional[str] = Field(None, title="Created on", description="")
    write_uid: Optional[int] = Field(None, title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, title="Last Updated on", description="")

