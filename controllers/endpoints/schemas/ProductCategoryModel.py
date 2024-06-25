
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class ProductCategoryModel(BaseModel):
    id: Optional[int] = Field(None, title="ID", description="")
    name: str = Field("", title="Name", description="")
    parent_id: Optional[int] = Field(None, title="Parent Category", description="")
    child_id: Optional[List[int]] = Field(None, title="Child Categories", description="")
    complete_name: Optional[str] = Field(None, title="Complete Name", description="")
    parent_path: Optional[str] = Field(None, title="Parent Path", description="")
    product_count: Optional[int] = Field(None, title="# Products", description="The number of products under this category (Does not consider the children categories)")
    product_properties_definition: Optional[Any] = Field(None, title="Product Properties", description="")
    display_name: Optional[str] = Field(None, title="Display Name", description="")
    create_uid: Optional[int] = Field(None, title="Created by", description="")
    create_date: Optional[str] = Field(None, title="Created on", description="")
    write_uid: Optional[int] = Field(None, title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, title="Last Updated on", description="")

