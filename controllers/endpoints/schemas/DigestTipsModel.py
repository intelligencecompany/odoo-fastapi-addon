
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class DigestTipsModel(BaseModel):
    id: Optional[int] = Field(None, title="ID", description="")
    group_id: Optional[int] = Field(None, title="Authorized Group", description="")
    user_ids: Optional[List[int]] = Field(None, title="Recipients", description="Users having already received this tip")
    sequence: Optional[int] = Field(None, title="Sequence", description="Used to display digest tip in email template base on order")
    name: Optional[str] = Field(None, title="Name", description="")
    tip_description: Optional[Any] = Field(None, title="Tip description", description="")
    display_name: Optional[str] = Field(None, title="Display Name", description="")
    create_uid: Optional[int] = Field(None, title="Created by", description="")
    create_date: Optional[str] = Field(None, title="Created on", description="")
    write_uid: Optional[int] = Field(None, title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, title="Last Updated on", description="")

