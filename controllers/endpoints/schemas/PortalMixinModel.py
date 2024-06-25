
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class PortalMixinModel(BaseModel):

    access_url: Optional[str] = Field(None, title="Portal Access URL", description="Customer Portal URL")
    access_token: Optional[str] = Field(None, title="Security Token", description="")
    access_warning: Optional[Any] = Field(None, title="Access warning", description="")

