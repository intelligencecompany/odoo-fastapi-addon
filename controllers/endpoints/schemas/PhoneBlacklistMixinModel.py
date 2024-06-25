
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class PhoneBlacklistMixinModel(BaseModel):

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
    phone_sanitized: Optional[str] = Field(None, title="Sanitized Number", description="Field used to store sanitized phone number. Helps speeding up searches and comparisons.")
    phone_sanitized_blacklisted: Optional[bool] = Field(None, title="Phone Blacklisted", description="If the sanitized phone number is on the blacklist, the contact won't receive mass mailing sms anymore, from any list")
    phone_blacklisted: Optional[bool] = Field(None, title="Blacklisted Phone is Phone", description="Indicates if a blacklisted sanitized phone number is a phone number. Helps distinguish which number is blacklisted             when there is both a mobile and phone field in a model.")
    mobile_blacklisted: Optional[bool] = Field(None, title="Blacklisted Phone Is Mobile", description="Indicates if a blacklisted sanitized phone number is a mobile number. Helps distinguish which number is blacklisted             when there is both a mobile and phone field in a model.")
    phone_mobile_search: Optional[str] = Field(None, title="Phone/Mobile", description="")

