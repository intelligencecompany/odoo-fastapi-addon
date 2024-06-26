
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class OnboardingStepModel(BaseModel):
    id: Optional[int] = Field(None, alias="id", title="ID", description="")
    button_text: str = Field("", alias="button_text", title="Button text", description="Text on the panel's button to start this step")
    current_progress_step_id: Optional[int] = Field(None, alias="current_progress_step_id", title="Step Progress", description="Onboarding Progress Step for the current context (company).")
    onboarding_ids: Optional[List[int]] = Field(None, alias="onboarding_ids", title="Onboardings", description="")
    progress_ids: Optional[List[int]] = Field(None, alias="progress_ids", title="Onboarding Progress Step Records", description="All related Onboarding Progress Step Records (across companies)")
    title: Optional[str] = Field(None, alias="title", title="Title", description="")
    description: Optional[str] = Field(None, alias="description", title="Description", description="")
    done_icon: Optional[str] = Field(None, alias="done_icon", title="Font Awesome Icon when completed", description="")
    done_text: Optional[str] = Field(None, alias="done_text", title="Text to show when step is completed", description="")
    step_image: Optional[Any] = Field(None, alias="step_image", title="Step Image", description="")
    step_image_filename: Optional[str] = Field(None, alias="step_image_filename", title="Step Image Filename", description="")
    step_image_alt: Optional[str] = Field(None, alias="step_image_alt", title="Alt Text for the Step Image", description="Show when impossible to load the image")
    panel_step_open_action_name: Optional[str] = Field(None, alias="panel_step_open_action_name", title="Opening action", description="Name of the onboarding step model action to execute when opening the step, e.g. action_open_onboarding_1_step_1")
    current_step_state: Optional[Any] = Field(None, alias="current_step_state", title="Completion State", description="")
    is_per_company: Optional[bool] = Field(None, alias="is_per_company", title="Is per company", description="")
    sequence: Optional[int] = Field(None, alias="sequence", title="Sequence", description="")
    display_name: Optional[str] = Field(None, alias="display_name", title="Display Name", description="")
    create_uid: Optional[int] = Field(None, alias="create_uid", title="Created by", description="")
    create_date: Optional[str] = Field(None, alias="create_date", title="Created on", description="")
    write_uid: Optional[int] = Field(None, alias="write_uid", title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, alias="write_date", title="Last Updated on", description="")

    class ConfigDict:
        from_attributes = True

    @classmethod
    def from_execute_kw(cls, data:List[dict], fields:List[str] = []) -> List['OnboardingStepModel']:
        transformed = []
        schema = OnboardingStepModel.model_json_schema()
        
        for item in data:
            filtered_item = {}

            if len(fields) == 0:
                fields = item.keys()

            for key in fields:
                if key in item:
                    value = item[key]
                    model_type = 'any'

                    if 'anyOf' in schema['properties'][key] and 'type' in schema['properties'][key]['anyOf'][0]:
                        model_type = schema['properties'][key]['anyOf'][0]['type']
                    elif 'type' in schema['properties'][key]:
                        model_type = schema['properties'][key]['type']

                    if isinstance(value, list) and model_type != 'array':
                        value = value[0] if item[key] else None
                    
                    if isinstance(value, bool) and model_type == 'string':
                        value = ''

                    if value is not None:
                        filtered_item[key] = value

            transformed.append(cls(**filtered_item).model_dump(by_alias=True))
        return transformed
