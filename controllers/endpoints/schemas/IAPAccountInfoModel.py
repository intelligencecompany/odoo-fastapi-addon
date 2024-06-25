
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class IAPAccountInfoModel(BaseModel):
    id: Optional[int] = Field(None, title="ID", description="")
    account_id: Optional[int] = Field(None, title="IAP Account", description="")
    account_token: Optional[str] = Field(None, title="Account Token", description="")
    balance: Optional[Any] = Field(None, title="Balance", description="")
    account_uuid_hashed: Optional[str] = Field(None, title="Account UUID", description="")
    service_name: Optional[str] = Field(None, title="Related Service", description="")
    description: Optional[str] = Field(None, title="Description", description="")
    warn_me: Optional[bool] = Field(None, title="Warn me", description="")
    warning_threshold: Optional[Any] = Field(None, title="Threshold", description="")
    warning_email: Optional[str] = Field(None, title="Warning Email", description="")
    unit_name: Optional[str] = Field(None, title="Unit Name", description="")
    display_name: Optional[str] = Field(None, title="Display Name", description="")
    create_uid: Optional[int] = Field(None, title="Created by", description="")
    create_date: Optional[str] = Field(None, title="Created on", description="")
    write_uid: Optional[int] = Field(None, title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, title="Last Updated on", description="")

