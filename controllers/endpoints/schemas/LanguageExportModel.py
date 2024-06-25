
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class LanguageExportModel(BaseModel):
    id: Optional[int] = Field(None, title="ID", description="")
    lang: Any = Field(None, title="Language", description="")
    format: Any = Field(None, title="File Format", description="")
    export_type: Any = Field(None, title="Export Type", description="")
    model_id: Optional[int] = Field(None, title="Model to Export", description="")
    name: Optional[str] = Field(None, title="File Name", description="")
    modules: Optional[List[int]] = Field(None, title="Apps To Export", description="")
    model_name: Optional[str] = Field(None, title="Model Name", description="")
    domain: Optional[str] = Field(None, title="Model Domain", description="")
    data: Optional[Any] = Field(None, title="File", description="")
    state: Optional[Any] = Field(None, title="State", description="")
    display_name: Optional[str] = Field(None, title="Display Name", description="")
    create_uid: Optional[int] = Field(None, title="Created by", description="")
    create_date: Optional[str] = Field(None, title="Created on", description="")
    write_uid: Optional[int] = Field(None, title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, title="Last Updated on", description="")

