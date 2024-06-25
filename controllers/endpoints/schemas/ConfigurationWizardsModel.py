
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class ConfigurationWizardsModel(BaseModel):
    id: Optional[int] = Field(None, title="ID", description="")
    state: Any = Field(None, title="Status", description="")
    action_id: int = Field(0, title="Action", description="")
    sequence: Optional[int] = Field(None, title="Sequence", description="")
    name: Optional[str] = Field(None, title="Name", description="")
    display_name: Optional[str] = Field(None, title="Display Name", description="")
    create_uid: Optional[int] = Field(None, title="Created by", description="")
    create_date: Optional[str] = Field(None, title="Created on", description="")
    write_uid: Optional[int] = Field(None, title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, title="Last Updated on", description="")

