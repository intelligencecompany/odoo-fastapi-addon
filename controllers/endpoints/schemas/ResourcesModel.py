
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class ResourcesModel(BaseModel):
    id: Optional[int] = Field(None, title="ID", description="")
    name: str = Field("", title="Name", description="")
    resource_type: Any = Field(None, title="Type", description="")
    time_efficiency: Any = Field(None, title="Efficiency Factor", description="This field is used to calculate the expected duration of a work order at this work center. For example, if a work order takes one hour and the efficiency factor is 100%, then the expected duration will be one hour. If the efficiency factor is 200%, however the expected duration will be 30 minutes.")
    tz: Any = Field(None, title="Timezone", description="")
    company_id: Optional[int] = Field(None, title="Company", description="")
    user_id: Optional[int] = Field(None, title="User", description="Related user name for the resource to manage its access.")
    calendar_id: Optional[int] = Field(None, title="Working Time", description="")
    active: Optional[bool] = Field(None, title="Active", description="If the active field is set to False, it will allow you to hide the resource record without removing it.")
    display_name: Optional[str] = Field(None, title="Display Name", description="")
    create_uid: Optional[int] = Field(None, title="Created by", description="")
    create_date: Optional[str] = Field(None, title="Created on", description="")
    write_uid: Optional[int] = Field(None, title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, title="Last Updated on", description="")

