
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class UpgradeModuleModel(BaseModel):
    id: Optional[int] = Field(None, title="ID", description="")
    module_info: Optional[Any] = Field(None, title="Apps to Update", description="")
    display_name: Optional[str] = Field(None, title="Display Name", description="")
    create_uid: Optional[int] = Field(None, title="Created by", description="")
    create_date: Optional[str] = Field(None, title="Created on", description="")
    write_uid: Optional[int] = Field(None, title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, title="Last Updated on", description="")

