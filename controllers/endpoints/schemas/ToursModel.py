
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class ToursModel(BaseModel):
    id: Optional[int] = Field(None, title="ID", description="")
    name: str = Field("", title="Tour name", description="")
    user_id: Optional[int] = Field(None, title="Consumed by", description="")
    display_name: Optional[str] = Field(None, title="Display Name", description="")

