
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class ChatbotMessageModel(BaseModel):
    id: Optional[int] = Field(None, title="ID", description="")
    mail_message_id: int = Field(0, title="Related Mail Message", description="")
    discuss_channel_id: int = Field(0, title="Discussion Channel", description="")
    script_step_id: int = Field(0, title="Chatbot Step", description="")
    user_script_answer_id: Optional[int] = Field(None, title="User's answer", description="")
    user_raw_answer: Optional[Any] = Field(None, title="User's raw answer", description="")
    display_name: Optional[str] = Field(None, title="Display Name", description="")
    create_uid: Optional[int] = Field(None, title="Created by", description="")
    create_date: Optional[str] = Field(None, title="Created on", description="")
    write_uid: Optional[int] = Field(None, title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, title="Last Updated on", description="")

