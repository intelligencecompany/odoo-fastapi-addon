
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class ResourcesModel(BaseModel):
    id: Optional[int] = Field(None, alias="id", title="ID", description="")
    name: str = Field("", alias="name", title="Name", description="")
    resource_type: Any = Field(None, alias="resource_type", title="Type", description="")
    time_efficiency: Any = Field(None, alias="time_efficiency", title="Efficiency Factor", description="This field is used to calculate the expected duration of a work order at this work center. For example, if a work order takes one hour and the efficiency factor is 100%, then the expected duration will be one hour. If the efficiency factor is 200%, however the expected duration will be 30 minutes.")
    tz: Any = Field(None, alias="tz", title="Timezone", description="")
    company_id: Optional[int] = Field(None, alias="company_id", title="Company", description="")
    user_id: Optional[int] = Field(None, alias="user_id", title="User", description="Related user name for the resource to manage its access.")
    calendar_id: Optional[int] = Field(None, alias="calendar_id", title="Working Time", description="")
    active: Optional[bool] = Field(None, alias="active", title="Active", description="If the active field is set to False, it will allow you to hide the resource record without removing it.")
    display_name: Optional[str] = Field(None, alias="display_name", title="Display Name", description="")
    create_uid: Optional[int] = Field(None, alias="create_uid", title="Created by", description="")
    create_date: Optional[str] = Field(None, alias="create_date", title="Created on", description="")
    write_uid: Optional[int] = Field(None, alias="write_uid", title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, alias="write_date", title="Last Updated on", description="")

    class Config:
        from_attributes = True

    @classmethod
    def from_execute_kw(cls, data:List[dict], fields:List[str] = []) -> List['ResourcesModel']:
        transformed = []
        schema = ResourcesModel.model_json_schema()
        
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
