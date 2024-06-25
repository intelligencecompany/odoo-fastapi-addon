
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class ModelConstraintModel(BaseModel):
    id: Optional[int] = Field(None, title="ID", description="")
    name: str = Field("", title="Constraint", description="PostgreSQL constraint or foreign key name.")
    model: int = Field(0, title="Model", description="")
    module: int = Field(0, title="Module", description="")
    type: str = Field("", title="Constraint Type", description="Type of the constraint: `f` for a foreign key, `u` for other constraints.")
    definition: Optional[str] = Field(None, title="Definition", description="PostgreSQL constraint definition")
    message: Optional[str] = Field(None, title="Message", description="Error message returned when the constraint is violated.")
    write_date: Optional[str] = Field(None, title="Write Date", description="")
    create_date: Optional[str] = Field(None, title="Create Date", description="")
    display_name: Optional[str] = Field(None, title="Display Name", description="")
    create_uid: Optional[int] = Field(None, title="Created by", description="")
    write_uid: Optional[int] = Field(None, title="Last Updated by", description="")

