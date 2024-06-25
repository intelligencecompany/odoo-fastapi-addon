
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class RecordRuleModel(BaseModel):
    id: Optional[int] = Field(None, title="ID", description="")
    model_id: int = Field(0, title="Model", description="")
    name: Optional[str] = Field(None, title="Name", description="")
    active: Optional[bool] = Field(None, title="Active", description="If you uncheck the active field, it will disable the record rule without deleting it (if you delete a native record rule, it may be re-created when you reload the module).")
    groups: Optional[List[int]] = Field(None, title="Groups", description="")
    domain_force: Optional[Any] = Field(None, title="Domain", description="")
    perm_read: Optional[bool] = Field(None, title="Read", description="")
    perm_write: Optional[bool] = Field(None, title="Write", description="")
    perm_create: Optional[bool] = Field(None, title="Create", description="")
    perm_unlink: Optional[bool] = Field(None, title="Delete", description="")
    display_name: Optional[str] = Field(None, title="Display Name", description="")
    create_uid: Optional[int] = Field(None, title="Created by", description="")
    create_date: Optional[str] = Field(None, title="Created on", description="")
    write_uid: Optional[int] = Field(None, title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, title="Last Updated on", description="")

