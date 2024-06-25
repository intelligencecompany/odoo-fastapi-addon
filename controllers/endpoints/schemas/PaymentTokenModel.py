
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class PaymentTokenModel(BaseModel):
    id: Optional[int] = Field(None, title="ID", description="")
    provider_ref: str = Field("", title="Provider Reference", description="The provider reference of the token of the transaction.")
    provider_id: int = Field(0, title="Provider", description="")
    company_id: Optional[int] = Field(None, title="Company", description="")
    payment_method_id: int = Field(0, title="Payment Method", description="")
    partner_id: int = Field(0, title="Partner", description="")
    transaction_ids: Optional[List[int]] = Field(None, title="Payment Transactions", description="")
    provider_code: Optional[Any] = Field(None, title="Provider Code", description="The technical code of this payment provider.")
    payment_method_code: Optional[str] = Field(None, title="Payment Method Code", description="The technical code of this payment method.")
    payment_details: Optional[str] = Field(None, title="Payment Details", description="The clear part of the payment method's payment details.")
    active: Optional[bool] = Field(None, title="Active", description="")
    display_name: Optional[str] = Field(None, title="Display Name", description="")
    create_uid: Optional[int] = Field(None, title="Created by", description="")
    create_date: Optional[str] = Field(None, title="Created on", description="")
    write_uid: Optional[int] = Field(None, title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, title="Last Updated on", description="")

