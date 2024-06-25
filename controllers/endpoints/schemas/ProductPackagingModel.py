
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class ProductPackagingModel(BaseModel):
    id: Optional[int] = Field(None, title="ID", description="")
    name: str = Field("", title="Product Packaging", description="")
    product_id: int = Field(0, title="Product", description="")
    product_uom_id: Optional[int] = Field(None, title="Unit of Measure", description="Default unit of measure used for all stock operations.")
    company_id: Optional[int] = Field(None, title="Company", description="")
    sequence: Optional[int] = Field(None, title="Sequence", description="The first in the sequence is the default one.")
    qty: Optional[Any] = Field(None, title="Contained Quantity", description="Quantity of products contained in the packaging.")
    barcode: Optional[str] = Field(None, title="Barcode", description="Barcode used for packaging identification. Scan this packaging barcode from a transfer in the Barcode app to move all the contained units")
    display_name: Optional[str] = Field(None, title="Display Name", description="")
    create_uid: Optional[int] = Field(None, title="Created by", description="")
    create_date: Optional[str] = Field(None, title="Created on", description="")
    write_uid: Optional[int] = Field(None, title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, title="Last Updated on", description="")

