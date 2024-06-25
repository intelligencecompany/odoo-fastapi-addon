
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class FieldhtmlHistoryModel(BaseModel):

    html_field_history: Optional[Any] = Field(None, title="History data", description="")
    html_field_history_metadata: Optional[Any] = Field(None, title="History metadata", description="")

