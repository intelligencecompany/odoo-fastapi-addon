
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class UsersDeletionRequestModel(BaseModel):
    id: Optional[int] = Field(None, title="ID", description="")
    state: Any = Field(None, title="State", description="")
    user_id: Optional[int] = Field(None, title="User", description="")
    user_id_int: Optional[int] = Field(None, title="User Id", description="")
    display_name: Optional[str] = Field(None, title="Display Name", description="")
    create_uid: Optional[int] = Field(None, title="Created by", description="")
    create_date: Optional[str] = Field(None, title="Created on", description="")
    write_uid: Optional[int] = Field(None, title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, title="Last Updated on", description="")

