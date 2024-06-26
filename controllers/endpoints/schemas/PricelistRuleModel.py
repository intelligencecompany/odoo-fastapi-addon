
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class PricelistRuleModel(BaseModel):
    id: Optional[int] = Field(None, alias="id", title="ID", description="")
    applied_on: Any = Field(None, alias="applied_on", title="Apply On", description="Pricelist Item applicable on selected option")
    base: Any = Field(None, alias="base", title="Based on", description="Base price for computation.\nSales Price: The base price will be the Sales Price.\nCost Price: The base price will be the cost price.\nOther Pricelist: Computation of the base price based on another Pricelist.")
    compute_price: Any = Field(None, alias="compute_price", title="Compute Price", description="")
    pricelist_id: int = Field(0, alias="pricelist_id", title="Pricelist", description="")
    company_id: Optional[int] = Field(None, alias="company_id", title="Company", description="")
    currency_id: Optional[int] = Field(None, alias="currency_id", title="Currency", description="")
    categ_id: Optional[int] = Field(None, alias="categ_id", title="Product Category", description="Specify a product category if this rule only applies to products belonging to this category or its children categories. Keep empty otherwise.")
    product_tmpl_id: Optional[int] = Field(None, alias="product_tmpl_id", title="Product", description="Specify a template if this rule only applies to one product template. Keep empty otherwise.")
    product_id: Optional[int] = Field(None, alias="product_id", title="Product Variant", description="Specify a product if this rule only applies to one product. Keep empty otherwise.")
    base_pricelist_id: Optional[int] = Field(None, alias="base_pricelist_id", title="Other Pricelist", description="")
    date_start: Optional[str] = Field(None, alias="date_start", title="Start Date", description="Starting datetime for the pricelist item validation\nThe displayed value depends on the timezone set in your preferences.")
    date_end: Optional[str] = Field(None, alias="date_end", title="End Date", description="Ending datetime for the pricelist item validation\nThe displayed value depends on the timezone set in your preferences.")
    min_quantity: Optional[Any] = Field(None, alias="min_quantity", title="Min. Quantity", description="For the rule to apply, bought/sold quantity must be greater than or equal to the minimum quantity specified in this field.\nExpressed in the default unit of measure of the product.")
    fixed_price: Optional[Any] = Field(None, alias="fixed_price", title="Fixed Price", description="")
    percent_price: Optional[Any] = Field(None, alias="percent_price", title="Percentage Price", description="You can apply a mark-up by setting a negative discount.")
    price_discount: Optional[Any] = Field(None, alias="price_discount", title="Price Discount", description="You can apply a mark-up by setting a negative discount.")
    price_round: Optional[Any] = Field(None, alias="price_round", title="Price Rounding", description="Sets the price so that it is a multiple of this value.\nRounding is applied after the discount and before the surcharge.\nTo have prices that end in 9.99, set rounding 10, surcharge -0.01")
    price_surcharge: Optional[Any] = Field(None, alias="price_surcharge", title="Price Surcharge", description="Specify the fixed amount to add or subtract (if negative) to the amount calculated with the discount.")
    price_min_margin: Optional[Any] = Field(None, alias="price_min_margin", title="Min. Price Margin", description="Specify the minimum amount of margin over the base price.")
    price_max_margin: Optional[Any] = Field(None, alias="price_max_margin", title="Max. Price Margin", description="Specify the maximum amount of margin over the base price.")
    name: Optional[str] = Field(None, alias="name", title="Name", description="Explicit rule name for this pricelist line.")
    price: Optional[str] = Field(None, alias="price", title="Price", description="Explicit rule name for this pricelist line.")
    rule_tip: Optional[str] = Field(None, alias="rule_tip", title="Rule Tip", description="")
    display_name: Optional[str] = Field(None, alias="display_name", title="Display Name", description="")
    create_uid: Optional[int] = Field(None, alias="create_uid", title="Created by", description="")
    create_date: Optional[str] = Field(None, alias="create_date", title="Created on", description="")
    write_uid: Optional[int] = Field(None, alias="write_uid", title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, alias="write_date", title="Last Updated on", description="")

    class Config:
        from_attributes = True

    @classmethod
    def from_execute_kw(cls, data:List[dict], fields:List[str] = []) -> List['PricelistRuleModel']:
        transformed = []
        schema = PricelistRuleModel.model_json_schema()
        
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
