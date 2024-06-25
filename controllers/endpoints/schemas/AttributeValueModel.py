
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class AttributeValueModel(BaseModel):
    id: Optional[int] = Field(None, title="ID", description="")
    name: str = Field("", title="Value", description="")
    attribute_id: int = Field(0, title="Attribute", description="The attribute cannot be changed once the value is used on at least one product.")
    pav_attribute_line_ids: Optional[List[int]] = Field(None, title="Lines", description="")
    sequence: Optional[int] = Field(None, title="Sequence", description="Determine the display order")
    is_used_on_products: Optional[bool] = Field(None, title="Used on Products", description="")
    default_extra_price: Optional[Any] = Field(None, title="Default Extra Price", description="")
    is_custom: Optional[bool] = Field(None, title="Is custom value", description="Allow users to input custom values for this attribute value")
    html_color: Optional[str] = Field(None, title="Color", description="Here you can set a specific HTML color index (e.g. #ff0000) to display the color if the attribute type is 'Color'.")
    display_type: Optional[Any] = Field(None, title="Display Type", description="The display type used in the Product Configurator.")
    color: Optional[int] = Field(None, title="Color Index", description="")
    image: Optional[Any] = Field(None, title="Image", description="You can upload an image that will be used as the color of the attribute value.")
    display_name: Optional[str] = Field(None, title="Display Name", description="")
    create_uid: Optional[int] = Field(None, title="Created by", description="")
    create_date: Optional[str] = Field(None, title="Created on", description="")
    write_uid: Optional[int] = Field(None, title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, title="Last Updated on", description="")

