
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class ShowAPIKeyModel(BaseModel):
    id: Optional[int] = Field(None, title="ID", description="")
    key: Optional[str] = Field(None, title="Key", description="")

