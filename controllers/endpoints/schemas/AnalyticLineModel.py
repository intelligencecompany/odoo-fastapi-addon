
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class AnalyticLineModel(BaseModel):
    id: Optional[int] = Field(None, alias="id", title="ID", description="")
    name: str = Field("", alias="name", title="Description", description="")
    date: str = Field("", alias="date", title="Date", description="")
    amount: float = Field(0.0, alias="amount", title="Amount", description="")
    product_uom_id: Optional[int] = Field(None, alias="product_uom_id", title="Unit of Measure", description="")
    product_uom_category_id: Optional[int] = Field(None, alias="product_uom_category_id", title="UoM Category", description="Conversion between Units of Measure can only occur if they belong to the same category. The conversion will be made based on the ratios.")
    account_id: Optional[int] = Field(None, alias="account_id", title="Project Account", description="")
    auto_account_id: Optional[int] = Field(None, alias="auto_account_id", title="Analytic Account", description="")
    partner_id: Optional[int] = Field(None, alias="partner_id", title="Partner", description="")
    user_id: Optional[int] = Field(None, alias="user_id", title="User", description="")
    company_id: int = Field(0, alias="company_id", title="Company", description="")
    currency_id: Optional[int] = Field(None, alias="currency_id", title="Currency", description="")
    x_plan2_id: Optional[int] = Field(None, alias="x_plan2_id", title="Departments", description="")
    x_plan3_id: Optional[int] = Field(None, alias="x_plan3_id", title="Internal", description="")
    unit_amount: Optional[Any] = Field(None, alias="unit_amount", title="Quantity", description="")
    category: Optional[Any] = Field(None, alias="category", title="Category", description="")
    display_name: Optional[str] = Field(None, alias="display_name", title="Display Name", description="")
    create_uid: Optional[int] = Field(None, alias="create_uid", title="Created by", description="")
    create_date: Optional[str] = Field(None, alias="create_date", title="Created on", description="")
    write_uid: Optional[int] = Field(None, alias="write_uid", title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, alias="write_date", title="Last Updated on", description="")

    class Config:
        from_attributes = True

    @classmethod
    def from_execute_kw(cls, data:List[dict], fields:List[str] = []) -> List['AnalyticLineModel']:
        transformed = []
        schema = AnalyticLineModel.model_json_schema()
        
        for item in data:
            filtered_item = {}

            if len(fields) == 0:
                fields = item.keys()

            for key in fields:
                if key in item:
                    value = item[key]
                    model_type = 'any'

                    if 'anyOf' in schema['properties'][key] and 'type' in schema['properties'][key]['anyOf'][0]:
                        model_type = schema['properties'][key]['anyOf'][0]['type']
                    elif 'type' in schema['properties'][key]:
                        model_type = schema['properties'][key]['type']

                    if isinstance(value, list) and model_type != 'array':
                        value = value[0] if item[key] else None
                    
                    if isinstance(value, bool) and model_type == 'string':
                        value = ''

                    if value is not None:
                        filtered_item[key] = value

            transformed.append(cls(**filtered_item))
        return transformed
