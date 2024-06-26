
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class UsersAPIKeysModel(BaseModel):
    id: Optional[int] = Field(None, alias="id", title="ID", description="")
    name: str = Field("", alias="name", title="Description", description="")
    user_id: int = Field(0, alias="user_id", title="User", description="")
    scope: Optional[str] = Field(None, alias="scope", title="Scope", description="")
    create_date: Optional[str] = Field(None, alias="create_date", title="Creation Date", description="")
    display_name: Optional[str] = Field(None, alias="display_name", title="Display Name", description="")

    class Config:
        from_attributes = True

    @classmethod
    def from_execute_kw(cls, data:List[dict], fields:List[str] = []) -> List['UsersAPIKeysModel']:
        transformed = []
        schema = UsersAPIKeysModel.model_json_schema()
        
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

            transformed.append(cls(**filtered_item))
        return transformed