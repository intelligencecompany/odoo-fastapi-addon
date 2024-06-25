
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class ChoosethesheetlayouttoprintthelabelsModel(BaseModel):
    id: Optional[int] = Field(None, title="ID", description="")
    print_format: Any = Field(None, title="Format", description="")
    custom_quantity: int = Field(0, title="Quantity", description="")
    pricelist_id: Optional[int] = Field(None, title="Pricelist", description="")
    product_ids: Optional[List[int]] = Field(None, title="Product", description="")
    product_tmpl_ids: Optional[List[int]] = Field(None, title="Product Tmpl", description="")
    extra_html: Optional[Any] = Field(None, title="Extra Content", description="")
    rows: Optional[int] = Field(None, title="Rows", description="")
    columns: Optional[int] = Field(None, title="Columns", description="")
    display_name: Optional[str] = Field(None, title="Display Name", description="")
    create_uid: Optional[int] = Field(None, title="Created by", description="")
    create_date: Optional[str] = Field(None, title="Created on", description="")
    write_uid: Optional[int] = Field(None, title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, title="Last Updated on", description="")

