
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class UserChangePasswordWizardModel(BaseModel):
    id: Optional[int] = Field(None, title="ID", description="")
    wizard_id: int = Field(0, title="Wizard", description="")
    user_id: int = Field(0, title="User", description="")
    user_login: Optional[str] = Field(None, title="User Login", description="")
    new_passwd: Optional[str] = Field(None, title="New Password", description="")
    display_name: Optional[str] = Field(None, title="Display Name", description="")
    create_uid: Optional[int] = Field(None, title="Created by", description="")
    create_date: Optional[str] = Field(None, title="Created on", description="")
    write_uid: Optional[int] = Field(None, title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, title="Last Updated on", description="")

