
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class ProductTagModel(BaseModel):
    id: Optional[int] = Field(None, title="ID", description="")
    name: str = Field("", title="Name", description="")
    product_template_ids: Optional[List[int]] = Field(None, title="Product Templates", description="")
    product_product_ids: Optional[List[int]] = Field(None, title="Product Variants", description="")
    product_ids: Optional[List[int]] = Field(None, title="All Product Variants using this Tag", description="")
    color: Optional[str] = Field(None, title="Color", description="")
    display_name: Optional[str] = Field(None, title="Display Name", description="")
    create_uid: Optional[int] = Field(None, title="Created by", description="")
    create_date: Optional[str] = Field(None, title="Created on", description="")
    write_uid: Optional[int] = Field(None, title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, title="Last Updated on", description="")

