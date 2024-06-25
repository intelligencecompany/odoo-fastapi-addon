
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class PricelistRuleModel(BaseModel):
    id: Optional[int] = Field(None, title="ID", description="")
    applied_on: Any = Field(None, title="Apply On", description="Pricelist Item applicable on selected option")
    base: Any = Field(None, title="Based on", description="Base price for computation.\nSales Price: The base price will be the Sales Price.\nCost Price: The base price will be the cost price.\nOther Pricelist: Computation of the base price based on another Pricelist.")
    compute_price: Any = Field(None, title="Compute Price", description="")
    pricelist_id: int = Field(0, title="Pricelist", description="")
    company_id: Optional[int] = Field(None, title="Company", description="")
    currency_id: Optional[int] = Field(None, title="Currency", description="")
    categ_id: Optional[int] = Field(None, title="Product Category", description="Specify a product category if this rule only applies to products belonging to this category or its children categories. Keep empty otherwise.")
    product_tmpl_id: Optional[int] = Field(None, title="Product", description="Specify a template if this rule only applies to one product template. Keep empty otherwise.")
    product_id: Optional[int] = Field(None, title="Product Variant", description="Specify a product if this rule only applies to one product. Keep empty otherwise.")
    base_pricelist_id: Optional[int] = Field(None, title="Other Pricelist", description="")
    date_start: Optional[str] = Field(None, title="Start Date", description="Starting datetime for the pricelist item validation\nThe displayed value depends on the timezone set in your preferences.")
    date_end: Optional[str] = Field(None, title="End Date", description="Ending datetime for the pricelist item validation\nThe displayed value depends on the timezone set in your preferences.")
    min_quantity: Optional[Any] = Field(None, title="Min. Quantity", description="For the rule to apply, bought/sold quantity must be greater than or equal to the minimum quantity specified in this field.\nExpressed in the default unit of measure of the product.")
    fixed_price: Optional[Any] = Field(None, title="Fixed Price", description="")
    percent_price: Optional[Any] = Field(None, title="Percentage Price", description="You can apply a mark-up by setting a negative discount.")
    price_discount: Optional[Any] = Field(None, title="Price Discount", description="You can apply a mark-up by setting a negative discount.")
    price_round: Optional[Any] = Field(None, title="Price Rounding", description="Sets the price so that it is a multiple of this value.\nRounding is applied after the discount and before the surcharge.\nTo have prices that end in 9.99, set rounding 10, surcharge -0.01")
    price_surcharge: Optional[Any] = Field(None, title="Price Surcharge", description="Specify the fixed amount to add or subtract (if negative) to the amount calculated with the discount.")
    price_min_margin: Optional[Any] = Field(None, title="Min. Price Margin", description="Specify the minimum amount of margin over the base price.")
    price_max_margin: Optional[Any] = Field(None, title="Max. Price Margin", description="Specify the maximum amount of margin over the base price.")
    name: Optional[str] = Field(None, title="Name", description="Explicit rule name for this pricelist line.")
    price: Optional[str] = Field(None, title="Price", description="Explicit rule name for this pricelist line.")
    rule_tip: Optional[str] = Field(None, title="Rule Tip", description="")
    display_name: Optional[str] = Field(None, title="Display Name", description="")
    create_uid: Optional[int] = Field(None, title="Created by", description="")
    create_date: Optional[str] = Field(None, title="Created on", description="")
    write_uid: Optional[int] = Field(None, title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, title="Last Updated on", description="")

