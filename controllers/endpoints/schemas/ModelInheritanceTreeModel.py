
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class ModelInheritanceTreeModel(BaseModel):
    id: Optional[int] = Field(None, title="ID", description="")
    model_id: int = Field(0, title="Model", description="")
    parent_id: int = Field(0, title="Parent", description="")
    parent_field_id: Optional[int] = Field(None, title="Parent Field", description="")
    display_name: Optional[str] = Field(None, title="Display Name", description="")

