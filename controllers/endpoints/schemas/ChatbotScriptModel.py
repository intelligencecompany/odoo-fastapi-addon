
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class ChatbotScriptModel(BaseModel):
    id: Optional[int] = Field(None, title="ID", description="")
    title: str = Field("", title="Title", description="")
    source_id: int = Field(0, title="Source", description="")
    operator_partner_id: int = Field(0, title="Bot Operator", description="")
    script_step_ids: Optional[List[int]] = Field(None, title="Script Steps", description="")
    name: Optional[str] = Field(None, title="Name", description="")
    image_1920: Optional[Any] = Field(None, title="Image", description="")
    image_1024: Optional[Any] = Field(None, title="Image 1024", description="")
    image_512: Optional[Any] = Field(None, title="Image 512", description="")
    image_256: Optional[Any] = Field(None, title="Image 256", description="")
    image_128: Optional[Any] = Field(None, title="Image 128", description="")
    active: Optional[bool] = Field(None, title="Active", description="")
    livechat_channel_count: Optional[int] = Field(None, title="Livechat Channel Count", description="")
    first_step_warning: Optional[Any] = Field(None, title="First Step Warning", description="")
    display_name: Optional[str] = Field(None, title="Display Name", description="")
    create_uid: Optional[int] = Field(None, title="Created by", description="")
    create_date: Optional[str] = Field(None, title="Created on", description="")
    write_uid: Optional[int] = Field(None, title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, title="Last Updated on", description="")

