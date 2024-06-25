
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class LivechatSupportOperatorReportModel(BaseModel):
    id: Optional[int] = Field(None, title="ID", description="")
    partner_id: Optional[int] = Field(None, title="Operator", description="")
    livechat_channel_id: Optional[int] = Field(None, title="Channel", description="")
    channel_id: Optional[int] = Field(None, title="Conversation", description="")
    nbr_channel: Optional[int] = Field(None, title="# of Sessions", description="")
    start_date: Optional[str] = Field(None, title="Start Date of session", description="")
    time_to_answer: Optional[Any] = Field(None, title="Time to answer", description="Average time to give the first answer to the visitor")
    duration: Optional[Any] = Field(None, title="Average duration", description="Duration of the conversation (in seconds)")
    rating: Optional[Any] = Field(None, title="Average rating", description="Average rating given by the visitor")
    display_name: Optional[str] = Field(None, title="Display Name", description="")

