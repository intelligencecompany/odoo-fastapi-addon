
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class AssetModel(BaseModel):
    id: Optional[int] = Field(None, alias="id", title="ID", description="")
    name: str = Field("", alias="name", title="Name", description="")
    bundle: str = Field("", alias="bundle", title="Bundle name", description="")
    path: str = Field("", alias="path", title="Path (or glob pattern)", description="")
    sequence: int = Field(0, alias="sequence", title="Sequence", description="")
    website_id: Optional[int] = Field(None, alias="website_id", title="Website", description="")
    theme_template_id: Optional[int] = Field(None, alias="theme_template_id", title="Theme Template", description="")
    directive: Optional[Any] = Field(None, alias="directive", title="Directive", description="")
    target: Optional[str] = Field(None, alias="target", title="Target", description="")
    active: Optional[bool] = Field(None, alias="active", title="active", description="")
    display_name: Optional[str] = Field(None, alias="display_name", title="Display Name", description="")
    create_uid: Optional[int] = Field(None, alias="create_uid", title="Created by", description="")
    create_date: Optional[str] = Field(None, alias="create_date", title="Created on", description="")
    write_uid: Optional[int] = Field(None, alias="write_uid", title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, alias="write_date", title="Last Updated on", description="")
    key: Optional[str] = Field(None, alias="key", title="Key", description="")

    class ConfigDict:
        from_attributes = True

    @classmethod
    def from_execute_kw(cls, data:List[dict], fields:List[str] = []) -> List['AssetModel']:
        transformed = []
        schema = AssetModel.model_json_schema()
        
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
