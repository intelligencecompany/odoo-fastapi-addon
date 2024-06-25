
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class ProductAttributeCustomValueModel(BaseModel):
    id: Optional[int] = Field(None, title="ID", description="")
    custom_product_template_attribute_value_id: int = Field(0, title="Attribute Value", description="")
    name: Optional[str] = Field(None, title="Name", description="")
    custom_value: Optional[str] = Field(None, title="Custom Value", description="")
    display_name: Optional[str] = Field(None, title="Display Name", description="")
    create_uid: Optional[int] = Field(None, title="Created by", description="")
    create_date: Optional[str] = Field(None, title="Created on", description="")
    write_uid: Optional[int] = Field(None, title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, title="Last Updated on", description="")

