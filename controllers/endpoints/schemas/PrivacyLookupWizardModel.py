
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class PrivacyLookupWizardModel(BaseModel):
    id: Optional[int] = Field(None, title="ID", description="")
    name: str = Field("", title="Name", description="")
    email: str = Field("", title="Email", description="")
    log_id: Optional[int] = Field(None, title="Log", description="")
    line_ids: Optional[List[int]] = Field(None, title="Line", description="")
    execution_details: Optional[Any] = Field(None, title="Execution Details", description="")
    records_description: Optional[Any] = Field(None, title="Records Description", description="")
    line_count: Optional[int] = Field(None, title="Line Count", description="")
    display_name: Optional[str] = Field(None, title="Display Name", description="")
    create_uid: Optional[int] = Field(None, title="Created by", description="")
    create_date: Optional[str] = Field(None, title="Created on", description="")
    write_uid: Optional[int] = Field(None, title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, title="Last Updated on", description="")

