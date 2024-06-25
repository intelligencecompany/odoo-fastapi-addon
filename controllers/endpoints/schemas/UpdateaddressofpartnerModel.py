
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class UpdateaddressofpartnerModel(BaseModel):
    id: Optional[int] = Field(None, title="ID", description="")
    partner_id: Optional[int] = Field(None, title="Partner", description="")
    letter_id: Optional[int] = Field(None, title="Letter", description="")
    state_id: Optional[int] = Field(None, title="State", description="")
    country_id: Optional[int] = Field(None, title="Country", description="")
    street: Optional[str] = Field(None, title="Street", description="")
    street2: Optional[str] = Field(None, title="Street2", description="")
    zip: Optional[str] = Field(None, title="Zip", description="")
    city: Optional[str] = Field(None, title="City", description="")
    display_name: Optional[str] = Field(None, title="Display Name", description="")
    create_uid: Optional[int] = Field(None, title="Created by", description="")
    create_date: Optional[str] = Field(None, title="Created on", description="")
    write_uid: Optional[int] = Field(None, title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, title="Last Updated on", description="")

