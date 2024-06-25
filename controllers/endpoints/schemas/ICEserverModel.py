
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class ICEserverModel(BaseModel):
    id: Optional[int] = Field(None, title="ID", description="")
    server_type: Any = Field(None, title="Type", description="")
    uri: str = Field("", title="URI", description="")
    username: Optional[str] = Field(None, title="Username", description="")
    credential: Optional[str] = Field(None, title="Credential", description="")
    display_name: Optional[str] = Field(None, title="Display Name", description="")
    create_uid: Optional[int] = Field(None, title="Created by", description="")
    create_date: Optional[str] = Field(None, title="Created on", description="")
    write_uid: Optional[int] = Field(None, title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, title="Last Updated on", description="")

