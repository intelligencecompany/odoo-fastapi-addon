
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class ThemeAssetModel(BaseModel):
    id: Optional[int] = Field(None, title="ID", description="")
    name: str = Field("", title="Name", description="")
    bundle: str = Field("", title="Bundle", description="")
    path: str = Field("", title="Path", description="")
    sequence: int = Field(0, title="Sequence", description="")
    copy_ids: Optional[List[int]] = Field(None, title="Assets using a copy of me", description="")
    key: Optional[str] = Field(None, title="Key", description="")
    directive: Optional[Any] = Field(None, title="Directive", description="")
    target: Optional[str] = Field(None, title="Target", description="")
    active: Optional[bool] = Field(None, title="Active", description="")
    display_name: Optional[str] = Field(None, title="Display Name", description="")
    create_uid: Optional[int] = Field(None, title="Created by", description="")
    create_date: Optional[str] = Field(None, title="Created on", description="")
    write_uid: Optional[int] = Field(None, title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, title="Last Updated on", description="")

