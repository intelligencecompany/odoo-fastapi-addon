
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class SupplierPricelistModel(BaseModel):
    id: Optional[int] = Field(None, alias="id", title="ID", description="")
    min_qty: Any = Field(None, alias="min_qty", title="Quantity", description="The quantity to purchase from this vendor to benefit from the price, expressed in the vendor Product Unit of Measure if not any, in the default unit of measure of the product otherwise.")
    price: Any = Field(None, alias="price", title="Price", description="The price to purchase a product")
    delay: int = Field(0, alias="delay", title="Delivery Lead Time", description="Lead time in days between the confirmation of the purchase order and the receipt of the products in your warehouse. Used by the scheduler for automatic computation of the purchase order planning.")
    partner_id: int = Field(0, alias="partner_id", title="Vendor", description="")
    company_id: Optional[int] = Field(None, alias="company_id", title="Company", description="")
    currency_id: int = Field(0, alias="currency_id", title="Currency", description="")
    product_id: Optional[int] = Field(None, alias="product_id", title="Product Variant", description="If not set, the vendor price will apply to all variants of this product.")
    product_tmpl_id: Optional[int] = Field(None, alias="product_tmpl_id", title="Product Template", description="")
    product_name: Optional[str] = Field(None, alias="product_name", title="Vendor Product Name", description="This vendor's product name will be used when printing a request for quotation. Keep empty to use the internal one.")
    product_code: Optional[str] = Field(None, alias="product_code", title="Vendor Product Code", description="This vendor's product code will be used when printing a request for quotation. Keep empty to use the internal one.")
    sequence: Optional[int] = Field(None, alias="sequence", title="Sequence", description="Assigns the priority to the list of product vendor.")
    product_uom: Optional[int] = Field(None, alias="product_uom", title="Unit of Measure", description="Default unit of measure used for purchase orders. It must be in the same category as the default unit of measure.")
    price_discounted: Optional[Any] = Field(None, alias="price_discounted", title="Discounted Price", description="")
    date_start: Optional[str] = Field(None, alias="date_start", title="Start Date", description="Start date for this vendor price")
    date_end: Optional[str] = Field(None, alias="date_end", title="End Date", description="End date for this vendor price")
    product_variant_count: Optional[int] = Field(None, alias="product_variant_count", title="Variant Count", description="")
    discount: Optional[Any] = Field(None, alias="discount", title="Discount (%)", description="")
    display_name: Optional[str] = Field(None, alias="display_name", title="Display Name", description="")
    create_uid: Optional[int] = Field(None, alias="create_uid", title="Created by", description="")
    create_date: Optional[str] = Field(None, alias="create_date", title="Created on", description="")
    write_uid: Optional[int] = Field(None, alias="write_uid", title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, alias="write_date", title="Last Updated on", description="")

    class ConfigDict:
        from_attributes = True

    @classmethod
    def from_execute_kw(cls, item:dict[str, any]) -> 'SupplierPricelistModel':
        filtered_item = {}
        schema = SupplierPricelistModel.model_json_schema()

        for key, value in item.items():
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

        return cls(**filtered_item).model_dump(by_alias=True)

    @classmethod
    def list_from_execute_kw(cls, data:List[dict], fields:List[str] = []) -> List['SupplierPricelistModel']:
        transformed = []
        schema = SupplierPricelistModel.model_json_schema()
        
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

            transformed.append(cls(**filtered_item).model_dump(by_alias=True))
        return transformed
