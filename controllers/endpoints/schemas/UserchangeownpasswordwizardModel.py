
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class UserchangeownpasswordwizardModel(BaseModel):
    id: Optional[int] = Field(None, title="ID", description="")
    new_password: Optional[str] = Field(None, title="New Password", description="")
    confirm_password: Optional[str] = Field(None, title="New Password (Confirmation)", description="")
    display_name: Optional[str] = Field(None, title="Display Name", description="")
    create_uid: Optional[int] = Field(None, title="Created by", description="")
    create_date: Optional[str] = Field(None, title="Created on", description="")
    write_uid: Optional[int] = Field(None, title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, title="Last Updated on", description="")

