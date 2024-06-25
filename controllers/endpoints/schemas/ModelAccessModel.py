
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class ModelAccessModel(BaseModel):
    id: Optional[int] = Field(None, title="ID", description="")
    name: str = Field("", title="Name", description="")
    model_id: int = Field(0, title="Model", description="")
    group_id: Optional[int] = Field(None, title="Group", description="")
    active: Optional[bool] = Field(None, title="Active", description="If you uncheck the active field, it will disable the ACL without deleting it (if you delete a native ACL, it will be re-created when you reload the module).")
    perm_read: Optional[bool] = Field(None, title="Read Access", description="")
    perm_write: Optional[bool] = Field(None, title="Write Access", description="")
    perm_create: Optional[bool] = Field(None, title="Create Access", description="")
    perm_unlink: Optional[bool] = Field(None, title="Delete Access", description="")
    display_name: Optional[str] = Field(None, title="Display Name", description="")
    create_uid: Optional[int] = Field(None, title="Created by", description="")
    create_date: Optional[str] = Field(None, title="Created on", description="")
    write_uid: Optional[int] = Field(None, title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, title="Last Updated on", description="")

