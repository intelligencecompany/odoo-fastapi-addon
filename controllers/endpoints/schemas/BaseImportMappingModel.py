
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class BaseImportMappingModel(BaseModel):
    id: Optional[int] = Field(None, title="ID", description="")
    res_model: Optional[str] = Field(None, title="Res Model", description="")
    column_name: Optional[str] = Field(None, title="Column Name", description="")
    field_name: Optional[str] = Field(None, title="Field Name", description="")
    display_name: Optional[str] = Field(None, title="Display Name", description="")
    create_uid: Optional[int] = Field(None, title="Created by", description="")
    create_date: Optional[str] = Field(None, title="Created on", description="")
    write_uid: Optional[int] = Field(None, title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, title="Last Updated on", description="")

