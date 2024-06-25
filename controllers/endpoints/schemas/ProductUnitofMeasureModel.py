
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class ProductUnitofMeasureModel(BaseModel):
    id: Optional[int] = Field(None, title="ID", description="")
    name: str = Field("", title="Unit of Measure", description="")
    factor: Any = Field(None, title="Ratio", description="How much bigger or smaller this unit is compared to the reference Unit of Measure for this category: 1 * (reference unit) = ratio * (this unit)")
    factor_inv: Any = Field(None, title="Bigger Ratio", description="How many times this Unit of Measure is bigger than the reference Unit of Measure in this category: 1 * (this unit) = ratio * (reference unit)")
    rounding: Any = Field(None, title="Rounding Precision", description="The computed quantity will be a multiple of this value. Use 1.0 for a Unit of Measure that cannot be further split, such as a piece.")
    uom_type: Any = Field(None, title="Type", description="")
    category_id: int = Field(0, title="Category", description="Conversion between Units of Measure can only occur if they belong to the same category. The conversion will be made based on the ratios.")
    active: Optional[bool] = Field(None, title="Active", description="Uncheck the active field to disable a unit of measure without deleting it.")
    ratio: Optional[Any] = Field(None, title="Combined Ratio", description="")
    color: Optional[int] = Field(None, title="Color", description="")
    display_name: Optional[str] = Field(None, title="Display Name", description="")
    create_uid: Optional[int] = Field(None, title="Created by", description="")
    create_date: Optional[str] = Field(None, title="Created on", description="")
    write_uid: Optional[int] = Field(None, title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, title="Last Updated on", description="")

