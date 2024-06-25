
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class ActivityscheduleplanWizardModel(BaseModel):
    id: Optional[int] = Field(None, title="ID", description="")
    res_model: str = Field("", title="Model", description="")
    res_model_id: int = Field(0, title="Applies to", description="")
    company_id: int = Field(0, title="Company", description="")
    plan_id: Optional[int] = Field(None, title="Plan", description="")
    plan_on_demand_user_id: Optional[int] = Field(None, title="Assigned To", description="Choose assignation for activities with on demand assignation.")
    activity_type_id: Optional[int] = Field(None, title="Activity Type", description="")
    activity_user_id: Optional[int] = Field(None, title="Assigned to", description="")
    res_ids: Optional[Any] = Field(None, title="Document IDs", description="")
    plan_available_ids: Optional[List[int]] = Field(None, title="Plan Available", description="")
    is_batch_mode: Optional[bool] = Field(None, title="Use in batch", description="")
    error: Optional[Any] = Field(None, title="Error", description="")
    has_error: Optional[bool] = Field(None, title="Has Error", description="")
    plan_has_user_on_demand: Optional[bool] = Field(None, title="Has on demand responsible", description="")
    plan_assignation_summary: Optional[Any] = Field(None, title="Plan Summary", description="")
    plan_date_deadline: Optional[str] = Field(None, title="Plan Date", description="")
    activity_category: Optional[Any] = Field(None, title="Action", description="Actions may trigger specific behavior like opening calendar view or automatically mark as done when a document is uploaded")
    date_deadline: Optional[str] = Field(None, title="Due Date", description="")
    summary: Optional[str] = Field(None, title="Summary", description="")
    note: Optional[Any] = Field(None, title="Note", description="")
    chaining_type: Optional[Any] = Field(None, title="Chaining Type", description="")
    display_name: Optional[str] = Field(None, title="Display Name", description="")
    create_uid: Optional[int] = Field(None, title="Created by", description="")
    create_date: Optional[str] = Field(None, title="Created on", description="")
    write_uid: Optional[int] = Field(None, title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, title="Last Updated on", description="")

