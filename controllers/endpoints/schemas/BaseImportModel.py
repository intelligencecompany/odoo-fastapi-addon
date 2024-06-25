
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class BaseImportModel(BaseModel):
    id: Optional[int] = Field(None, title="ID", description="")
    res_model: Optional[str] = Field(None, title="Model", description="")
    file: Optional[Any] = Field(None, title="File", description="File to check and/or import, raw binary (not base64)")
    file_name: Optional[str] = Field(None, title="File Name", description="")
    file_type: Optional[str] = Field(None, title="File Type", description="")
    display_name: Optional[str] = Field(None, title="Display Name", description="")
    create_uid: Optional[int] = Field(None, title="Created by", description="")
    create_date: Optional[str] = Field(None, title="Created on", description="")
    write_uid: Optional[int] = Field(None, title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, title="Last Updated on", description="")

