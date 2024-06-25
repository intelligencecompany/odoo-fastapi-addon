
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class LoggingModel(BaseModel):
    id: Optional[int] = Field(None, title="ID", description="")
    name: str = Field("", title="Name", description="")
    type: Any = Field(None, title="Type", description="")
    message: Any = Field(None, title="Message", description="")
    path: str = Field("", title="Path", description="")
    func: str = Field("", title="Function", description="")
    line: str = Field("", title="Line", description="")
    create_uid: Optional[int] = Field(None, title="Created by", description="")
    create_date: Optional[str] = Field(None, title="Created on", description="")
    write_uid: Optional[int] = Field(None, title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, title="Last Updated on", description="")
    dbname: Optional[str] = Field(None, title="Database Name", description="")
    level: Optional[str] = Field(None, title="Level", description="")
    display_name: Optional[str] = Field(None, title="Display Name", description="")

