
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class ResourceWorkingTimeModel(BaseModel):
    id: Optional[int] = Field(None, alias="id", title="ID", description="")
    name: str = Field("", alias="name", title="Name", description="")
    tz: Any = Field(None, alias="tz", title="Timezone", description="This field is used in order to define in which timezone the resources will work.")
    company_id: Optional[int] = Field(None, alias="company_id", title="Company", description="")
    attendance_ids: Optional[List[int]] = Field(None, alias="attendance_ids", title="Working Time", description="")
    leave_ids: Optional[List[int]] = Field(None, alias="leave_ids", title="Time Off", description="")
    global_leave_ids: Optional[List[int]] = Field(None, alias="global_leave_ids", title="Global Time Off", description="")
    active: Optional[bool] = Field(None, alias="active", title="Active", description="If the active field is set to false, it will allow you to hide the Working Time without removing it.")
    hours_per_day: Optional[Any] = Field(None, alias="hours_per_day", title="Average Hour per Day", description="Average hours per day a resource is supposed to work with this calendar.")
    tz_offset: Optional[str] = Field(None, alias="tz_offset", title="Timezone offset", description="")
    two_weeks_calendar: Optional[bool] = Field(None, alias="two_weeks_calendar", title="Calendar in 2 weeks mode", description="")
    two_weeks_explanation: Optional[str] = Field(None, alias="two_weeks_explanation", title="Explanation", description="")
    display_name: Optional[str] = Field(None, alias="display_name", title="Display Name", description="")
    create_uid: Optional[int] = Field(None, alias="create_uid", title="Created by", description="")
    create_date: Optional[str] = Field(None, alias="create_date", title="Created on", description="")
    write_uid: Optional[int] = Field(None, alias="write_uid", title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, alias="write_date", title="Last Updated on", description="")

    class ConfigDict:
        from_attributes = True

    @classmethod
    def from_execute_kw(cls, data:List[dict], fields:List[str] = []) -> List['ResourceWorkingTimeModel']:
        transformed = []
        schema = ResourceWorkingTimeModel.model_json_schema()
        
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
