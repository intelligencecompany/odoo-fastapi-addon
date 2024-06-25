
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class RatingMixinModel(BaseModel):

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
    rating_last_value: Optional[Any] = Field(None, title="Rating Last Value", description="")
    rating_last_feedback: Optional[Any] = Field(None, title="Rating Last Feedback", description="")
    rating_last_image: Optional[Any] = Field(None, title="Rating Last Image", description="")
    rating_count: Optional[int] = Field(None, title="Rating count", description="")
    rating_avg: Optional[Any] = Field(None, title="Average Rating", description="")
    rating_avg_text: Optional[Any] = Field(None, title="Rating Avg Text", description="")
    rating_percentage_satisfaction: Optional[Any] = Field(None, title="Rating Satisfaction", description="")
    rating_last_text: Optional[Any] = Field(None, title="Rating Text", description="")

