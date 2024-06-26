
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class ThemeUIViewModel(BaseModel):
    id: Optional[int] = Field(None, alias="id", title="ID", description="")
    name: str = Field("", alias="name", title="Name", description="")
    priority: int = Field(0, alias="priority", title="Priority", description="")
    inherit_id: Optional[Any] = Field(None, alias="inherit_id", title="Inherit", description="")
    copy_ids: Optional[List[int]] = Field(None, alias="copy_ids", title="Views using a copy of me", description="")
    key: Optional[str] = Field(None, alias="key", title="Key", description="")
    type: Optional[str] = Field(None, alias="type", title="Type", description="")
    mode: Optional[Any] = Field(None, alias="mode", title="Mode", description="")
    active: Optional[bool] = Field(None, alias="active", title="Active", description="")
    arch: Optional[Any] = Field(None, alias="arch", title="Arch", description="")
    arch_fs: Optional[str] = Field(None, alias="arch_fs", title="Arch Fs", description="")
    customize_show: Optional[bool] = Field(None, alias="customize_show", title="Customize Show", description="")
    display_name: Optional[str] = Field(None, alias="display_name", title="Display Name", description="")
    create_uid: Optional[int] = Field(None, alias="create_uid", title="Created by", description="")
    create_date: Optional[str] = Field(None, alias="create_date", title="Created on", description="")
    write_uid: Optional[int] = Field(None, alias="write_uid", title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, alias="write_date", title="Last Updated on", description="")

    class ConfigDict:
        from_attributes = True

    @classmethod
    def from_execute_kw(cls, data:List[dict], fields:List[str] = []) -> List['ThemeUIViewModel']:
        transformed = []
        schema = ThemeUIViewModel.model_json_schema()
        
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
