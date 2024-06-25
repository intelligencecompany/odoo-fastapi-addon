
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class ActionWindowModel(BaseModel):
    id: Optional[int] = Field(None, title="ID", description="")
    name: str = Field("", title="Action Name", description="")
    type: str = Field("", title="Action Type", description="")
    binding_type: Any = Field(None, title="Binding Type", description="")
    context: str = Field("", title="Context Value", description="Context dictionary as Python expression, empty by default (Default: {})")
    res_model: str = Field("", title="Destination Model", description="Model name of the object to open in the view window")
    view_mode: str = Field("", title="View Mode", description="Comma-separated list of allowed view modes, such as 'form', 'tree', 'calendar', etc. (Default: tree,form)")
    xml_id: Optional[str] = Field(None, title="External ID", description="")
    binding_model_id: Optional[int] = Field(None, title="Binding Model", description="Setting a value makes this action available in the sidebar for the given model.")
    view_id: Optional[int] = Field(None, title="View Ref.", description="")
    res_id: Optional[int] = Field(None, title="Record ID", description="Database ID of record to open in form view, when ``view_mode`` is set to 'form' only")
    groups_id: Optional[List[int]] = Field(None, title="Groups", description="")
    search_view_id: Optional[int] = Field(None, title="Search View Ref.", description="")
    view_ids: Optional[List[int]] = Field(None, title="No of Views", description="")
    help: Optional[Any] = Field(None, title="Action Description", description="Optional help text for the users with a description of the target view, such as its usage and purpose.")
    binding_view_types: Optional[str] = Field(None, title="Binding View Types", description="")
    display_name: Optional[str] = Field(None, title="Display Name", description="")
    create_uid: Optional[int] = Field(None, title="Created by", description="")
    create_date: Optional[str] = Field(None, title="Created on", description="")
    write_uid: Optional[int] = Field(None, title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, title="Last Updated on", description="")
    domain: Optional[str] = Field(None, title="Domain Value", description="Optional domain filtering of the destination data, as a Python expression")
    target: Optional[Any] = Field(None, title="Target Window", description="")
    mobile_view_mode: Optional[str] = Field(None, title="Mobile View Mode", description="First view mode in mobile and small screen environments (default='kanban'). If it can't be found among available view modes, the same mode as for wider screens is used)")
    usage: Optional[str] = Field(None, title="Action Usage", description="Used to filter menu and home actions from the user form.")
    views: Optional[Any] = Field(None, title="Views", description="This function field computes the ordered list of views that should be enabled when displaying the result of an action, federating view mode, views and reference view. The result is returned as an ordered list of pairs (view_id,view_mode).")
    limit: Optional[int] = Field(None, title="Limit", description="Default limit for the list view")
    filter: Optional[bool] = Field(None, title="Filter", description="")

