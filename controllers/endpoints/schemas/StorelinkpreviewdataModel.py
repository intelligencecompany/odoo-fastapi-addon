
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class StorelinkpreviewdataModel(BaseModel):
    id: Optional[int] = Field(None, title="ID", description="")
    source_url: str = Field("", title="URL", description="")
    message_id: int = Field(0, title="Message", description="")
    og_type: Optional[str] = Field(None, title="Type", description="")
    og_title: Optional[str] = Field(None, title="Title", description="")
    og_site_name: Optional[str] = Field(None, title="Site name", description="")
    og_image: Optional[str] = Field(None, title="Image", description="")
    og_description: Optional[Any] = Field(None, title="Description", description="")
    og_mimetype: Optional[str] = Field(None, title="MIME type", description="")
    image_mimetype: Optional[str] = Field(None, title="Image MIME type", description="")
    create_date: Optional[str] = Field(None, title="Create Date", description="")
    display_name: Optional[str] = Field(None, title="Display Name", description="")
    create_uid: Optional[int] = Field(None, title="Created by", description="")
    write_uid: Optional[int] = Field(None, title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, title="Last Updated on", description="")

