
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class WorkDetailModel(BaseModel):
    id: Optional[int] = Field(None, alias="id", title="ID", description="")
    name: str = Field("", alias="name", title="Name", description="")
    dayofweek: Any = Field(None, alias="dayofweek", title="Day of Week", description="")
    hour_from: Any = Field(None, alias="hour_from", title="Work from", description="Start and End time of working.\nA specific value of 24:00 is interpreted as 23:59:59.999999.")
    hour_to: Any = Field(None, alias="hour_to", title="Work to", description="")
    day_period: Any = Field(None, alias="day_period", title="Day Period", description="")
    calendar_id: int = Field(0, alias="calendar_id", title="Resource's Calendar", description="")
    resource_id: Optional[int] = Field(None, alias="resource_id", title="Resource", description="")
    date_from: Optional[str] = Field(None, alias="date_from", title="Starting Date", description="")
    date_to: Optional[str] = Field(None, alias="date_to", title="End Date", description="")
    duration_hours: Optional[Any] = Field(None, alias="duration_hours", title="Duration (hours)", description="")
    duration_days: Optional[Any] = Field(None, alias="duration_days", title="Duration (days)", description="")
    week_type: Optional[Any] = Field(None, alias="week_type", title="Week Number", description="")
    two_weeks_calendar: Optional[bool] = Field(None, alias="two_weeks_calendar", title="Calendar in 2 weeks mode", description="")
    display_type: Optional[Any] = Field(None, alias="display_type", title="Display Type", description="Technical field for UX purpose.")
    sequence: Optional[int] = Field(None, alias="sequence", title="Sequence", description="Gives the sequence of this line when displaying the resource calendar.")
    display_name: Optional[str] = Field(None, alias="display_name", title="Display Name", description="")
    create_uid: Optional[int] = Field(None, alias="create_uid", title="Created by", description="")
    create_date: Optional[str] = Field(None, alias="create_date", title="Created on", description="")
    write_uid: Optional[int] = Field(None, alias="write_uid", title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, alias="write_date", title="Last Updated on", description="")

    class ConfigDict:
        from_attributes = True

    @classmethod
    def from_execute_kw(cls, item:dict[str, any]) -> 'WorkDetailModel':
        filtered_item = {}
        schema = WorkDetailModel.model_json_schema()

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
    def list_from_execute_kw(cls, data:List[dict], fields:List[str] = []) -> List['WorkDetailModel']:
        transformed = []
        schema = WorkDetailModel.model_json_schema()
        
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
