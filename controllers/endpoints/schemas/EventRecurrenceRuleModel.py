
from pydantic import BaseModel, Field
from typing import Optional, List, Any, Dict

class EventRecurrenceRuleModel(BaseModel):
    id: Optional[int] = Field(None, alias="id", title="ID", description="")
    base_event_id: Optional[int] = Field(None, alias="base_event_id", title="Base Event", description="")
    trigger_id: Optional[int] = Field(None, alias="trigger_id", title="Trigger", description="")
    calendar_event_ids: Optional[List[int]] = Field(None, alias="calendar_event_ids", title="Calendar Event", description="")
    name: Optional[str] = Field(None, alias="name", title="Name", description="")
    event_tz: Optional[Any] = Field(None, alias="event_tz", title="Timezone", description="")
    rrule: Optional[str] = Field(None, alias="rrule", title="Rrule", description="")
    dtstart: Optional[str] = Field(None, alias="dtstart", title="Dtstart", description="")
    rrule_type: Optional[Any] = Field(None, alias="rrule_type", title="Rrule Type", description="")
    end_type: Optional[Any] = Field(None, alias="end_type", title="End Type", description="")
    interval: Optional[int] = Field(None, alias="interval", title="Interval", description="")
    count: Optional[int] = Field(None, alias="count", title="Count", description="")
    mon: Optional[bool] = Field(None, alias="mon", title="Mon", description="")
    tue: Optional[bool] = Field(None, alias="tue", title="Tue", description="")
    wed: Optional[bool] = Field(None, alias="wed", title="Wed", description="")
    thu: Optional[bool] = Field(None, alias="thu", title="Thu", description="")
    fri: Optional[bool] = Field(None, alias="fri", title="Fri", description="")
    sat: Optional[bool] = Field(None, alias="sat", title="Sat", description="")
    sun: Optional[bool] = Field(None, alias="sun", title="Sun", description="")
    month_by: Optional[Any] = Field(None, alias="month_by", title="Month By", description="")
    day: Optional[int] = Field(None, alias="day", title="Day", description="")
    weekday: Optional[Any] = Field(None, alias="weekday", title="Weekday", description="")
    byday: Optional[Any] = Field(None, alias="byday", title="By day", description="")
    until: Optional[str] = Field(None, alias="until", title="Repeat Until", description="")
    display_name: Optional[str] = Field(None, alias="display_name", title="Display Name", description="")
    create_uid: Optional[int] = Field(None, alias="create_uid", title="Created by", description="")
    create_date: Optional[str] = Field(None, alias="create_date", title="Created on", description="")
    write_uid: Optional[int] = Field(None, alias="write_uid", title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, alias="write_date", title="Last Updated on", description="")

    class ConfigDict:
        from_attributes = True

    @classmethod
    def from_execute_kw(cls, item:dict) -> 'EventRecurrenceRuleModel':
        filtered_item = {}
        schema = EventRecurrenceRuleModel.model_json_schema()

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
    def list_from_execute_kw(cls, data:List[dict], fields:List[str] = []) -> List['EventRecurrenceRuleModel']:
        transformed = []
        schema = EventRecurrenceRuleModel.model_json_schema()
        
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
