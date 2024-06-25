
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class PaymentprovideronboardingwizardModel(BaseModel):
    id: Optional[int] = Field(None, title="ID", description="")
    payment_method: Optional[Any] = Field(None, title="Payment Method", description="")
    paypal_email_account: Optional[str] = Field(None, title="Email", description="")
    paypal_pdt_token: Optional[str] = Field(None, title="PDT Identity Token", description="")
    manual_name: Optional[str] = Field(None, title="Method", description="")
    journal_name: Optional[str] = Field(None, title="Bank Name", description="")
    acc_number: Optional[str] = Field(None, title="Account Number", description="")
    manual_post_msg: Optional[Any] = Field(None, title="Payment Instructions", description="")
    display_name: Optional[str] = Field(None, title="Display Name", description="")
    create_uid: Optional[int] = Field(None, title="Created by", description="")
    create_date: Optional[str] = Field(None, title="Created on", description="")
    write_uid: Optional[int] = Field(None, title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, title="Last Updated on", description="")

