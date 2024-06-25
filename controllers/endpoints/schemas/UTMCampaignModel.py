
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class UTMCampaignModel(BaseModel):
    id: Optional[int] = Field(None, title="ID", description="")
    name: str = Field("", title="Campaign Identifier", description="")
    title: str = Field("", title="Campaign Name", description="")
    user_id: int = Field(0, title="Responsible", description="")
    stage_id: int = Field(0, title="Stage", description="")
    tag_ids: Optional[List[int]] = Field(None, title="Tags", description="")
    active: Optional[bool] = Field(None, title="Active", description="")
    is_auto_campaign: Optional[bool] = Field(None, title="Automatically Generated Campaign", description="Allows us to filter relevant Campaigns")
    color: Optional[int] = Field(None, title="Color Index", description="")
    display_name: Optional[str] = Field(None, title="Display Name", description="")
    create_uid: Optional[int] = Field(None, title="Created by", description="")
    create_date: Optional[str] = Field(None, title="Created on", description="")
    write_uid: Optional[int] = Field(None, title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, title="Last Updated on", description="")

