
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class ActionWindowViewModel(BaseModel):
    id: Optional[int] = Field(None, title="ID", description="")
    view_mode: Any = Field(None, title="View Type", description="")
    view_id: Optional[int] = Field(None, title="View", description="")
    act_window_id: Optional[int] = Field(None, title="Action", description="")
    sequence: Optional[int] = Field(None, title="Sequence", description="")
    multi: Optional[bool] = Field(None, title="On Multiple Doc.", description="If set to true, the action will not be displayed on the right toolbar of a form view.")
    display_name: Optional[str] = Field(None, title="Display Name", description="")
    create_uid: Optional[int] = Field(None, title="Created by", description="")
    create_date: Optional[str] = Field(None, title="Created on", description="")
    write_uid: Optional[int] = Field(None, title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, title="Last Updated on", description="")

