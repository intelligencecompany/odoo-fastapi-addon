
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class CurrencyRateModel(BaseModel):
    id: Optional[int] = Field(None, title="ID", description="")
    name: str = Field("", title="Date", description="")
    currency_id: int = Field(0, title="Currency", description="")
    company_id: Optional[int] = Field(None, title="Company", description="")
    rate: Optional[Any] = Field(None, title="Technical Rate", description="The rate of the currency to the currency of rate 1")
    company_rate: Optional[Any] = Field(None, title="Company Rate", description="The currency of rate 1 to the rate of the currency.")
    inverse_company_rate: Optional[Any] = Field(None, title="Inverse Company Rate", description="The rate of the currency to the currency of rate 1")
    display_name: Optional[str] = Field(None, title="Display Name", description="")
    create_uid: Optional[int] = Field(None, title="Created by", description="")
    create_date: Optional[str] = Field(None, title="Created on", description="")
    write_uid: Optional[int] = Field(None, title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, title="Last Updated on", description="")

