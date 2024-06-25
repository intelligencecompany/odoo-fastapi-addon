
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class ProductAttributeModel(BaseModel):
    id: Optional[int] = Field(None, title="ID", description="")
    name: str = Field("", title="Attribute", description="")
    create_variant: Any = Field(None, title="Variants Creation Mode", description="- Instantly: All possible variants are created as soon as the attribute and its values are added to a product.\n        - Dynamically: Each variant is created only when its corresponding attributes and values are added to a sales order.\n        - Never: Variants are never created for the attribute.\n        Note: the variants creation mode cannot be changed once the attribute is used on at least one product.")
    display_type: Any = Field(None, title="Display Type", description="The display type used in the Product Configurator.")
    value_ids: Optional[List[int]] = Field(None, title="Values", description="")
    attribute_line_ids: Optional[List[int]] = Field(None, title="Lines", description="")
    product_tmpl_ids: Optional[List[int]] = Field(None, title="Related Products", description="")
    sequence: Optional[int] = Field(None, title="Sequence", description="Determine the display order")
    number_related_products: Optional[int] = Field(None, title="Number Related Products", description="")
    display_name: Optional[str] = Field(None, title="Display Name", description="")
    create_uid: Optional[int] = Field(None, title="Created by", description="")
    create_date: Optional[str] = Field(None, title="Created on", description="")
    write_uid: Optional[int] = Field(None, title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, title="Last Updated on", description="")

