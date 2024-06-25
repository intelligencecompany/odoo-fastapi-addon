
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class PrivacyLogModel(BaseModel):
    id: Optional[int] = Field(None, title="ID", description="")
    date: str = Field("", title="Date", description="")
    anonymized_name: str = Field("", title="Anonymized Name", description="")
    anonymized_email: str = Field("", title="Anonymized Email", description="")
    user_id: int = Field(0, title="Handled By", description="")
    execution_details: Optional[Any] = Field(None, title="Execution Details", description="")
    records_description: Optional[Any] = Field(None, title="Found Records", description="")
    additional_note: Optional[Any] = Field(None, title="Additional Note", description="")
    display_name: Optional[str] = Field(None, title="Display Name", description="")
    create_uid: Optional[int] = Field(None, title="Created by", description="")
    create_date: Optional[str] = Field(None, title="Created on", description="")
    write_uid: Optional[int] = Field(None, title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, title="Last Updated on", description="")

