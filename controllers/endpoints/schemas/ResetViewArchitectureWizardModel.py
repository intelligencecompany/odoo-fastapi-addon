
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class ResetViewArchitectureWizardModel(BaseModel):
    id: Optional[int] = Field(None, title="ID", description="")
    reset_mode: Any = Field(None, title="Reset Mode", description="")
    view_id: Optional[int] = Field(None, title="View", description="")
    compare_view_id: Optional[int] = Field(None, title="Compare To View", description="")
    view_name: Optional[str] = Field(None, title="View Name", description="")
    has_diff: Optional[bool] = Field(None, title="Has Diff", description="")
    arch_diff: Optional[Any] = Field(None, title="Architecture Diff", description="")
    arch_to_compare: Optional[Any] = Field(None, title="Arch To Compare To", description="")
    display_name: Optional[str] = Field(None, title="Display Name", description="")
    create_uid: Optional[int] = Field(None, title="Created by", description="")
    create_date: Optional[str] = Field(None, title="Created on", description="")
    write_uid: Optional[int] = Field(None, title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, title="Last Updated on", description="")

