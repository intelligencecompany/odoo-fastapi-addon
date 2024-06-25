
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class AnalyticLineModel(BaseModel):
    id: Optional[int] = Field(None, title="ID", description="")
    name: str = Field("", title="Description", description="")
    date: str = Field("", title="Date", description="")
    amount: float = Field(0.0, title="Amount", description="")
    product_uom_id: Optional[int] = Field(None, title="Unit of Measure", description="")
    product_uom_category_id: Optional[int] = Field(None, title="UoM Category", description="Conversion between Units of Measure can only occur if they belong to the same category. The conversion will be made based on the ratios.")
    account_id: Optional[int] = Field(None, title="Project Account", description="")
    auto_account_id: Optional[int] = Field(None, title="Analytic Account", description="")
    partner_id: Optional[int] = Field(None, title="Partner", description="")
    user_id: Optional[int] = Field(None, title="User", description="")
    company_id: int = Field(0, title="Company", description="")
    currency_id: Optional[int] = Field(None, title="Currency", description="")
    x_plan2_id: Optional[int] = Field(None, title="Departments", description="")
    x_plan3_id: Optional[int] = Field(None, title="Internal", description="")
    unit_amount: Optional[Any] = Field(None, title="Quantity", description="")
    category: Optional[Any] = Field(None, title="Category", description="")
    display_name: Optional[str] = Field(None, title="Display Name", description="")
    create_uid: Optional[int] = Field(None, title="Created by", description="")
    create_date: Optional[str] = Field(None, title="Created on", description="")
    write_uid: Optional[int] = Field(None, title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, title="Last Updated on", description="")

