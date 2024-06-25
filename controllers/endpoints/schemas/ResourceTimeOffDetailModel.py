
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class ResourceTimeOffDetailModel(BaseModel):
    id: Optional[int] = Field(None, title="ID", description="")
    date_from: str = Field("", title="Start Date", description="")
    date_to: str = Field("", title="End Date", description="")
    company_id: Optional[int] = Field(None, title="Company", description="")
    calendar_id: Optional[int] = Field(None, title="Working Hours", description="")
    resource_id: Optional[int] = Field(None, title="Resource", description="If empty, this is a generic time off for the company. If a resource is set, the time off is only for this resource")
    name: Optional[str] = Field(None, title="Reason", description="")
    time_type: Optional[Any] = Field(None, title="Time Type", description="Whether this should be computed as a time off or as work time (eg: formation)")
    display_name: Optional[str] = Field(None, title="Display Name", description="")
    create_uid: Optional[int] = Field(None, title="Created by", description="")
    create_date: Optional[str] = Field(None, title="Created on", description="")
    write_uid: Optional[int] = Field(None, title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, title="Last Updated on", description="")

