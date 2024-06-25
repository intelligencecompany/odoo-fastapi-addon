
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class DocumentFollowersModel(BaseModel):
    id: Optional[int] = Field(None, title="ID", description="")
    res_model: str = Field("", title="Related Document Model Name", description="")
    res_id: Optional[Any] = Field(None, title="Related Document ID", description="Id of the followed resource")
    partner_id: int = Field(0, title="Related Partner", description="")
    subtype_ids: Optional[List[int]] = Field(None, title="Subtype", description="Message subtypes followed, meaning subtypes that will be pushed onto the user's Wall.")
    name: Optional[str] = Field(None, title="Name", description="")
    email: Optional[str] = Field(None, title="Email", description="")
    is_active: Optional[bool] = Field(None, title="Is Active", description="")
    display_name: Optional[str] = Field(None, title="Display Name", description="")

