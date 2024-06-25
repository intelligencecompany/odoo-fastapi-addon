
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class WorkDetailModel(BaseModel):
    id: Optional[int] = Field(None, title="ID", description="")
    name: str = Field("", title="Name", description="")
    dayofweek: Any = Field(None, title="Day of Week", description="")
    hour_from: Any = Field(None, title="Work from", description="Start and End time of working.\nA specific value of 24:00 is interpreted as 23:59:59.999999.")
    hour_to: Any = Field(None, title="Work to", description="")
    day_period: Any = Field(None, title="Day Period", description="")
    calendar_id: int = Field(0, title="Resource's Calendar", description="")
    resource_id: Optional[int] = Field(None, title="Resource", description="")
    date_from: Optional[str] = Field(None, title="Starting Date", description="")
    date_to: Optional[str] = Field(None, title="End Date", description="")
    duration_hours: Optional[Any] = Field(None, title="Duration (hours)", description="")
    duration_days: Optional[Any] = Field(None, title="Duration (days)", description="")
    week_type: Optional[Any] = Field(None, title="Week Number", description="")
    two_weeks_calendar: Optional[bool] = Field(None, title="Calendar in 2 weeks mode", description="")
    display_type: Optional[Any] = Field(None, title="Display Type", description="Technical field for UX purpose.")
    sequence: Optional[int] = Field(None, title="Sequence", description="Gives the sequence of this line when displaying the resource calendar.")
    display_name: Optional[str] = Field(None, title="Display Name", description="")
    create_uid: Optional[int] = Field(None, title="Created by", description="")
    create_date: Optional[str] = Field(None, title="Created on", description="")
    write_uid: Optional[int] = Field(None, title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, title="Last Updated on", description="")

