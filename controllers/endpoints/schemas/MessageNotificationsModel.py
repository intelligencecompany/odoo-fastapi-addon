
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class MessageNotificationsModel(BaseModel):
    id: Optional[int] = Field(None, alias="id", title="ID", description="")
    notification_type: Any = Field(None, alias="notification_type", title="Notification Type", description="")
    author_id: Optional[int] = Field(None, alias="author_id", title="Author", description="")
    mail_message_id: int = Field(0, alias="mail_message_id", title="Message", description="")
    mail_mail_id: Optional[int] = Field(None, alias="mail_mail_id", title="Mail", description="Optional mail_mail ID. Used mainly to optimize searches.")
    res_partner_id: Optional[int] = Field(None, alias="res_partner_id", title="Recipient", description="")
    sms_id: Optional[int] = Field(None, alias="sms_id", title="SMS", description="")
    letter_id: Optional[int] = Field(None, alias="letter_id", title="Snailmail Letter", description="")
    sms_tracker_ids: Optional[List[int]] = Field(None, alias="sms_tracker_ids", title="SMS Trackers", description="")
    notification_status: Optional[Any] = Field(None, alias="notification_status", title="Status", description="")
    is_read: Optional[bool] = Field(None, alias="is_read", title="Is Read", description="")
    read_date: Optional[str] = Field(None, alias="read_date", title="Read Date", description="")
    failure_type: Optional[Any] = Field(None, alias="failure_type", title="Failure type", description="")
    failure_reason: Optional[Any] = Field(None, alias="failure_reason", title="Failure reason", description="")
    display_name: Optional[str] = Field(None, alias="display_name", title="Display Name", description="")
    sms_id_int: Optional[int] = Field(None, alias="sms_id_int", title="SMS ID", description="")
    sms_number: Optional[str] = Field(None, alias="sms_number", title="SMS Number", description="")

    class ConfigDict:
        from_attributes = True

    @classmethod
    def from_execute_kw(cls, item:dict) -> 'MessageNotificationsModel':
        filtered_item = {}
        schema = MessageNotificationsModel.model_json_schema()

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
    def list_from_execute_kw(cls, data:List[dict], fields:List[str] = []) -> List['MessageNotificationsModel']:
        transformed = []
        schema = MessageNotificationsModel.model_json_schema()
        
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
