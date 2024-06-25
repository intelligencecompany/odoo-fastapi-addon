
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class LivechatSupportChannelReportModel(BaseModel):
    id: Optional[int] = Field(None, title="ID", description="")
    channel_id: Optional[int] = Field(None, title="Conversation", description="")
    livechat_channel_id: Optional[int] = Field(None, title="Channel", description="")
    country_id: Optional[int] = Field(None, title="Country of the visitor", description="")
    partner_id: Optional[int] = Field(None, title="Operator", description="")
    uuid: Optional[str] = Field(None, title="UUID", description="")
    channel_name: Optional[str] = Field(None, title="Channel Name", description="")
    technical_name: Optional[str] = Field(None, title="Code", description="")
    start_date: Optional[str] = Field(None, title="Start Date of session", description="")
    start_hour: Optional[str] = Field(None, title="Start Hour of session", description="")
    day_number: Optional[str] = Field(None, title="Day Number", description="1 is Monday, 7 is Sunday")
    time_to_answer: Optional[Any] = Field(None, title="Time to answer (sec)", description="Average time in seconds to give the first answer to the visitor")
    start_date_hour: Optional[str] = Field(None, title="Hour of start Date of session", description="")
    duration: Optional[Any] = Field(None, title="Average duration", description="Duration of the conversation (in seconds)")
    nbr_speaker: Optional[int] = Field(None, title="# of speakers", description="Number of different speakers")
    nbr_message: Optional[int] = Field(None, title="Average message", description="Number of message in the conversation")
    is_without_answer: Optional[int] = Field(None, title="Session(s) without answer", description="A session is without answer if the operator did not answer. \n                                       If the visitor is also the operator, the session will always be answered.")
    days_of_activity: Optional[int] = Field(None, title="Days of activity", description="Number of days since the first session of the operator")
    is_anonymous: Optional[int] = Field(None, title="Is visitor anonymous", description="")
    is_happy: Optional[int] = Field(None, title="Visitor is Happy", description="")
    rating: Optional[int] = Field(None, title="Rating", description="")
    rating_text: Optional[str] = Field(None, title="Satisfaction Rate", description="")
    is_unrated: Optional[int] = Field(None, title="Session not rated", description="")
    display_name: Optional[str] = Field(None, title="Display Name", description="")

