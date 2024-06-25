
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class OnboardingModel(BaseModel):
    id: Optional[int] = Field(None, title="ID", description="")
    route_name: str = Field("", title="One word name", description="")
    current_progress_id: Optional[int] = Field(None, title="Onboarding Progress", description="Onboarding Progress for the current context (company).")
    step_ids: Optional[List[int]] = Field(None, title="Onboarding steps", description="")
    progress_ids: Optional[List[int]] = Field(None, title="Onboarding Progress Records", description="All Onboarding Progress Records (across companies).")
    name: Optional[str] = Field(None, title="Name of the onboarding", description="")
    text_completed: Optional[str] = Field(None, title="Message at completion", description="Text shown on onboarding when completed")
    is_per_company: Optional[bool] = Field(None, title="Should be done per company?", description="")
    panel_close_action_name: Optional[str] = Field(None, title="Closing action", description="Name of the onboarding model action to execute when closing the panel.")
    current_onboarding_state: Optional[Any] = Field(None, title="Completion State", description="")
    is_onboarding_closed: Optional[bool] = Field(None, title="Was panel closed?", description="")
    sequence: Optional[int] = Field(None, title="Sequence", description="")
    display_name: Optional[str] = Field(None, title="Display Name", description="")
    create_uid: Optional[int] = Field(None, title="Created by", description="")
    create_date: Optional[str] = Field(None, title="Created on", description="")
    write_uid: Optional[int] = Field(None, title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, title="Last Updated on", description="")

