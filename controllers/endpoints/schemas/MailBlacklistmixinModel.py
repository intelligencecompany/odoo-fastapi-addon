
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class MailBlacklistmixinModel(BaseModel):

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
    email_normalized: Optional[str] = Field(None, title="Normalized Email", description="This field is used to search on email address as the primary email field can contain more than strictly an email address.")
    is_blacklisted: Optional[bool] = Field(None, title="Blacklist", description="If the email address is on the blacklist, the contact won't receive mass mailing anymore, from any list")
    message_bounce: Optional[int] = Field(None, title="Bounce", description="Counter of the number of bounced emails for this contact")

