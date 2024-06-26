
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class ActivityscheduleplanWizardModel(BaseModel):
    id: Optional[int] = Field(None, alias="id", title="ID", description="")
    res_model: str = Field("", alias="res_model", title="Model", description="")
    res_model_id: int = Field(0, alias="res_model_id", title="Applies to", description="")
    company_id: int = Field(0, alias="company_id", title="Company", description="")
    plan_id: Optional[int] = Field(None, alias="plan_id", title="Plan", description="")
    plan_on_demand_user_id: Optional[int] = Field(None, alias="plan_on_demand_user_id", title="Assigned To", description="Choose assignation for activities with on demand assignation.")
    activity_type_id: Optional[int] = Field(None, alias="activity_type_id", title="Activity Type", description="")
    activity_user_id: Optional[int] = Field(None, alias="activity_user_id", title="Assigned to", description="")
    res_ids: Optional[Any] = Field(None, alias="res_ids", title="Document IDs", description="")
    plan_available_ids: Optional[List[int]] = Field(None, alias="plan_available_ids", title="Plan Available", description="")
    is_batch_mode: Optional[bool] = Field(None, alias="is_batch_mode", title="Use in batch", description="")
    error: Optional[Any] = Field(None, alias="error", title="Error", description="")
    has_error: Optional[bool] = Field(None, alias="has_error", title="Has Error", description="")
    plan_has_user_on_demand: Optional[bool] = Field(None, alias="plan_has_user_on_demand", title="Has on demand responsible", description="")
    plan_assignation_summary: Optional[Any] = Field(None, alias="plan_assignation_summary", title="Plan Summary", description="")
    plan_date_deadline: Optional[str] = Field(None, alias="plan_date_deadline", title="Plan Date", description="")
    activity_category: Optional[Any] = Field(None, alias="activity_category", title="Action", description="Actions may trigger specific behavior like opening calendar view or automatically mark as done when a document is uploaded")
    date_deadline: Optional[str] = Field(None, alias="date_deadline", title="Due Date", description="")
    summary: Optional[str] = Field(None, alias="summary", title="Summary", description="")
    note: Optional[Any] = Field(None, alias="note", title="Note", description="")
    chaining_type: Optional[Any] = Field(None, alias="chaining_type", title="Chaining Type", description="")
    display_name: Optional[str] = Field(None, alias="display_name", title="Display Name", description="")
    create_uid: Optional[int] = Field(None, alias="create_uid", title="Created by", description="")
    create_date: Optional[str] = Field(None, alias="create_date", title="Created on", description="")
    write_uid: Optional[int] = Field(None, alias="write_uid", title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, alias="write_date", title="Last Updated on", description="")

    class ConfigDict:
        from_attributes = True

    @classmethod
    def from_execute_kw(cls, data:List[dict], fields:List[str] = []) -> List['ActivityscheduleplanWizardModel']:
        transformed = []
        schema = ActivityscheduleplanWizardModel.model_json_schema()
        
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
