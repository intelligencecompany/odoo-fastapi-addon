
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class ResourceWorkingTimeModel(BaseModel):
    id: Optional[int] = Field(None, title="ID", description="")
    name: str = Field("", title="Name", description="")
    tz: Any = Field(None, title="Timezone", description="This field is used in order to define in which timezone the resources will work.")
    company_id: Optional[int] = Field(None, title="Company", description="")
    attendance_ids: Optional[List[int]] = Field(None, title="Working Time", description="")
    leave_ids: Optional[List[int]] = Field(None, title="Time Off", description="")
    global_leave_ids: Optional[List[int]] = Field(None, title="Global Time Off", description="")
    active: Optional[bool] = Field(None, title="Active", description="If the active field is set to false, it will allow you to hide the Working Time without removing it.")
    hours_per_day: Optional[Any] = Field(None, title="Average Hour per Day", description="Average hours per day a resource is supposed to work with this calendar.")
    tz_offset: Optional[str] = Field(None, title="Timezone offset", description="")
    two_weeks_calendar: Optional[bool] = Field(None, title="Calendar in 2 weeks mode", description="")
    two_weeks_explanation: Optional[str] = Field(None, title="Explanation", description="")
    display_name: Optional[str] = Field(None, title="Display Name", description="")
    create_uid: Optional[int] = Field(None, title="Created by", description="")
    create_date: Optional[str] = Field(None, title="Created on", description="")
    write_uid: Optional[int] = Field(None, title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, title="Last Updated on", description="")

