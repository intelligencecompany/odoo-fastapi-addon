
from pydantic import BaseModel, Field
from typing import Optional, List, Any, Dict

class SMSResendModel(BaseModel):
    id: Optional[int] = Field(None, alias="id", title="ID", description="")
    mail_message_id: int = Field(0, alias="mail_message_id", title="Message", description="")
    recipient_ids: Optional[List[int]] = Field(None, alias="recipient_ids", title="Recipients", description="")
    can_cancel: Optional[bool] = Field(None, alias="can_cancel", title="Can Cancel", description="")
    can_resend: Optional[bool] = Field(None, alias="can_resend", title="Can Resend", description="")
    has_insufficient_credit: Optional[bool] = Field(None, alias="has_insufficient_credit", title="Has Insufficient Credit", description="")
    has_unregistered_account: Optional[bool] = Field(None, alias="has_unregistered_account", title="Has Unregistered Account", description="")
    display_name: Optional[str] = Field(None, alias="display_name", title="Display Name", description="")
    create_uid: Optional[int] = Field(None, alias="create_uid", title="Created by", description="")
    create_date: Optional[str] = Field(None, alias="create_date", title="Created on", description="")
    write_uid: Optional[int] = Field(None, alias="write_uid", title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, alias="write_date", title="Last Updated on", description="")

    class ConfigDict:
        from_attributes = True

    @classmethod
    def from_execute_kw(cls, item:Dict[str, Any]) -> 'SMSResendModel':
        filtered_item = {}
        schema = SMSResendModel.model_json_schema()

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
    def list_from_execute_kw(cls, data:List[dict], fields:List[str] = []) -> List['SMSResendModel']:
        transformed = []
        schema = SMSResendModel.model_json_schema()
        
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
