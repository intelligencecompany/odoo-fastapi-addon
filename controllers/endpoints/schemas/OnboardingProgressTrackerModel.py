
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class OnboardingProgressTrackerModel(BaseModel):
    id: Optional[int] = Field(None, title="ID", description="")
    company_id: Optional[int] = Field(None, title="Company", description="")
    onboarding_id: int = Field(0, title="Related onboarding tracked", description="")
    progress_step_ids: Optional[List[int]] = Field(None, title="Progress Steps Trackers", description="")
    onboarding_state: Optional[Any] = Field(None, title="Onboarding progress", description="")
    is_onboarding_closed: Optional[bool] = Field(None, title="Was panel closed?", description="")
    display_name: Optional[str] = Field(None, title="Display Name", description="")
    create_uid: Optional[int] = Field(None, title="Created by", description="")
    create_date: Optional[str] = Field(None, title="Created on", description="")
    write_uid: Optional[int] = Field(None, title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, title="Last Updated on", description="")

