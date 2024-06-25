
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class PrivacyLookupWizardLineModel(BaseModel):
    id: Optional[int] = Field(None, title="ID", description="")
    wizard_id: Optional[int] = Field(None, title="Wizard", description="")
    res_id: int = Field(0, title="Resource ID", description="")
    res_model_id: Optional[int] = Field(None, title="Related Document Model", description="")
    res_name: Optional[str] = Field(None, title="Resource name", description="")
    res_model: Optional[str] = Field(None, title="Document Model", description="")
    resource_ref: Optional[Any] = Field(None, title="Record", description="")
    has_active: Optional[bool] = Field(None, title="Has Active", description="")
    is_active: Optional[bool] = Field(None, title="Is Active", description="")
    is_unlinked: Optional[bool] = Field(None, title="Is Unlinked", description="")
    execution_details: Optional[str] = Field(None, title="Execution Details", description="")
    display_name: Optional[str] = Field(None, title="Display Name", description="")
    create_uid: Optional[int] = Field(None, title="Created by", description="")
    create_date: Optional[str] = Field(None, title="Created on", description="")
    write_uid: Optional[int] = Field(None, title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, title="Last Updated on", description="")

