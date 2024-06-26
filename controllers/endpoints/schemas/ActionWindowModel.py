
from pydantic import BaseModel, Field
from typing import Optional, List, Any, Dict

class ActionWindowModel(BaseModel):
    id: Optional[int] = Field(None, alias="id", title="ID", description="")
    name: str = Field("", alias="name", title="Action Name", description="")
    type: str = Field("", alias="type", title="Action Type", description="")
    binding_type: Any = Field(None, alias="binding_type", title="Binding Type", description="")
    context: str = Field("", alias="context", title="Context Value", description="Context dictionary as Python expression, empty by default (Default: {})")
    res_model: str = Field("", alias="res_model", title="Destination Model", description="Model name of the object to open in the view window")
    view_mode: str = Field("", alias="view_mode", title="View Mode", description="Comma-separated list of allowed view modes, such as 'form', 'tree', 'calendar', etc. (Default: tree,form)")
    xml_id: Optional[str] = Field(None, alias="xml_id", title="External ID", description="")
    binding_model_id: Optional[int] = Field(None, alias="binding_model_id", title="Binding Model", description="Setting a value makes this action available in the sidebar for the given model.")
    view_id: Optional[int] = Field(None, alias="view_id", title="View Ref.", description="")
    res_id: Optional[int] = Field(None, alias="res_id", title="Record ID", description="Database ID of record to open in form view, when ``view_mode`` is set to 'form' only")
    groups_id: Optional[List[int]] = Field(None, alias="groups_id", title="Groups", description="")
    search_view_id: Optional[int] = Field(None, alias="search_view_id", title="Search View Ref.", description="")
    view_ids: Optional[List[int]] = Field(None, alias="view_ids", title="No of Views", description="")
    help: Optional[Any] = Field(None, alias="help", title="Action Description", description="Optional help text for the users with a description of the target view, such as its usage and purpose.")
    binding_view_types: Optional[str] = Field(None, alias="binding_view_types", title="Binding View Types", description="")
    display_name: Optional[str] = Field(None, alias="display_name", title="Display Name", description="")
    create_uid: Optional[int] = Field(None, alias="create_uid", title="Created by", description="")
    create_date: Optional[str] = Field(None, alias="create_date", title="Created on", description="")
    write_uid: Optional[int] = Field(None, alias="write_uid", title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, alias="write_date", title="Last Updated on", description="")
    domain: Optional[str] = Field(None, alias="domain", title="Domain Value", description="Optional domain filtering of the destination data, as a Python expression")
    target: Optional[Any] = Field(None, alias="target", title="Target Window", description="")
    mobile_view_mode: Optional[str] = Field(None, alias="mobile_view_mode", title="Mobile View Mode", description="First view mode in mobile and small screen environments (default='kanban'). If it can't be found among available view modes, the same mode as for wider screens is used)")
    usage: Optional[str] = Field(None, alias="usage", title="Action Usage", description="Used to filter menu and home actions from the user form.")
    views: Optional[Any] = Field(None, alias="views", title="Views", description="This function field computes the ordered list of views that should be enabled when displaying the result of an action, federating view mode, views and reference view. The result is returned as an ordered list of pairs (view_id,view_mode).")
    limit: Optional[int] = Field(None, alias="limit", title="Limit", description="Default limit for the list view")
    filter: Optional[bool] = Field(None, alias="filter", title="Filter", description="")

    class ConfigDict:
        from_attributes = True

    @classmethod
    def from_execute_kw(cls, item:Dict[str, Any]) -> 'ActionWindowModel':
        filtered_item = {}
        schema = ActionWindowModel.model_json_schema()

        for key in item.keys():
            value = item[key]
            model_type = 'any'

            if 'anyOf' in schema['properties'][key] and 'type' in schema['properties'][key]['anyOf'][0]:
                model_type = schema['properties'][key]['anyOf'][0]['type']
            elif 'type' in schema['properties'][key]:
                model_type = schema['properties'][key]['type']

            if isinstance(value, list) and model_type != 'array':
                value = value[0] if item[key] else None
            
            if isinstance(value, bool) and model_type == 'string':
                value = ''

            if value is not None:
                filtered_item[key] = value

        return cls(**filtered_item).model_dump(by_alias=True)

    @classmethod
    def list_from_execute_kw(cls, data:List[dict], fields:List[str] = []) -> List['ActionWindowModel']:
        transformed = []
        schema = ActionWindowModel.model_json_schema()
        
        for item in data:
            filtered_item = {}

            if len(fields) == 0:
                fields = item.keys()

            for key in fields:
                if key in item:
                    value = item[key]
                    model_type = 'any'

                    if 'anyOf' in schema['properties'][key] and 'type' in schema['properties'][key]['anyOf'][0]:
                        model_type = schema['properties'][key]['anyOf'][0]['type']
                    elif 'type' in schema['properties'][key]:
                        model_type = schema['properties'][key]['type']

                    if isinstance(value, list) and model_type != 'array':
                        value = value[0] if item[key] else None
                    
                    if isinstance(value, bool) and model_type == 'string':
                        value = ''

                    if value is not None:
                        filtered_item[key] = value

            transformed.append(cls(**filtered_item).model_dump(by_alias=True))
        return transformed
