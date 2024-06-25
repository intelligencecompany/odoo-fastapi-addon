
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class InvitewizardModel(BaseModel):
    id: Optional[int] = Field(None, title="ID", description="")
    res_model: str = Field("", title="Related Document Model", description="Model of the followed resource")
    res_id: Optional[int] = Field(None, title="Related Document ID", description="Id of the followed resource")
    partner_ids: Optional[List[int]] = Field(None, title="Recipients", description="")
    message: Optional[Any] = Field(None, title="Message", description="")
    notify: Optional[bool] = Field(None, title="Send Notification", description="")
    display_name: Optional[str] = Field(None, title="Display Name", description="")
    create_uid: Optional[int] = Field(None, title="Created by", description="")
    create_date: Optional[str] = Field(None, title="Created on", description="")
    write_uid: Optional[int] = Field(None, title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, title="Last Updated on", description="")

