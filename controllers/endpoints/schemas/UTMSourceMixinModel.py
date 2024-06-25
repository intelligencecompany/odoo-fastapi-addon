
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class UTMSourceMixinModel(BaseModel):

    source_id: int = Field(0, title="Source", description="")
    name: Optional[str] = Field(None, title="Name", description="")

