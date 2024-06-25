
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class ActionsModel(BaseModel):
    id: Optional[int] = Field(None, title="ID", description="")
    name: str = Field("", title="Action Name", description="")
    type: str = Field("", title="Action Type", description="")
    binding_type: Any = Field(None, title="Binding Type", description="")
    xml_id: Optional[str] = Field(None, title="External ID", description="")
    binding_model_id: Optional[int] = Field(None, title="Binding Model", description="Setting a value makes this action available in the sidebar for the given model.")
    help: Optional[Any] = Field(None, title="Action Description", description="Optional help text for the users with a description of the target view, such as its usage and purpose.")
    binding_view_types: Optional[str] = Field(None, title="Binding View Types", description="")
    display_name: Optional[str] = Field(None, title="Display Name", description="")
    create_uid: Optional[int] = Field(None, title="Created by", description="")
    create_date: Optional[str] = Field(None, title="Created on", description="")
    write_uid: Optional[int] = Field(None, title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, title="Last Updated on", description="")

