
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class OnboardingStepModel(BaseModel):
    id: Optional[int] = Field(None, title="ID", description="")
    button_text: str = Field("", title="Button text", description="Text on the panel's button to start this step")
    current_progress_step_id: Optional[int] = Field(None, title="Step Progress", description="Onboarding Progress Step for the current context (company).")
    onboarding_ids: Optional[List[int]] = Field(None, title="Onboardings", description="")
    progress_ids: Optional[List[int]] = Field(None, title="Onboarding Progress Step Records", description="All related Onboarding Progress Step Records (across companies)")
    title: Optional[str] = Field(None, title="Title", description="")
    description: Optional[str] = Field(None, title="Description", description="")
    done_icon: Optional[str] = Field(None, title="Font Awesome Icon when completed", description="")
    done_text: Optional[str] = Field(None, title="Text to show when step is completed", description="")
    step_image: Optional[Any] = Field(None, title="Step Image", description="")
    step_image_filename: Optional[str] = Field(None, title="Step Image Filename", description="")
    step_image_alt: Optional[str] = Field(None, title="Alt Text for the Step Image", description="Show when impossible to load the image")
    panel_step_open_action_name: Optional[str] = Field(None, title="Opening action", description="Name of the onboarding step model action to execute when opening the step, e.g. action_open_onboarding_1_step_1")
    current_step_state: Optional[Any] = Field(None, title="Completion State", description="")
    is_per_company: Optional[bool] = Field(None, title="Is per company", description="")
    sequence: Optional[int] = Field(None, title="Sequence", description="")
    display_name: Optional[str] = Field(None, title="Display Name", description="")
    create_uid: Optional[int] = Field(None, title="Created by", description="")
    create_date: Optional[str] = Field(None, title="Created on", description="")
    write_uid: Optional[int] = Field(None, title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, title="Last Updated on", description="")

