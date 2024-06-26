
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class ActivityModel(BaseModel):
    id: Optional[int] = Field(None, alias="id", title="ID", description="")
    date_deadline: str = Field("", alias="date_deadline", title="Due Date", description="")
    res_model_id: int = Field(0, alias="res_model_id", title="Document Model", description="")
    res_id: Optional[Any] = Field(None, alias="res_id", title="Related Document ID", description="")
    activity_type_id: Optional[int] = Field(None, alias="activity_type_id", title="Activity Type", description="")
    user_id: int = Field(0, alias="user_id", title="Assigned to", description="")
    request_partner_id: Optional[int] = Field(None, alias="request_partner_id", title="Requesting Partner", description="")
    recommended_activity_type_id: Optional[int] = Field(None, alias="recommended_activity_type_id", title="Recommended Activity Type", description="")
    previous_activity_type_id: Optional[int] = Field(None, alias="previous_activity_type_id", title="Previous Activity Type", description="")
    attachment_ids: Optional[List[int]] = Field(None, alias="attachment_ids", title="Attachments", description="")
    mail_template_ids: Optional[List[int]] = Field(None, alias="mail_template_ids", title="Email templates", description="")
    res_model: Optional[str] = Field(None, alias="res_model", title="Related Document Model", description="")
    res_name: Optional[str] = Field(None, alias="res_name", title="Document Name", description="")
    activity_category: Optional[Any] = Field(None, alias="activity_category", title="Action", description="Actions may trigger specific behavior like opening calendar view or automatically mark as done when a document is uploaded")
    activity_decoration: Optional[Any] = Field(None, alias="activity_decoration", title="Decoration Type", description="Change the background color of the related activities of this type.")
    icon: Optional[str] = Field(None, alias="icon", title="Icon", description="Font awesome icon e.g. fa-tasks")
    summary: Optional[str] = Field(None, alias="summary", title="Summary", description="")
    note: Optional[Any] = Field(None, alias="note", title="Note", description="")
    date_done: Optional[str] = Field(None, alias="date_done", title="Done Date", description="")
    automated: Optional[bool] = Field(None, alias="automated", title="Automated activity", description="Indicates this activity has been created automatically and not by any user.")
    state: Optional[Any] = Field(None, alias="state", title="State", description="")
    has_recommended_activities: Optional[bool] = Field(None, alias="has_recommended_activities", title="Next activities available", description="")
    chaining_type: Optional[Any] = Field(None, alias="chaining_type", title="Chaining Type", description="")
    can_write: Optional[bool] = Field(None, alias="can_write", title="Can Write", description="")
    active: Optional[bool] = Field(None, alias="active", title="Active", description="")
    display_name: Optional[str] = Field(None, alias="display_name", title="Display Name", description="")
    create_uid: Optional[int] = Field(None, alias="create_uid", title="Created by", description="")
    create_date: Optional[str] = Field(None, alias="create_date", title="Created on", description="")
    write_uid: Optional[int] = Field(None, alias="write_uid", title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, alias="write_date", title="Last Updated on", description="")

    class ConfigDict:
        from_attributes = True

    @classmethod
    def from_execute_kw(cls, item:dict) -> 'ActivityModel':
        filtered_item = {}
        schema = ActivityModel.model_json_schema()

        for key in item.keys():
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
    def list_from_execute_kw(cls, data:List[dict], fields:List[str] = []) -> List['ActivityModel']:
        transformed = []
        schema = ActivityModel.model_json_schema()
        
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
