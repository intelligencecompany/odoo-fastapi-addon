
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class AssetModel(BaseModel):
    id: Optional[int] = Field(None, title="ID", description="")
    name: str = Field("", title="Name", description="")
    bundle: str = Field("", title="Bundle name", description="")
    path: str = Field("", title="Path (or glob pattern)", description="")
    sequence: int = Field(0, title="Sequence", description="")
    website_id: Optional[int] = Field(None, title="Website", description="")
    theme_template_id: Optional[int] = Field(None, title="Theme Template", description="")
    directive: Optional[Any] = Field(None, title="Directive", description="")
    target: Optional[str] = Field(None, title="Target", description="")
    active: Optional[bool] = Field(None, title="active", description="")
    display_name: Optional[str] = Field(None, title="Display Name", description="")
    create_uid: Optional[int] = Field(None, title="Created by", description="")
    create_date: Optional[str] = Field(None, title="Created on", description="")
    write_uid: Optional[int] = Field(None, title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, title="Last Updated on", description="")
    key: Optional[str] = Field(None, title="Key", description="")

