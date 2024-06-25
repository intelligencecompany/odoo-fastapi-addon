
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class ThemeUIViewModel(BaseModel):
    id: Optional[int] = Field(None, title="ID", description="")
    name: str = Field("", title="Name", description="")
    priority: int = Field(0, title="Priority", description="")
    inherit_id: Optional[Any] = Field(None, title="Inherit", description="")
    copy_ids: Optional[List[int]] = Field(None, title="Views using a copy of me", description="")
    key: Optional[str] = Field(None, title="Key", description="")
    type: Optional[str] = Field(None, title="Type", description="")
    mode: Optional[Any] = Field(None, title="Mode", description="")
    active: Optional[bool] = Field(None, title="Active", description="")
    arch: Optional[Any] = Field(None, title="Arch", description="")
    arch_fs: Optional[str] = Field(None, title="Arch Fs", description="")
    customize_show: Optional[bool] = Field(None, title="Customize Show", description="")
    display_name: Optional[str] = Field(None, title="Display Name", description="")
    create_uid: Optional[int] = Field(None, title="Created by", description="")
    create_date: Optional[str] = Field(None, title="Created on", description="")
    write_uid: Optional[int] = Field(None, title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, title="Last Updated on", description="")

