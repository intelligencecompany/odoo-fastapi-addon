
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class AnalyticPlansModel(BaseModel):
    id: Optional[int] = Field(None, title="ID", description="")
    name: str = Field("", title="Name", description="")
    default_applicability: Any = Field(None, title="Default Applicability", description="")
    parent_id: Optional[int] = Field(None, title="Parent", description="")
    root_id: Optional[int] = Field(None, title="Root", description="")
    children_ids: Optional[List[int]] = Field(None, title="Childrens", description="")
    account_ids: Optional[List[int]] = Field(None, title="Accounts", description="")
    applicability_ids: Optional[List[int]] = Field(None, title="Applicability", description="")
    description: Optional[Any] = Field(None, title="Description", description="")
    parent_path: Optional[str] = Field(None, title="Parent Path", description="")
    children_count: Optional[int] = Field(None, title="Children Plans Count", description="")
    complete_name: Optional[str] = Field(None, title="Complete Name", description="")
    account_count: Optional[int] = Field(None, title="Analytic Accounts Count", description="")
    all_account_count: Optional[int] = Field(None, title="All Analytic Accounts Count", description="")
    color: Optional[int] = Field(None, title="Color", description="")
    sequence: Optional[int] = Field(None, title="Sequence", description="")
    display_name: Optional[str] = Field(None, title="Display Name", description="")
    create_uid: Optional[int] = Field(None, title="Created by", description="")
    create_date: Optional[str] = Field(None, title="Created on", description="")
    write_uid: Optional[int] = Field(None, title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, title="Last Updated on", description="")

