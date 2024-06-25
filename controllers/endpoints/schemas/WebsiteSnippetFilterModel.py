
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class WebsiteSnippetFilterModel(BaseModel):
    id: Optional[int] = Field(None, title="ID", description="")
    name: str = Field("", title="Name", description="")
    field_names: str = Field("", title="Field Names", description="A list of comma-separated field names")
    limit: int = Field(0, title="Limit", description="The limit is the maximum number of records retrieved")
    website_id: Optional[int] = Field(None, title="Website", description="Restrict publishing to this website.")
    action_server_id: Optional[int] = Field(None, title="Server Action", description="")
    filter_id: Optional[int] = Field(None, title="Filter", description="")
    website_published: Optional[bool] = Field(None, title="Visible on current website", description="")
    is_published: Optional[bool] = Field(None, title="Is Published", description="")
    can_publish: Optional[bool] = Field(None, title="Can Publish", description="")
    website_url: Optional[str] = Field(None, title="Website URL", description="The full URL to access the document through the website.")
    model_name: Optional[str] = Field(None, title="Model name", description="")
    display_name: Optional[str] = Field(None, title="Display Name", description="")
    create_uid: Optional[int] = Field(None, title="Created by", description="")
    create_date: Optional[str] = Field(None, title="Created on", description="")
    write_uid: Optional[int] = Field(None, title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, title="Last Updated on", description="")

