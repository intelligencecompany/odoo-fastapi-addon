
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class ChannelMemberModel(BaseModel):
    id: Optional[int] = Field(None, alias="id", title="ID", description="")
    partner_id: Optional[int] = Field(None, alias="partner_id", title="Partner", description="")
    guest_id: Optional[int] = Field(None, alias="guest_id", title="Guest", description="")
    channel_id: int = Field(0, alias="channel_id", title="Channel", description="")
    fetched_message_id: Optional[int] = Field(None, alias="fetched_message_id", title="Last Fetched", description="")
    seen_message_id: Optional[int] = Field(None, alias="seen_message_id", title="Last Seen", description="")
    rtc_inviting_session_id: Optional[int] = Field(None, alias="rtc_inviting_session_id", title="Ringing session", description="")
    rtc_session_ids: Optional[List[int]] = Field(None, alias="rtc_session_ids", title="RTC Sessions", description="")
    is_self: Optional[bool] = Field(None, alias="is_self", title="Is Self", description="")
    custom_channel_name: Optional[str] = Field(None, alias="custom_channel_name", title="Custom channel name", description="")
    message_unread_counter: Optional[int] = Field(None, alias="message_unread_counter", title="Unread Messages Counter", description="")
    fold_state: Optional[Any] = Field(None, alias="fold_state", title="Conversation Fold State", description="")
    is_minimized: Optional[bool] = Field(None, alias="is_minimized", title="Conversation is minimized", description="")
    custom_notifications: Optional[Any] = Field(None, alias="custom_notifications", title="Customized Notifications", description="All Messages if not specified")
    mute_until_dt: Optional[str] = Field(None, alias="mute_until_dt", title="Mute notifications until", description="If set, the member will not receive notifications from the channel until this date.")
    is_pinned: Optional[bool] = Field(None, alias="is_pinned", title="Is pinned on the interface", description="")
    last_interest_dt: Optional[str] = Field(None, alias="last_interest_dt", title="Last Interest", description="Contains the date and time of the last interesting event that happened in this channel for this partner. This includes: creating, joining, pinning, and new message posted.")
    last_seen_dt: Optional[str] = Field(None, alias="last_seen_dt", title="Last seen date", description="")
    display_name: Optional[str] = Field(None, alias="display_name", title="Display Name", description="")
    create_uid: Optional[int] = Field(None, alias="create_uid", title="Created by", description="")
    create_date: Optional[str] = Field(None, alias="create_date", title="Created on", description="")
    write_uid: Optional[int] = Field(None, alias="write_uid", title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, alias="write_date", title="Last Updated on", description="")

    class ConfigDict:
        from_attributes = True

    @classmethod
    def from_execute_kw(cls, item:dict) -> 'ChannelMemberModel':
        filtered_item = {}
        schema = ChannelMemberModel.model_json_schema()

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
    def list_from_execute_kw(cls, data:List[dict], fields:List[str] = []) -> List['ChannelMemberModel']:
        transformed = []
        schema = ChannelMemberModel.model_json_schema()
        
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
