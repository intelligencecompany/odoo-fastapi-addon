
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class CoverPropertiesWebsiteMixinModel(BaseModel):

    cover_properties: Optional[Any] = Field(None, title="Cover Properties", description="")

