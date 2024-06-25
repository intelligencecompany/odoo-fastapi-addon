
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class ActivityplantemplateModel(BaseModel):
    id: Optional[int] = Field(None, title="ID", description="")
    responsible_type: Any = Field(None, title="Assignment", description="")
    plan_id: int = Field(0, title="Plan", description="")
    company_id: Optional[int] = Field(None, title="Company", description="")
    activity_type_id: int = Field(0, title="Activity Type", description="")
    responsible_id: Optional[int] = Field(None, title="Assigned to", description="")
    res_model: Optional[Any] = Field(None, title="Model", description="Specify a model if the activity should be specific to a model and not available when managing activities for other models.")
    sequence: Optional[int] = Field(None, title="Sequence", description="")
    summary: Optional[str] = Field(None, title="Summary", description="")
    note: Optional[Any] = Field(None, title="Note", description="")
    display_name: Optional[str] = Field(None, title="Display Name", description="")
    create_uid: Optional[int] = Field(None, title="Created by", description="")
    create_date: Optional[str] = Field(None, title="Created on", description="")
    write_uid: Optional[int] = Field(None, title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, title="Last Updated on", description="")

