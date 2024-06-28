
from pydantic import BaseModel, Field
from typing import Optional, List, Any, Dict

class EventAlarmModel(BaseModel):
    id: Optional[int] = Field(None, alias="id", title="ID", description="")
    name: str = Field("", alias="name", title="Name", description="")
    alarm_type: Any = Field(None, alias="alarm_type", title="Type", description="")
    duration: int = Field(0, alias="duration", title="Remind Before", description="")
    interval: Any = Field(None, alias="interval", title="Unit", description="")
    mail_template_id: Optional[int] = Field(None, alias="mail_template_id", title="Email Template", description="Template used to render mail reminder content.")
    sms_template_id: Optional[int] = Field(None, alias="sms_template_id", title="SMS Template", description="Template used to render SMS reminder content.")
    duration_minutes: Optional[int] = Field(None, alias="duration_minutes", title="Duration in minutes", description="")
    body: Optional[Any] = Field(None, alias="body", title="Additional Message", description="Additional message that would be sent with the notification for the reminder")
    display_name: Optional[str] = Field(None, alias="display_name", title="Display Name", description="")
    create_uid: Optional[int] = Field(None, alias="create_uid", title="Created by", description="")
    create_date: Optional[str] = Field(None, alias="create_date", title="Created on", description="")
    write_uid: Optional[int] = Field(None, alias="write_uid", title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, alias="write_date", title="Last Updated on", description="")
    sms_notify_responsible: Optional[bool] = Field(None, alias="sms_notify_responsible", title="Notify Responsible", description="")

    class ConfigDict:
        from_attributes = True

    @classmethod
    def from_execute_kw(cls, item:dict) -> 'EventAlarmModel':
        filtered_item = {}
        schema = EventAlarmModel.model_json_schema()

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
    def list_from_execute_kw(cls, data:List[dict], fields:List[str] = []) -> List['EventAlarmModel']:
        transformed = []
        schema = EventAlarmModel.model_json_schema()
        
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
