
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class IAPAccountModel(BaseModel):
    id: Optional[int] = Field(None, title="ID", description="")
    account_info_id: Optional[int] = Field(None, title="Account Info", description="")
    company_ids: Optional[List[int]] = Field(None, title="Company", description="")
    account_info_ids: Optional[List[int]] = Field(None, title="Accounts from IAP", description="")
    name: Optional[str] = Field(None, title="Name", description="")
    service_name: Optional[str] = Field(None, title="Service Name", description="")
    account_token: Optional[str] = Field(None, title="Account Token", description="Account token is your authentication key for this service. Do not share it.")
    balance: Optional[str] = Field(None, title="Balance", description="")
    description: Optional[str] = Field(None, title="Description", description="")
    warn_me: Optional[bool] = Field(None, title="Warn me", description="We will send you an email when your balance gets below that threshold")
    warning_threshold: Optional[Any] = Field(None, title="Threshold", description="")
    warning_email: Optional[str] = Field(None, title="Warning Email", description="")
    show_token: Optional[bool] = Field(None, title="Show Token", description="")
    display_name: Optional[str] = Field(None, title="Display Name", description="")
    create_uid: Optional[int] = Field(None, title="Created by", description="")
    create_date: Optional[str] = Field(None, title="Created on", description="")
    write_uid: Optional[int] = Field(None, title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, title="Last Updated on", description="")

