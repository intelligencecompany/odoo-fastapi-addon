
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class BankModel(BaseModel):
    id: Optional[int] = Field(None, title="ID", description="")
    name: str = Field("", title="Name", description="")
    street: Optional[str] = Field(None, title="Street", description="")
    street2: Optional[str] = Field(None, title="Street2", description="")
    zip: Optional[str] = Field(None, title="Zip", description="")
    city: Optional[str] = Field(None, title="City", description="")
    state: Optional[int] = Field(None, title="Fed. State", description="")
    country: Optional[int] = Field(None, title="Country", description="")
    email: Optional[str] = Field(None, title="Email", description="")
    phone: Optional[str] = Field(None, title="Phone", description="")
    active: Optional[bool] = Field(None, title="Active", description="")
    bic: Optional[str] = Field(None, title="Bank Identifier Code", description="Sometimes called BIC or Swift.")
    display_name: Optional[str] = Field(None, title="Display Name", description="")
    create_uid: Optional[int] = Field(None, title="Created by", description="")
    create_date: Optional[str] = Field(None, title="Created on", description="")
    write_uid: Optional[int] = Field(None, title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, title="Last Updated on", description="")

