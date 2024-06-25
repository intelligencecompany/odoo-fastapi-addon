
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class ResourceMixinModel(BaseModel):

    resource_id: int = Field(0, title="Resource", description="")
    company_id: Optional[int] = Field(None, title="Company", description="")
    resource_calendar_id: Optional[int] = Field(None, title="Working Hours", description="")
    tz: Optional[Any] = Field(None, title="Timezone", description="This field is used in order to define in which timezone the resources will work.")

