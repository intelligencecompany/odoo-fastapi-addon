
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class PaymentCaptureWizardModel(BaseModel):
    id: Optional[int] = Field(None, title="ID", description="")
    currency_id: Optional[int] = Field(None, title="Currency", description="")
    transaction_ids: Optional[List[int]] = Field(None, title="Transaction", description="")
    authorized_amount: Optional[float] = Field(None, title="Authorized Amount", description="")
    captured_amount: Optional[float] = Field(None, title="Already Captured", description="")
    voided_amount: Optional[float] = Field(None, title="Already Voided", description="")
    available_amount: Optional[float] = Field(None, title="Maximum Capture Allowed", description="")
    amount_to_capture: Optional[float] = Field(None, title="Amount To Capture", description="")
    is_amount_to_capture_valid: Optional[bool] = Field(None, title="Is Amount To Capture Valid", description="")
    void_remaining_amount: Optional[bool] = Field(None, title="Void Remaining Amount", description="")
    support_partial_capture: Optional[bool] = Field(None, title="Support Partial Capture", description="Whether each of the transactions' provider supports the partial capture.")
    has_draft_children: Optional[bool] = Field(None, title="Has Draft Children", description="")
    has_remaining_amount: Optional[bool] = Field(None, title="Has Remaining Amount", description="")
    display_name: Optional[str] = Field(None, title="Display Name", description="")
    create_uid: Optional[int] = Field(None, title="Created by", description="")
    create_date: Optional[str] = Field(None, title="Created on", description="")
    write_uid: Optional[int] = Field(None, title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, title="Last Updated on", description="")

