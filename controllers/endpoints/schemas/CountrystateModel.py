
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class CountrystateModel(BaseModel):
    id: Optional[int] = Field(None, title="ID", description="")
    name: str = Field("", title="State Name", description="Administrative divisions of a country. E.g. Fed. State, Departement, Canton")
    code: str = Field("", title="State Code", description="The state code.")
    country_id: int = Field(0, title="Country", description="")
    display_name: Optional[str] = Field(None, title="Display Name", description="")
    create_uid: Optional[int] = Field(None, title="Created by", description="")
    create_date: Optional[str] = Field(None, title="Created on", description="")
    write_uid: Optional[int] = Field(None, title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, title="Last Updated on", description="")

