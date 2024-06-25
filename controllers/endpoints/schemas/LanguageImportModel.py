
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class LanguageImportModel(BaseModel):
    id: Optional[int] = Field(None, title="ID", description="")
    name: str = Field("", title="Language Name", description="")
    code: str = Field("", title="ISO Code", description="ISO Language and Country code, e.g. en_US")
    data: Any = Field(None, title="File", description="")
    filename: str = Field("", title="File Name", description="")
    overwrite: Optional[bool] = Field(None, title="Overwrite Existing Terms", description="If you enable this option, existing translations (including custom ones) will be overwritten and replaced by those in this file")
    display_name: Optional[str] = Field(None, title="Display Name", description="")
    create_uid: Optional[int] = Field(None, title="Created by", description="")
    create_date: Optional[str] = Field(None, title="Created on", description="")
    write_uid: Optional[int] = Field(None, title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, title="Last Updated on", description="")

