
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class ActivityMixinModel(BaseModel):

    activity_user_id: Optional[int] = Field(None, title="Responsible User", description="")
    activity_type_id: Optional[int] = Field(None, title="Next Activity Type", description="")
    activity_ids: Optional[List[int]] = Field(None, title="Activities", description="")
    activity_state: Optional[Any] = Field(None, title="Activity State", description="Status based on activities\nOverdue: Due date is already passed\nToday: Activity date is today\nPlanned: Future activities.")
    activity_type_icon: Optional[str] = Field(None, title="Activity Type Icon", description="Font awesome icon e.g. fa-tasks")
    activity_date_deadline: Optional[str] = Field(None, title="Next Activity Deadline", description="")
    my_activity_date_deadline: Optional[str] = Field(None, title="My Activity Deadline", description="")
    activity_summary: Optional[str] = Field(None, title="Next Activity Summary", description="")
    activity_exception_decoration: Optional[Any] = Field(None, title="Activity Exception Decoration", description="Type of the exception activity on record.")
    activity_exception_icon: Optional[str] = Field(None, title="Icon", description="Icon to indicate an exception activity.")

