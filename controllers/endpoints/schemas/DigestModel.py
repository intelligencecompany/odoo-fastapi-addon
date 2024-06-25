
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class DigestModel(BaseModel):
    id: Optional[int] = Field(None, title="ID", description="")
    name: str = Field("", title="Name", description="")
    periodicity: Any = Field(None, title="Periodicity", description="")
    currency_id: Optional[int] = Field(None, title="Currency", description="")
    company_id: Optional[int] = Field(None, title="Company", description="")
    user_ids: Optional[List[int]] = Field(None, title="Recipients", description="")
    next_run_date: Optional[str] = Field(None, title="Next Mailing Date", description="")
    available_fields: Optional[str] = Field(None, title="Available Fields", description="")
    is_subscribed: Optional[bool] = Field(None, title="Is user subscribed", description="")
    state: Optional[Any] = Field(None, title="Status", description="")
    kpi_res_users_connected: Optional[bool] = Field(None, title="Connected Users", description="")
    kpi_res_users_connected_value: Optional[int] = Field(None, title="Kpi Res Users Connected Value", description="")
    kpi_mail_message_total: Optional[bool] = Field(None, title="Messages Sent", description="")
    kpi_mail_message_total_value: Optional[int] = Field(None, title="Kpi Mail Message Total Value", description="")
    display_name: Optional[str] = Field(None, title="Display Name", description="")
    create_uid: Optional[int] = Field(None, title="Created by", description="")
    create_date: Optional[str] = Field(None, title="Created on", description="")
    write_uid: Optional[int] = Field(None, title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, title="Last Updated on", description="")
    kpi_livechat_rating: Optional[bool] = Field(None, title="% of Happiness", description="")
    kpi_livechat_rating_value: Optional[Any] = Field(None, title="Kpi Livechat Rating Value", description="")
    kpi_livechat_conversations: Optional[bool] = Field(None, title="Conversations handled", description="")
    kpi_livechat_conversations_value: Optional[int] = Field(None, title="Kpi Livechat Conversations Value", description="")
    kpi_livechat_response: Optional[bool] = Field(None, title="Time to answer (sec)", description="")
    kpi_livechat_response_value: Optional[Any] = Field(None, title="Kpi Livechat Response Value", description="")

