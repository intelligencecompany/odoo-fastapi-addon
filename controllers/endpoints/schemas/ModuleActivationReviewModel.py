
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class ModuleActivationReviewModel(BaseModel):
    id: Optional[int] = Field(None, title="ID", description="")
    module_id: int = Field(0, title="Module", description="")
    module_ids: Optional[List[int]] = Field(None, title="Depending Apps", description="")
    modules_description: Optional[Any] = Field(None, title="Modules Description", description="")
    display_name: Optional[str] = Field(None, title="Display Name", description="")
    create_uid: Optional[int] = Field(None, title="Created by", description="")
    create_date: Optional[str] = Field(None, title="Created on", description="")
    write_uid: Optional[int] = Field(None, title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, title="Last Updated on", description="")

