
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class WebsitePublishedMixinModel(BaseModel):

    website_published: Optional[bool] = Field(None, title="Visible on current website", description="")
    is_published: Optional[bool] = Field(None, title="Is Published", description="")
    can_publish: Optional[bool] = Field(None, title="Can Publish", description="")
    website_url: Optional[str] = Field(None, title="Website URL", description="The full URL to access the document through the website.")

