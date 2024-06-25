
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class TriggeredactionsModel(BaseModel):
    id: Optional[int] = Field(None, title="ID", description="")
    cron_id: Optional[int] = Field(None, title="Cron", description="")
    call_at: Optional[str] = Field(None, title="Call At", description="")
    display_name: Optional[str] = Field(None, title="Display Name", description="")
    create_uid: Optional[int] = Field(None, title="Created by", description="")
    create_date: Optional[str] = Field(None, title="Created on", description="")
    write_uid: Optional[int] = Field(None, title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, title="Last Updated on", description="")

