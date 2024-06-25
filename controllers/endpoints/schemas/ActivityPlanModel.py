
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class ActivityPlanModel(BaseModel):
    id: Optional[int] = Field(None, title="ID", description="")
    name: str = Field("", title="Name", description="")
    res_model: Any = Field(None, title="Model", description="Specify a model if the activity should be specific to a model and not available when managing activities for other models.")
    company_id: Optional[int] = Field(None, title="Company", description="")
    res_model_id: int = Field(0, title="Applies to", description="")
    template_ids: Optional[List[int]] = Field(None, title="Activities", description="")
    active: Optional[bool] = Field(None, title="Active", description="")
    steps_count: Optional[int] = Field(None, title="Steps Count", description="")
    assignation_summary: Optional[Any] = Field(None, title="Plan Summary", description="")
    has_user_on_demand: Optional[bool] = Field(None, title="Has on demand responsible", description="")
    display_name: Optional[str] = Field(None, title="Display Name", description="")
    create_uid: Optional[int] = Field(None, title="Created by", description="")
    create_date: Optional[str] = Field(None, title="Created on", description="")
    write_uid: Optional[int] = Field(None, title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, title="Last Updated on", description="")

