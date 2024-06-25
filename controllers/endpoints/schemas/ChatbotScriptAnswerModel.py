
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class ChatbotScriptAnswerModel(BaseModel):
    id: Optional[int] = Field(None, title="ID", description="")
    name: str = Field("", title="Answer", description="")
    script_step_id: int = Field(0, title="Script Step", description="")
    chatbot_script_id: Optional[int] = Field(None, title="Chatbot", description="")
    sequence: Optional[int] = Field(None, title="Sequence", description="")
    redirect_link: Optional[str] = Field(None, title="Redirect Link", description="The visitor will be redirected to this link upon clicking the option (note that the script will end if the link is external to the livechat website).")
    display_name: Optional[str] = Field(None, title="Display Name", description="")
    create_uid: Optional[int] = Field(None, title="Created by", description="")
    create_date: Optional[str] = Field(None, title="Created on", description="")
    write_uid: Optional[int] = Field(None, title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, title="Last Updated on", description="")

