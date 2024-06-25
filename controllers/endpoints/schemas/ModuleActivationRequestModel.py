
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class ModuleActivationRequestModel(BaseModel):
    id: Optional[int] = Field(None, title="ID", description="")
    module_id: int = Field(0, title="Module", description="")
    user_id: int = Field(0, title="User", description="")
    user_ids: Optional[List[int]] = Field(None, title="Send to:", description="")
    body_html: Optional[Any] = Field(None, title="Body", description="")
    display_name: Optional[str] = Field(None, title="Display Name", description="")
    create_uid: Optional[int] = Field(None, title="Created by", description="")
    create_date: Optional[str] = Field(None, title="Created on", description="")
    write_uid: Optional[int] = Field(None, title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, title="Last Updated on", description="")

