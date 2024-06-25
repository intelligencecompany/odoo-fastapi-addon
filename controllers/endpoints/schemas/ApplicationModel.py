
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class ApplicationModel(BaseModel):
    id: Optional[int] = Field(None, title="ID", description="")
    name: str = Field("", title="Name", description="")
    parent_id: Optional[int] = Field(None, title="Parent Application", description="")
    xml_id: Optional[str] = Field(None, title="External ID", description="")
    child_ids: Optional[List[int]] = Field(None, title="Child Applications", description="")
    module_ids: Optional[List[int]] = Field(None, title="Modules", description="")
    description: Optional[Any] = Field(None, title="Description", description="")
    sequence: Optional[int] = Field(None, title="Sequence", description="")
    visible: Optional[bool] = Field(None, title="Visible", description="")
    exclusive: Optional[bool] = Field(None, title="Exclusive", description="")
    display_name: Optional[str] = Field(None, title="Display Name", description="")
    create_uid: Optional[int] = Field(None, title="Created by", description="")
    create_date: Optional[str] = Field(None, title="Created on", description="")
    write_uid: Optional[int] = Field(None, title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, title="Last Updated on", description="")

