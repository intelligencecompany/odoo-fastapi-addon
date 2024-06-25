
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class VisitedPagesModel(BaseModel):
    id: Optional[int] = Field(None, title="ID", description="")
    visit_datetime: str = Field("", title="Visit Date", description="")
    visitor_id: int = Field(0, title="Visitor", description="")
    page_id: Optional[int] = Field(None, title="Page", description="")
    url: Optional[Any] = Field(None, title="Url", description="")
    display_name: Optional[str] = Field(None, title="Display Name", description="")

