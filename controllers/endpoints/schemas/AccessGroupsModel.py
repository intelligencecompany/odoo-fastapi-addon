
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class AccessGroupsModel(BaseModel):
    id: Optional[int] = Field(None, alias="id", title="ID", description="")
    name: str = Field("", alias="name", title="Name", description="")
    category_id: Optional[int] = Field(None, alias="category_id", title="Application", description="")
    implied_ids: Optional[List[int]] = Field(None, alias="implied_ids", title="Inherits", description="Users of this group automatically inherit those groups")
    trans_implied_ids: Optional[List[int]] = Field(None, alias="trans_implied_ids", title="Transitively inherits", description="")
    users: Optional[List[int]] = Field(None, alias="users", title="Users", description="")
    x_model_access: Optional[List[int]] = Field(None, alias="x_model_access", title="Access Controls", description="")
    rule_groups: Optional[List[int]] = Field(None, alias="rule_groups", title="Rules", description="")
    menu_access: Optional[List[int]] = Field(None, alias="menu_access", title="Access Menu", description="")
    view_access: Optional[List[int]] = Field(None, alias="view_access", title="Views", description="")
    comment: Optional[Any] = Field(None, alias="comment", title="Comment", description="")
    color: Optional[int] = Field(None, alias="color", title="Color Index", description="")
    full_name: Optional[str] = Field(None, alias="full_name", title="Group Name", description="")
    share: Optional[bool] = Field(None, alias="share", title="Share Group", description="Group created to set access rights for sharing data with some users.")
    display_name: Optional[str] = Field(None, alias="display_name", title="Display Name", description="")
    create_uid: Optional[int] = Field(None, alias="create_uid", title="Created by", description="")
    create_date: Optional[str] = Field(None, alias="create_date", title="Created on", description="")
    write_uid: Optional[int] = Field(None, alias="write_uid", title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, alias="write_date", title="Last Updated on", description="")

    class ConfigDict:
        from_attributes = True

    @classmethod
    def from_execute_kw(cls, item:dict[str, any]) -> 'AccessGroupsModel':
        filtered_item = {}
        schema = AccessGroupsModel.model_json_schema()

        for key, value in item.items():
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
    def list_from_execute_kw(cls, data:List[dict], fields:List[str] = []) -> List['AccessGroupsModel']:
        transformed = []
        schema = AccessGroupsModel.model_json_schema()
        
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
