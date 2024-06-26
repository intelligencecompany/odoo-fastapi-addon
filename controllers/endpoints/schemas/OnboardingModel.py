
from pydantic import BaseModel, Field
from typing import Optional, List, Any, Dict

class OnboardingModel(BaseModel):
    id: Optional[int] = Field(None, alias="id", title="ID", description="")
    route_name: str = Field("", alias="route_name", title="One word name", description="")
    current_progress_id: Optional[int] = Field(None, alias="current_progress_id", title="Onboarding Progress", description="Onboarding Progress for the current context (company).")
    step_ids: Optional[List[int]] = Field(None, alias="step_ids", title="Onboarding steps", description="")
    progress_ids: Optional[List[int]] = Field(None, alias="progress_ids", title="Onboarding Progress Records", description="All Onboarding Progress Records (across companies).")
    name: Optional[str] = Field(None, alias="name", title="Name of the onboarding", description="")
    text_completed: Optional[str] = Field(None, alias="text_completed", title="Message at completion", description="Text shown on onboarding when completed")
    is_per_company: Optional[bool] = Field(None, alias="is_per_company", title="Should be done per company?", description="")
    panel_close_action_name: Optional[str] = Field(None, alias="panel_close_action_name", title="Closing action", description="Name of the onboarding model action to execute when closing the panel.")
    current_onboarding_state: Optional[Any] = Field(None, alias="current_onboarding_state", title="Completion State", description="")
    is_onboarding_closed: Optional[bool] = Field(None, alias="is_onboarding_closed", title="Was panel closed?", description="")
    sequence: Optional[int] = Field(None, alias="sequence", title="Sequence", description="")
    display_name: Optional[str] = Field(None, alias="display_name", title="Display Name", description="")
    create_uid: Optional[int] = Field(None, alias="create_uid", title="Created by", description="")
    create_date: Optional[str] = Field(None, alias="create_date", title="Created on", description="")
    write_uid: Optional[int] = Field(None, alias="write_uid", title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, alias="write_date", title="Last Updated on", description="")

    class ConfigDict:
        from_attributes = True

    @classmethod
    def from_execute_kw(cls, item:Dict[str, Any]) -> 'OnboardingModel':
        filtered_item = {}
        schema = OnboardingModel.model_json_schema()

        for key in item:
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

        return cls(**filtered_item).model_dump(by_alias=True)

    @classmethod
    def list_from_execute_kw(cls, data:List[dict], fields:List[str] = []) -> List['OnboardingModel']:
        transformed = []
        schema = OnboardingModel.model_json_schema()
        
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
