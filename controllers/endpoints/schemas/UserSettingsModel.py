
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class UserSettingsModel(BaseModel):
    id: Optional[int] = Field(None, title="ID", description="")
    user_id: int = Field(0, title="User", description="")
    volume_settings_ids: Optional[List[int]] = Field(None, title="Volumes of other partners", description="")
    livechat_lang_ids: Optional[List[int]] = Field(None, title="Livechat languages", description="These languages, in addition to your main language, will be used to assign you to Live Chat sessions.")
    display_name: Optional[str] = Field(None, title="Display Name", description="")
    create_uid: Optional[int] = Field(None, title="Created by", description="")
    create_date: Optional[str] = Field(None, title="Created on", description="")
    write_uid: Optional[int] = Field(None, title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, title="Last Updated on", description="")
    is_discuss_sidebar_category_channel_open: Optional[bool] = Field(None, title="Is discuss sidebar category channel open?", description="")
    is_discuss_sidebar_category_chat_open: Optional[bool] = Field(None, title="Is discuss sidebar category chat open?", description="")
    push_to_talk_key: Optional[str] = Field(None, title="Push-To-Talk shortcut", description="String formatted to represent a key with modifiers following this pattern: shift.ctrl.alt.key, e.g: truthy.1.true.b")
    use_push_to_talk: Optional[bool] = Field(None, title="Use the push to talk feature", description="")
    voice_active_duration: Optional[int] = Field(None, title="Duration of voice activity in ms", description="How long the audio broadcast will remain active after passing the volume threshold")
    livechat_username: Optional[str] = Field(None, title="Livechat Username", description="This username will be used as your name in the livechat channels.")
    is_discuss_sidebar_category_livechat_open: Optional[bool] = Field(None, title="Is category livechat open", description="")

