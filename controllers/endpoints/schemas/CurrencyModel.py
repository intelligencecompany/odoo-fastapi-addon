
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class CurrencyModel(BaseModel):
    id: Optional[int] = Field(None, title="ID", description="")
    name: str = Field("", title="Currency", description="Currency Code (ISO 4217)")
    symbol: str = Field("", title="Symbol", description="Currency sign, to be used when printing amounts.")
    rate_ids: Optional[List[int]] = Field(None, title="Rates", description="")
    full_name: Optional[str] = Field(None, title="Name", description="")
    rate: Optional[Any] = Field(None, title="Current Rate", description="The rate of the currency to the currency of rate 1.")
    inverse_rate: Optional[Any] = Field(None, title="Inverse Rate", description="The currency of rate 1 to the rate of the currency.")
    rate_string: Optional[str] = Field(None, title="Rate String", description="")
    rounding: Optional[Any] = Field(None, title="Rounding Factor", description="Amounts in this currency are rounded off to the nearest multiple of the rounding factor.")
    decimal_places: Optional[int] = Field(None, title="Decimal Places", description="Decimal places taken into account for operations on amounts in this currency. It is determined by the rounding factor.")
    active: Optional[bool] = Field(None, title="Active", description="")
    position: Optional[Any] = Field(None, title="Symbol Position", description="Determines where the currency symbol should be placed after or before the amount.")
    date: Optional[str] = Field(None, title="Date", description="")
    currency_unit_label: Optional[str] = Field(None, title="Currency Unit", description="")
    currency_subunit_label: Optional[str] = Field(None, title="Currency Subunit", description="")
    is_current_company_currency: Optional[bool] = Field(None, title="Is Current Company Currency", description="")
    display_name: Optional[str] = Field(None, title="Display Name", description="")
    create_uid: Optional[int] = Field(None, title="Created by", description="")
    create_date: Optional[str] = Field(None, title="Created on", description="")
    write_uid: Optional[int] = Field(None, title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, title="Last Updated on", description="")

