
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class ProductTemplateAttributeLineModel(BaseModel):
    id: Optional[int] = Field(None, title="ID", description="")
    product_tmpl_id: int = Field(0, title="Product Template", description="")
    attribute_id: int = Field(0, title="Attribute", description="")
    value_ids: Optional[List[int]] = Field(None, title="Values", description="")
    product_template_value_ids: Optional[List[int]] = Field(None, title="Product Attribute Values", description="")
    active: Optional[bool] = Field(None, title="Active", description="")
    sequence: Optional[int] = Field(None, title="Sequence", description="")
    value_count: Optional[int] = Field(None, title="Value Count", description="")
    display_name: Optional[str] = Field(None, title="Display Name", description="")
    create_uid: Optional[int] = Field(None, title="Created by", description="")
    create_date: Optional[str] = Field(None, title="Created on", description="")
    write_uid: Optional[int] = Field(None, title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, title="Last Updated on", description="")

