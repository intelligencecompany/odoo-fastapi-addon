
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class ThemeAttachmentsModel(BaseModel):
    id: Optional[int] = Field(None, title="ID", description="")
    name: str = Field("", title="Name", description="")
    key: str = Field("", title="Key", description="")
    copy_ids: Optional[List[int]] = Field(None, title="Attachment using a copy of me", description="")
    url: Optional[str] = Field(None, title="Url", description="")
    display_name: Optional[str] = Field(None, title="Display Name", description="")
    create_uid: Optional[int] = Field(None, title="Created by", description="")
    create_date: Optional[str] = Field(None, title="Created on", description="")
    write_uid: Optional[int] = Field(None, title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, title="Last Updated on", description="")

