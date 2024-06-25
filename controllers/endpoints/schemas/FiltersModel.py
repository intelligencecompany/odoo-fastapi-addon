
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class FiltersModel(BaseModel):
    id: Optional[int] = Field(None, title="ID", description="")
    name: str = Field("", title="Filter Name", description="")
    domain: Any = Field(None, title="Domain", description="")
    context: Any = Field(None, title="Context", description="")
    sort: Any = Field(None, title="Sort", description="")
    user_id: Optional[int] = Field(None, title="User", description="The user this filter is private to. When left empty the filter is public and available to all users.")
    model_id: Any = Field(None, title="Model", description="")
    action_id: Optional[int] = Field(None, title="Action", description="The menu action this filter applies to. When left empty the filter applies to all menus for this model.")
    is_default: Optional[bool] = Field(None, title="Default Filter", description="")
    active: Optional[bool] = Field(None, title="Active", description="")
    display_name: Optional[str] = Field(None, title="Display Name", description="")
    create_uid: Optional[int] = Field(None, title="Created by", description="")
    create_date: Optional[str] = Field(None, title="Created on", description="")
    write_uid: Optional[int] = Field(None, title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, title="Last Updated on", description="")

