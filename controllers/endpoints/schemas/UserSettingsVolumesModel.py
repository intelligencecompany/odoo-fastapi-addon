
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class UserSettingsVolumesModel(BaseModel):
    id: Optional[int] = Field(None, title="ID", description="")
    user_setting_id: int = Field(0, title="User Setting", description="")
    partner_id: Optional[int] = Field(None, title="Partner", description="")
    guest_id: Optional[int] = Field(None, title="Guest", description="")
    volume: Optional[Any] = Field(None, title="Volume", description="Ranges between 0.0 and 1.0, scale depends on the browser implementation")
    display_name: Optional[str] = Field(None, title="Display Name", description="")
    create_uid: Optional[int] = Field(None, title="Created by", description="")
    create_date: Optional[str] = Field(None, title="Created on", description="")
    write_uid: Optional[int] = Field(None, title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, title="Last Updated on", description="")

