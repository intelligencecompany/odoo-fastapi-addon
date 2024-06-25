
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class ModelDataModel(BaseModel):
    id: Optional[int] = Field(None, title="ID", description="")
    name: str = Field("", title="External Identifier", description="External Key/Identifier that can be used for data integration with third-party systems")
    model: str = Field("", title="Model Name", description="")
    module: str = Field("", title="Module", description="")
    res_id: Optional[Any] = Field(None, title="Record ID", description="ID of the target record in the database")
    complete_name: Optional[str] = Field(None, title="Complete ID", description="")
    noupdate: Optional[bool] = Field(None, title="Non Updatable", description="")
    reference: Optional[str] = Field(None, title="Reference", description="")
    display_name: Optional[str] = Field(None, title="Display Name", description="")
    create_uid: Optional[int] = Field(None, title="Created by", description="")
    create_date: Optional[str] = Field(None, title="Created on", description="")
    write_uid: Optional[int] = Field(None, title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, title="Last Updated on", description="")

