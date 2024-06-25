
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class GeneratePaymentLinkModel(BaseModel):
    id: Optional[int] = Field(None, title="ID", description="")
    res_model: str = Field("", title="Related Document Model", description="")
    amount: float = Field(0.0, title="Amount", description="")
    res_id: int = Field(0, title="Related Document ID", description="")
    currency_id: Optional[int] = Field(None, title="Currency", description="")
    partner_id: Optional[int] = Field(None, title="Partner", description="")
    company_id: Optional[int] = Field(None, title="Company", description="")
    amount_max: Optional[float] = Field(None, title="Amount Max", description="")
    partner_email: Optional[str] = Field(None, title="Email", description="")
    link: Optional[str] = Field(None, title="Payment Link", description="")
    warning_message: Optional[str] = Field(None, title="Warning Message", description="")
    display_name: Optional[str] = Field(None, title="Display Name", description="")
    create_uid: Optional[int] = Field(None, title="Created by", description="")
    create_date: Optional[str] = Field(None, title="Created on", description="")
    write_uid: Optional[int] = Field(None, title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, title="Last Updated on", description="")

