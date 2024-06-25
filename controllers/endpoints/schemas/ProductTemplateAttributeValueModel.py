
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class ProductTemplateAttributeValueModel(BaseModel):
    id: Optional[int] = Field(None, title="ID", description="")
    product_attribute_value_id: int = Field(0, title="Attribute Value", description="")
    attribute_line_id: int = Field(0, title="Attribute Line", description="")
    currency_id: Optional[int] = Field(None, title="Currency", description="")
    product_tmpl_id: Optional[int] = Field(None, title="Product Template", description="")
    attribute_id: Optional[int] = Field(None, title="Attribute", description="")
    ptav_product_variant_ids: Optional[List[int]] = Field(None, title="Related Variants", description="")
    ptav_active: Optional[bool] = Field(None, title="Active", description="")
    name: Optional[str] = Field(None, title="Value", description="")
    price_extra: Optional[Any] = Field(None, title="Value Price Extra", description="Extra price for the variant with this attribute value on sale price. eg. 200 price extra, 1000 + 200 = 1200.")
    exclude_for: Optional[List[int]] = Field(None, title="Exclude for", description="Make this attribute value not compatible with other values of the product or some attribute values of optional and accessory products.")
    html_color: Optional[str] = Field(None, title="HTML Color Index", description="Here you can set a specific HTML color index (e.g. #ff0000) to display the color if the attribute type is 'Color'.")
    is_custom: Optional[bool] = Field(None, title="Is custom value", description="Allow users to input custom values for this attribute value")
    display_type: Optional[Any] = Field(None, title="Display Type", description="The display type used in the Product Configurator.")
    color: Optional[int] = Field(None, title="Color", description="")
    image: Optional[Any] = Field(None, title="Image", description="You can upload an image that will be used as the color of the attribute value.")
    display_name: Optional[str] = Field(None, title="Display Name", description="")
    create_uid: Optional[int] = Field(None, title="Created by", description="")
    create_date: Optional[str] = Field(None, title="Created on", description="")
    write_uid: Optional[int] = Field(None, title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, title="Last Updated on", description="")

