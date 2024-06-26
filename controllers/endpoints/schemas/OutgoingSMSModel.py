
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class OutgoingSMSModel(BaseModel):
    id: Optional[int] = Field(None, alias="id", title="ID", description="")
    state: Any = Field(None, alias="state", title="SMS Status", description="")
    partner_id: Optional[int] = Field(None, alias="partner_id", title="Customer", description="")
    mail_message_id: Optional[int] = Field(None, alias="mail_message_id", title="Mail Message", description="")
    sms_tracker_id: Optional[int] = Field(None, alias="sms_tracker_id", title="SMS trackers", description="")
    uuid: Optional[str] = Field(None, alias="uuid", title="UUID", description="Alternate way to identify a SMS record, used for delivery reports")
    number: Optional[str] = Field(None, alias="number", title="Number", description="")
    body: Optional[Any] = Field(None, alias="body", title="Body", description="")
    failure_type: Optional[Any] = Field(None, alias="failure_type", title="Failure Type", description="")
    to_delete: Optional[bool] = Field(None, alias="to_delete", title="Marked for deletion", description="Will automatically be deleted, while notifications will not be deleted in any case.")
    display_name: Optional[str] = Field(None, alias="display_name", title="Display Name", description="")
    create_uid: Optional[int] = Field(None, alias="create_uid", title="Created by", description="")
    create_date: Optional[str] = Field(None, alias="create_date", title="Created on", description="")
    write_uid: Optional[int] = Field(None, alias="write_uid", title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, alias="write_date", title="Last Updated on", description="")

    class ConfigDict:
        from_attributes = True

    @classmethod
    def from_execute_kw(cls, item:dict[str, any]) -> 'OutgoingSMSModel':
        filtered_item = {}
        schema = OutgoingSMSModel.model_json_schema()

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
    def list_from_execute_kw(cls, data:List[dict], fields:List[str] = []) -> List['OutgoingSMSModel']:
        transformed = []
        schema = OutgoingSMSModel.model_json_schema()
        
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
