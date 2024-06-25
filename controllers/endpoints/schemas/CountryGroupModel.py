
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class CountryGroupModel(BaseModel):
    id: Optional[int] = Field(None, title="ID", description="")
    name: str = Field("", title="Name", description="")
    country_ids: Optional[List[int]] = Field(None, title="Countries", description="")
    pricelist_ids: Optional[List[int]] = Field(None, title="Pricelists", description="")
    display_name: Optional[str] = Field(None, title="Display Name", description="")
    create_uid: Optional[int] = Field(None, title="Created by", description="")
    create_date: Optional[str] = Field(None, title="Created on", description="")
    write_uid: Optional[int] = Field(None, title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, title="Last Updated on", description="")

