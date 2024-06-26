
from pydantic import BaseModel, Field
from typing import Optional, List, Any, Dict

class PhoneBlacklistModel(BaseModel):
    id: Optional[int] = Field(None, alias="id", title="ID", description="")
    number: str = Field("", alias="number", title="Phone Number", description="Number should be E164 formatted")
    message_follower_ids: Optional[List[int]] = Field(None, alias="message_follower_ids", title="Followers", description="")
    message_partner_ids: Optional[List[int]] = Field(None, alias="message_partner_ids", title="Followers (Partners)", description="")
    message_ids: Optional[List[int]] = Field(None, alias="message_ids", title="Messages", description="")
    rating_ids: Optional[List[int]] = Field(None, alias="rating_ids", title="Ratings", description="")
    website_message_ids: Optional[List[int]] = Field(None, alias="website_message_ids", title="Website Messages", description="Website communication history")
    message_is_follower: Optional[bool] = Field(None, alias="message_is_follower", title="Is Follower", description="")
    has_message: Optional[bool] = Field(None, alias="has_message", title="Has Message", description="")
    message_needaction: Optional[bool] = Field(None, alias="message_needaction", title="Action Needed", description="If checked, new messages require your attention.")
    message_needaction_counter: Optional[int] = Field(None, alias="message_needaction_counter", title="Number of Actions", description="Number of messages requiring action")
    message_has_error: Optional[bool] = Field(None, alias="message_has_error", title="Message Delivery error", description="If checked, some messages have a delivery error.")
    message_has_error_counter: Optional[int] = Field(None, alias="message_has_error_counter", title="Number of errors", description="Number of messages with delivery error")
    message_attachment_count: Optional[int] = Field(None, alias="message_attachment_count", title="Attachment Count", description="")
    message_has_sms_error: Optional[bool] = Field(None, alias="message_has_sms_error", title="SMS Delivery error", description="If checked, some messages have a delivery error.")
    active: Optional[bool] = Field(None, alias="active", title="Active", description="")
    display_name: Optional[str] = Field(None, alias="display_name", title="Display Name", description="")
    create_uid: Optional[int] = Field(None, alias="create_uid", title="Created by", description="")
    create_date: Optional[str] = Field(None, alias="create_date", title="Created on", description="")
    write_uid: Optional[int] = Field(None, alias="write_uid", title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, alias="write_date", title="Last Updated on", description="")

    class ConfigDict:
        from_attributes = True

    @classmethod
    def from_execute_kw(cls, item:dict) -> 'PhoneBlacklistModel':
        filtered_item = {}
        schema = PhoneBlacklistModel.model_json_schema()

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
    def list_from_execute_kw(cls, data:List[dict], fields:List[str] = []) -> List['PhoneBlacklistModel']:
        transformed = []
        schema = PhoneBlacklistModel.model_json_schema()
        
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
