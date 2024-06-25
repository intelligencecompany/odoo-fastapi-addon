
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class ChatbotScriptStepModel(BaseModel):
    id: Optional[int] = Field(None, title="ID", description="")
    step_type: Any = Field(None, title="Step Type", description="")
    chatbot_script_id: int = Field(0, title="Chatbot", description="")
    answer_ids: Optional[List[int]] = Field(None, title="Answers", description="")
    triggering_answer_ids: Optional[List[int]] = Field(None, title="Only If", description="Show this step only if all of these answers have been selected.")
    message: Optional[Any] = Field(None, title="Message", description="")
    sequence: Optional[int] = Field(None, title="Sequence", description="")
    is_forward_operator_child: Optional[bool] = Field(None, title="Is Forward Operator Child", description="")
    display_name: Optional[str] = Field(None, title="Display Name", description="")
    create_uid: Optional[int] = Field(None, title="Created by", description="")
    create_date: Optional[str] = Field(None, title="Created on", description="")
    write_uid: Optional[int] = Field(None, title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, title="Last Updated on", description="")

