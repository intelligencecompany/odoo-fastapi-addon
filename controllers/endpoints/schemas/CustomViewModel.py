
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class CustomViewModel(BaseModel):
    id: Optional[int] = Field(None, title="ID", description="")
    arch: Any = Field(None, title="View Architecture", description="")
    ref_id: int = Field(0, title="Original View", description="")
    user_id: int = Field(0, title="User", description="")
    display_name: Optional[str] = Field(None, title="Display Name", description="")
    create_uid: Optional[int] = Field(None, title="Created by", description="")
    create_date: Optional[str] = Field(None, title="Created on", description="")
    write_uid: Optional[int] = Field(None, title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, title="Last Updated on", description="")

