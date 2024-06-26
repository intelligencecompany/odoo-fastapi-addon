
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class DiscussionChannelModel(BaseModel):
    id: Optional[int] = Field(None, alias="id", title="ID", description="")
    name: str = Field("", alias="name", title="Name", description="")
    channel_type: Any = Field(None, alias="channel_type", title="Channel Type", description="Chat is private and unique between 2 persons. Group is private among invited persons. Channel can be freely joined (depending on its configuration).")
    group_public_id: Optional[int] = Field(None, alias="group_public_id", title="Authorized Group", description="")
    livechat_channel_id: Optional[int] = Field(None, alias="livechat_channel_id", title="Channel", description="")
    livechat_operator_id: Optional[int] = Field(None, alias="livechat_operator_id", title="Operator", description="")
    chatbot_current_step_id: Optional[int] = Field(None, alias="chatbot_current_step_id", title="Chatbot Current Step", description="")
    country_id: Optional[int] = Field(None, alias="country_id", title="Country", description="Country of the visitor of the channel")
    livechat_visitor_id: Optional[int] = Field(None, alias="livechat_visitor_id", title="Visitor", description="")
    message_follower_ids: Optional[List[int]] = Field(None, alias="message_follower_ids", title="Followers", description="")
    message_partner_ids: Optional[List[int]] = Field(None, alias="message_partner_ids", title="Followers (Partners)", description="")
    message_ids: Optional[List[int]] = Field(None, alias="message_ids", title="Messages", description="")
    rating_ids: Optional[List[int]] = Field(None, alias="rating_ids", title="Ratings", description="")
    website_message_ids: Optional[List[int]] = Field(None, alias="website_message_ids", title="Website Messages", description="Website communication history")
    channel_partner_ids: Optional[List[int]] = Field(None, alias="channel_partner_ids", title="Partners", description="")
    channel_member_ids: Optional[List[int]] = Field(None, alias="channel_member_ids", title="Members", description="")
    pinned_message_ids: Optional[List[int]] = Field(None, alias="pinned_message_ids", title="Pinned Messages", description="")
    rtc_session_ids: Optional[List[int]] = Field(None, alias="rtc_session_ids", title="Rtc Session", description="")
    group_ids: Optional[List[int]] = Field(None, alias="group_ids", title="Auto Subscription", description="Members of those groups will automatically added as followers. Note that they will be able to manage their subscription manually if necessary.")
    chatbot_message_ids: Optional[List[int]] = Field(None, alias="chatbot_message_ids", title="Chatbot Messages", description="")
    message_is_follower: Optional[bool] = Field(None, alias="message_is_follower", title="Is Follower", description="")
    has_message: Optional[bool] = Field(None, alias="has_message", title="Has Message", description="")
    message_needaction: Optional[bool] = Field(None, alias="message_needaction", title="Action Needed", description="If checked, new messages require your attention.")
    message_needaction_counter: Optional[int] = Field(None, alias="message_needaction_counter", title="Number of Actions", description="Number of messages requiring action")
    message_has_error: Optional[bool] = Field(None, alias="message_has_error", title="Message Delivery error", description="If checked, some messages have a delivery error.")
    message_has_error_counter: Optional[int] = Field(None, alias="message_has_error_counter", title="Number of errors", description="Number of messages with delivery error")
    message_attachment_count: Optional[int] = Field(None, alias="message_attachment_count", title="Attachment Count", description="")
    message_has_sms_error: Optional[bool] = Field(None, alias="message_has_sms_error", title="SMS Delivery error", description="If checked, some messages have a delivery error.")
    active: Optional[bool] = Field(None, alias="active", title="Active", description="Set active to false to hide the channel without removing it.")
    is_chat: Optional[bool] = Field(None, alias="is_chat", title="Is a chat", description="")
    is_editable: Optional[bool] = Field(None, alias="is_editable", title="Is Editable", description="")
    default_display_mode: Optional[Any] = Field(None, alias="default_display_mode", title="Default Display Mode", description="Determines how the channel will be displayed by default when opening it from its invitation link. No value means display text (no voice/video).")
    description: Optional[Any] = Field(None, alias="description", title="Description", description="")
    image_128: Optional[Any] = Field(None, alias="image_128", title="Image", description="")
    avatar_128: Optional[Any] = Field(None, alias="avatar_128", title="Avatar", description="")
    sfu_channel_uuid: Optional[str] = Field(None, alias="sfu_channel_uuid", title="Sfu Channel Uuid", description="")
    sfu_server_url: Optional[str] = Field(None, alias="sfu_server_url", title="Sfu Server Url", description="")
    is_member: Optional[bool] = Field(None, alias="is_member", title="Is Member", description="")
    member_count: Optional[int] = Field(None, alias="member_count", title="Member Count", description="")
    uuid: Optional[str] = Field(None, alias="uuid", title="UUID", description="")
    invitation_url: Optional[str] = Field(None, alias="invitation_url", title="Invitation URL", description="")
    allow_public_upload: Optional[bool] = Field(None, alias="allow_public_upload", title="Allow Public Upload", description="")
    display_name: Optional[str] = Field(None, alias="display_name", title="Display Name", description="")
    create_uid: Optional[int] = Field(None, alias="create_uid", title="Created by", description="")
    create_date: Optional[str] = Field(None, alias="create_date", title="Created on", description="")
    write_uid: Optional[int] = Field(None, alias="write_uid", title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, alias="write_date", title="Last Updated on", description="")
    rating_last_value: Optional[Any] = Field(None, alias="rating_last_value", title="Rating Last Value", description="")
    rating_last_feedback: Optional[Any] = Field(None, alias="rating_last_feedback", title="Rating Last Feedback", description="")
    rating_last_image: Optional[Any] = Field(None, alias="rating_last_image", title="Rating Last Image", description="")
    rating_count: Optional[int] = Field(None, alias="rating_count", title="Rating count", description="")
    rating_avg: Optional[Any] = Field(None, alias="rating_avg", title="Average Rating", description="")
    rating_avg_text: Optional[Any] = Field(None, alias="rating_avg_text", title="Rating Avg Text", description="")
    rating_percentage_satisfaction: Optional[Any] = Field(None, alias="rating_percentage_satisfaction", title="Rating Satisfaction", description="")
    rating_last_text: Optional[Any] = Field(None, alias="rating_last_text", title="Rating Text", description="")
    anonymous_name: Optional[str] = Field(None, alias="anonymous_name", title="Anonymous Name", description="")
    duration: Optional[Any] = Field(None, alias="duration", title="Duration", description="Duration of the session in hours")
    livechat_active: Optional[bool] = Field(None, alias="livechat_active", title="Is livechat ongoing?", description="Livechat session is active until visitor leaves the conversation.")

    class Config:
        from_attributes = True

    @classmethod
    def from_execute_kw(cls, data:List[dict], fields:List[str] = []) -> List['DiscussionChannelModel']:
        transformed = []
        schema = DiscussionChannelModel.model_json_schema()
        
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
