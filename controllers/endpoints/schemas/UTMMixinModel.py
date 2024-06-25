
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class UTMMixinModel(BaseModel):

    campaign_id: Optional[int] = Field(None, title="Campaign", description="This is a name that helps you keep track of your different campaign efforts, e.g. Fall_Drive, Christmas_Special")
    source_id: Optional[int] = Field(None, title="Source", description="This is the source of the link, e.g. Search Engine, another domain, or name of email list")
    medium_id: Optional[int] = Field(None, title="Medium", description="This is the method of delivery, e.g. Postcard, Email, or Banner Ad")

