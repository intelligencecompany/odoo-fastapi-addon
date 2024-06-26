
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class MenuModel(BaseModel):
    id: Optional[int] = Field(None, alias="id", title="ID", description="")
    name: str = Field("", alias="name", title="Menu", description="")
    child_id: Optional[List[int]] = Field(None, alias="child_id", title="Child IDs", description="")
    parent_id: Optional[int] = Field(None, alias="parent_id", title="Parent Menu", description="")
    groups_id: Optional[List[int]] = Field(None, alias="groups_id", title="Groups", description="If you have groups, the visibility of this menu will be based on these groups. If this field is empty, Odoo will compute visibility based on the related object's read access.")
    active: Optional[bool] = Field(None, alias="active", title="Active", description="")
    sequence: Optional[int] = Field(None, alias="sequence", title="Sequence", description="")
    parent_path: Optional[str] = Field(None, alias="parent_path", title="Parent Path", description="")
    complete_name: Optional[str] = Field(None, alias="complete_name", title="Full Path", description="")
    web_icon: Optional[str] = Field(None, alias="web_icon", title="Web Icon File", description="")
    action: Optional[Any] = Field(None, alias="action", title="Action", description="")
    web_icon_data: Optional[Any] = Field(None, alias="web_icon_data", title="Web Icon Image", description="")
    display_name: Optional[str] = Field(None, alias="display_name", title="Display Name", description="")
    create_uid: Optional[int] = Field(None, alias="create_uid", title="Created by", description="")
    create_date: Optional[str] = Field(None, alias="create_date", title="Created on", description="")
    write_uid: Optional[int] = Field(None, alias="write_uid", title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, alias="write_date", title="Last Updated on", description="")

    class ConfigDict:
        from_attributes = True

    @classmethod
    def from_execute_kw(cls, item:dict) -> 'MenuModel':
        filtered_item = {}
        schema = MenuModel.model_json_schema()

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
    def list_from_execute_kw(cls, data:List[dict], fields:List[str] = []) -> List['MenuModel']:
        transformed = []
        schema = MenuModel.model_json_schema()
        
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
