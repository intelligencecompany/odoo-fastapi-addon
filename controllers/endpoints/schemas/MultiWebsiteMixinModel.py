
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class MultiWebsiteMixinModel(BaseModel):

    website_id: Optional[int] = Field(None, title="Website", description="Restrict publishing to this website.")

