
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class ModuledependencyModel(BaseModel):
    id: Optional[int] = Field(None, title="ID", description="")
    module_id: Optional[int] = Field(None, title="Module", description="")
    depend_id: Optional[int] = Field(None, title="Dependency", description="")
    name: Optional[str] = Field(None, title="Name", description="")
    state: Optional[Any] = Field(None, title="Status", description="")
    auto_install_required: Optional[bool] = Field(None, title="Auto Install Required", description="Whether this dependency blocks automatic installation of the dependent")
    display_name: Optional[str] = Field(None, title="Display Name", description="")

