
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class UTMTagModel(BaseModel):
    id: Optional[int] = Field(None, title="ID", description="")
    name: str = Field("", title="Name", description="")
    color: Optional[int] = Field(None, title="Color Index", description="Tag color. No color means no display in kanban to distinguish internal tags from public categorization tags.")
    display_name: Optional[str] = Field(None, title="Display Name", description="")
    create_uid: Optional[int] = Field(None, title="Created by", description="")
    create_date: Optional[str] = Field(None, title="Created on", description="")
    write_uid: Optional[int] = Field(None, title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, title="Last Updated on", description="")

