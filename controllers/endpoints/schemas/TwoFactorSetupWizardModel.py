
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class TwoFactorSetupWizardModel(BaseModel):
    id: Optional[int] = Field(None, title="ID", description="")
    secret: str = Field("", title="Secret", description="")
    user_id: int = Field(0, title="User", description="")
    url: Optional[str] = Field(None, title="Url", description="")
    qrcode: Optional[Any] = Field(None, title="Qrcode", description="")
    code: Optional[str] = Field(None, title="Verification Code", description="")
    display_name: Optional[str] = Field(None, title="Display Name", description="")
    create_uid: Optional[int] = Field(None, title="Created by", description="")
    create_date: Optional[str] = Field(None, title="Created on", description="")
    write_uid: Optional[int] = Field(None, title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, title="Last Updated on", description="")

