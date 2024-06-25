
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class ChannelMemberModel(BaseModel):
    id: Optional[int] = Field(None, title="ID", description="")
    partner_id: Optional[int] = Field(None, title="Partner", description="")
    guest_id: Optional[int] = Field(None, title="Guest", description="")
    channel_id: int = Field(0, title="Channel", description="")
    fetched_message_id: Optional[int] = Field(None, title="Last Fetched", description="")
    seen_message_id: Optional[int] = Field(None, title="Last Seen", description="")
    rtc_inviting_session_id: Optional[int] = Field(None, title="Ringing session", description="")
    rtc_session_ids: Optional[List[int]] = Field(None, title="RTC Sessions", description="")
    is_self: Optional[bool] = Field(None, title="Is Self", description="")
    custom_channel_name: Optional[str] = Field(None, title="Custom channel name", description="")
    message_unread_counter: Optional[int] = Field(None, title="Unread Messages Counter", description="")
    fold_state: Optional[Any] = Field(None, title="Conversation Fold State", description="")
    is_minimized: Optional[bool] = Field(None, title="Conversation is minimized", description="")
    custom_notifications: Optional[Any] = Field(None, title="Customized Notifications", description="All Messages if not specified")
    mute_until_dt: Optional[str] = Field(None, title="Mute notifications until", description="If set, the member will not receive notifications from the channel until this date.")
    is_pinned: Optional[bool] = Field(None, title="Is pinned on the interface", description="")
    last_interest_dt: Optional[str] = Field(None, title="Last Interest", description="Contains the date and time of the last interesting event that happened in this channel for this partner. This includes: creating, joining, pinning, and new message posted.")
    last_seen_dt: Optional[str] = Field(None, title="Last seen date", description="")
    display_name: Optional[str] = Field(None, title="Display Name", description="")
    create_uid: Optional[int] = Field(None, title="Created by", description="")
    create_date: Optional[str] = Field(None, title="Created on", description="")
    write_uid: Optional[int] = Field(None, title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, title="Last Updated on", description="")

