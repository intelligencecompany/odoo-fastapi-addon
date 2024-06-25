
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class SupplierPricelistModel(BaseModel):
    id: Optional[int] = Field(None, title="ID", description="")
    min_qty: Any = Field(None, title="Quantity", description="The quantity to purchase from this vendor to benefit from the price, expressed in the vendor Product Unit of Measure if not any, in the default unit of measure of the product otherwise.")
    price: Any = Field(None, title="Price", description="The price to purchase a product")
    delay: int = Field(0, title="Delivery Lead Time", description="Lead time in days between the confirmation of the purchase order and the receipt of the products in your warehouse. Used by the scheduler for automatic computation of the purchase order planning.")
    partner_id: int = Field(0, title="Vendor", description="")
    company_id: Optional[int] = Field(None, title="Company", description="")
    currency_id: int = Field(0, title="Currency", description="")
    product_id: Optional[int] = Field(None, title="Product Variant", description="If not set, the vendor price will apply to all variants of this product.")
    product_tmpl_id: Optional[int] = Field(None, title="Product Template", description="")
    product_name: Optional[str] = Field(None, title="Vendor Product Name", description="This vendor's product name will be used when printing a request for quotation. Keep empty to use the internal one.")
    product_code: Optional[str] = Field(None, title="Vendor Product Code", description="This vendor's product code will be used when printing a request for quotation. Keep empty to use the internal one.")
    sequence: Optional[int] = Field(None, title="Sequence", description="Assigns the priority to the list of product vendor.")
    product_uom: Optional[int] = Field(None, title="Unit of Measure", description="Default unit of measure used for purchase orders. It must be in the same category as the default unit of measure.")
    price_discounted: Optional[Any] = Field(None, title="Discounted Price", description="")
    date_start: Optional[str] = Field(None, title="Start Date", description="Start date for this vendor price")
    date_end: Optional[str] = Field(None, title="End Date", description="End date for this vendor price")
    product_variant_count: Optional[int] = Field(None, title="Variant Count", description="")
    discount: Optional[Any] = Field(None, title="Discount (%)", description="")
    display_name: Optional[str] = Field(None, title="Display Name", description="")
    create_uid: Optional[int] = Field(None, title="Created by", description="")
    create_date: Optional[str] = Field(None, title="Created on", description="")
    write_uid: Optional[int] = Field(None, title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, title="Last Updated on", description="")

