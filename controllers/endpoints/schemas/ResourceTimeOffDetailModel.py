
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class ResourceTimeOffDetailModel(BaseModel):
    id: Optional[int] = Field(None, alias="id", title="ID", description="")
    date_from: str = Field("", alias="date_from", title="Start Date", description="")
    date_to: str = Field("", alias="date_to", title="End Date", description="")
    company_id: Optional[int] = Field(None, alias="company_id", title="Company", description="")
    calendar_id: Optional[int] = Field(None, alias="calendar_id", title="Working Hours", description="")
    resource_id: Optional[int] = Field(None, alias="resource_id", title="Resource", description="If empty, this is a generic time off for the company. If a resource is set, the time off is only for this resource")
    name: Optional[str] = Field(None, alias="name", title="Reason", description="")
    time_type: Optional[Any] = Field(None, alias="time_type", title="Time Type", description="Whether this should be computed as a time off or as work time (eg: formation)")
    display_name: Optional[str] = Field(None, alias="display_name", title="Display Name", description="")
    create_uid: Optional[int] = Field(None, alias="create_uid", title="Created by", description="")
    create_date: Optional[str] = Field(None, alias="create_date", title="Created on", description="")
    write_uid: Optional[int] = Field(None, alias="write_uid", title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, alias="write_date", title="Last Updated on", description="")

    class ConfigDict:
        from_attributes = True

    @classmethod
    def from_execute_kw(cls, item:dict[str, any]) -> 'ResourceTimeOffDetailModel':
        filtered_item = {}
        schema = ResourceTimeOffDetailModel.model_json_schema()

        for key in item:
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
    def list_from_execute_kw(cls, data:List[dict], fields:List[str] = []) -> List['ResourceTimeOffDetailModel']:
        transformed = []
        schema = ResourceTimeOffDetailModel.model_json_schema()
        
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
