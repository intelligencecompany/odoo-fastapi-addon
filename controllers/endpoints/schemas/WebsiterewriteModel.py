
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class WebsiterewriteModel(BaseModel):
    id: Optional[int] = Field(None, title="ID", description="")
    name: str = Field("", title="Name", description="")
    website_id: Optional[int] = Field(None, title="Website", description="")
    route_id: Optional[int] = Field(None, title="Route", description="")
    active: Optional[bool] = Field(None, title="Active", description="")
    url_from: Optional[str] = Field(None, title="URL from", description="")
    url_to: Optional[str] = Field(None, title="URL to", description="")
    redirect_type: Optional[Any] = Field(None, title="Action", description="Type of redirect/Rewrite:\n\n        301 Moved permanently: The browser will keep in cache the new url.\n        302 Moved temporarily: The browser will not keep in cache the new url and ask again the next time the new url.\n        404 Not Found: If you want remove a specific page/controller (e.g. Ecommerce is installed, but you don't want /shop on a specific website)\n        308 Redirect / Rewrite: If you want rename a controller with a new url. (Eg: /shop -> /garden - Both url will be accessible but /shop will automatically be redirected to /garden)")
    sequence: Optional[int] = Field(None, title="Sequence", description="")
    display_name: Optional[str] = Field(None, title="Display Name", description="")
    create_uid: Optional[int] = Field(None, title="Created by", description="")
    create_date: Optional[str] = Field(None, title="Created on", description="")
    write_uid: Optional[int] = Field(None, title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, title="Last Updated on", description="")

