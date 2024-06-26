
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class UserSettingsModel(BaseModel):
    id: Optional[int] = Field(None, alias="id", title="ID", description="")
    user_id: int = Field(0, alias="user_id", title="User", description="")
    volume_settings_ids: Optional[List[int]] = Field(None, alias="volume_settings_ids", title="Volumes of other partners", description="")
    livechat_lang_ids: Optional[List[int]] = Field(None, alias="livechat_lang_ids", title="Livechat languages", description="These languages, in addition to your main language, will be used to assign you to Live Chat sessions.")
    display_name: Optional[str] = Field(None, alias="display_name", title="Display Name", description="")
    create_uid: Optional[int] = Field(None, alias="create_uid", title="Created by", description="")
    create_date: Optional[str] = Field(None, alias="create_date", title="Created on", description="")
    write_uid: Optional[int] = Field(None, alias="write_uid", title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, alias="write_date", title="Last Updated on", description="")
    is_discuss_sidebar_category_channel_open: Optional[bool] = Field(None, alias="is_discuss_sidebar_category_channel_open", title="Is discuss sidebar category channel open?", description="")
    is_discuss_sidebar_category_chat_open: Optional[bool] = Field(None, alias="is_discuss_sidebar_category_chat_open", title="Is discuss sidebar category chat open?", description="")
    push_to_talk_key: Optional[str] = Field(None, alias="push_to_talk_key", title="Push-To-Talk shortcut", description="String formatted to represent a key with modifiers following this pattern: shift.ctrl.alt.key, e.g: truthy.1.true.b")
    use_push_to_talk: Optional[bool] = Field(None, alias="use_push_to_talk", title="Use the push to talk feature", description="")
    voice_active_duration: Optional[int] = Field(None, alias="voice_active_duration", title="Duration of voice activity in ms", description="How long the audio broadcast will remain active after passing the volume threshold")
    livechat_username: Optional[str] = Field(None, alias="livechat_username", title="Livechat Username", description="This username will be used as your name in the livechat channels.")
    is_discuss_sidebar_category_livechat_open: Optional[bool] = Field(None, alias="is_discuss_sidebar_category_livechat_open", title="Is category livechat open", description="")

    class Config:
        from_attributes = True

    @classmethod
    def from_execute_kw(cls, data:List[dict], fields:List[str] = []) -> List['UserSettingsModel']:
        transformed = []
        schema = UserSettingsModel.model_json_schema()
        
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

            transformed.append(cls(**filtered_item))
        return transformed
