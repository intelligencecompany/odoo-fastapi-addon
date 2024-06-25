
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class MailBlacklistModel(BaseModel):
    id: Optional[int] = Field(None, title="ID", description="")
    email: str = Field("", title="Email Address", description="This field is case insensitive.")
    message_follower_ids: Optional[List[int]] = Field(None, title="Followers", description="")
    message_partner_ids: Optional[List[int]] = Field(None, title="Followers (Partners)", description="")
    message_ids: Optional[List[int]] = Field(None, title="Messages", description="")
    rating_ids: Optional[List[int]] = Field(None, title="Ratings", description="")
    website_message_ids: Optional[List[int]] = Field(None, title="Website Messages", description="Website communication history")
    message_is_follower: Optional[bool] = Field(None, title="Is Follower", description="")
    has_message: Optional[bool] = Field(None, title="Has Message", description="")
    message_needaction: Optional[bool] = Field(None, title="Action Needed", description="If checked, new messages require your attention.")
    message_needaction_counter: Optional[int] = Field(None, title="Number of Actions", description="Number of messages requiring action")
    message_has_error: Optional[bool] = Field(None, title="Message Delivery error", description="If checked, some messages have a delivery error.")
    message_has_error_counter: Optional[int] = Field(None, title="Number of errors", description="Number of messages with delivery error")
    message_attachment_count: Optional[int] = Field(None, title="Attachment Count", description="")
    message_has_sms_error: Optional[bool] = Field(None, title="SMS Delivery error", description="If checked, some messages have a delivery error.")
    active: Optional[bool] = Field(None, title="Active", description="")
    display_name: Optional[str] = Field(None, title="Display Name", description="")
    create_uid: Optional[int] = Field(None, title="Created by", description="")
    create_date: Optional[str] = Field(None, title="Created on", description="")
    write_uid: Optional[int] = Field(None, title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, title="Last Updated on", description="")

