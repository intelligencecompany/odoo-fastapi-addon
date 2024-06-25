
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class BankAccountsModel(BaseModel):
    id: Optional[int] = Field(None, title="ID", description="")
    acc_number: str = Field("", title="Account Number", description="")
    partner_id: int = Field(0, title="Account Holder", description="")
    bank_id: Optional[int] = Field(None, title="Bank", description="")
    currency_id: Optional[int] = Field(None, title="Currency", description="")
    company_id: Optional[int] = Field(None, title="Company", description="")
    active: Optional[bool] = Field(None, title="Active", description="")
    acc_type: Optional[Any] = Field(None, title="Type", description="Bank account type: Normal or IBAN. Inferred from the bank account number.")
    sanitized_acc_number: Optional[str] = Field(None, title="Sanitized Account Number", description="")
    acc_holder_name: Optional[str] = Field(None, title="Account Holder Name", description="Account holder name, in case it is different than the name of the Account Holder")
    allow_out_payment: Optional[bool] = Field(None, title="Send Money", description="This account can be used for outgoing payments")
    bank_name: Optional[str] = Field(None, title="Name", description="")
    bank_bic: Optional[str] = Field(None, title="Bank Identifier Code", description="Sometimes called BIC or Swift.")
    sequence: Optional[int] = Field(None, title="Sequence", description="")
    display_name: Optional[str] = Field(None, title="Display Name", description="")
    create_uid: Optional[int] = Field(None, title="Created by", description="")
    create_date: Optional[str] = Field(None, title="Created on", description="")
    write_uid: Optional[int] = Field(None, title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, title="Last Updated on", description="")

