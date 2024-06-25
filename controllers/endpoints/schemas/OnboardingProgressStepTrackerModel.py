
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class OnboardingProgressStepTrackerModel(BaseModel):
    id: Optional[int] = Field(None, title="ID", description="")
    step_id: int = Field(0, title="Onboarding Step", description="")
    company_id: Optional[int] = Field(None, title="Company", description="")
    progress_ids: Optional[List[int]] = Field(None, title="Related Onboarding Progress Tracker", description="")
    step_state: Optional[Any] = Field(None, title="Onboarding Step Progress", description="")
    display_name: Optional[str] = Field(None, title="Display Name", description="")
    create_uid: Optional[int] = Field(None, title="Created by", description="")
    create_date: Optional[str] = Field(None, title="Created on", description="")
    write_uid: Optional[int] = Field(None, title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, title="Last Updated on", description="")

