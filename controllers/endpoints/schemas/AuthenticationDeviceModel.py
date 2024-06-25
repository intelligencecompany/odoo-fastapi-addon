
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class AuthenticationDeviceModel(BaseModel):
    id: Optional[int] = Field(None, title="ID", description="")
    name: str = Field("", title="Description", description="")
    user_id: int = Field(0, title="User", description="")
    scope: Optional[str] = Field(None, title="Scope", description="")
    create_date: Optional[str] = Field(None, title="Creation Date", description="")
    display_name: Optional[str] = Field(None, title="Display Name", description="")

