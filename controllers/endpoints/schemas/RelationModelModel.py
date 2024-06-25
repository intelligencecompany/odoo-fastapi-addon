
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class RelationModelModel(BaseModel):
    id: Optional[int] = Field(None, title="ID", description="")
    name: str = Field("", title="Relation Name", description="PostgreSQL table name implementing a many2many relation.")
    model: int = Field(0, title="Model", description="")
    module: int = Field(0, title="Module", description="")
    write_date: Optional[str] = Field(None, title="Write Date", description="")
    create_date: Optional[str] = Field(None, title="Create Date", description="")
    display_name: Optional[str] = Field(None, title="Display Name", description="")
    create_uid: Optional[int] = Field(None, title="Created by", description="")
    write_uid: Optional[int] = Field(None, title="Last Updated by", description="")

