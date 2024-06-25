
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class ProductTemplateAttributeExclusionModel(BaseModel):
    id: Optional[int] = Field(None, title="ID", description="")
    product_template_attribute_value_id: Optional[int] = Field(None, title="Attribute Value", description="")
    product_tmpl_id: int = Field(0, title="Product Template", description="")
    value_ids: Optional[List[int]] = Field(None, title="Attribute Values", description="")
    display_name: Optional[str] = Field(None, title="Display Name", description="")
    create_uid: Optional[int] = Field(None, title="Created by", description="")
    create_date: Optional[str] = Field(None, title="Created on", description="")
    write_uid: Optional[int] = Field(None, title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, title="Last Updated on", description="")

