
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class PaperFormatConfigModel(BaseModel):
    id: Optional[int] = Field(None, title="ID", description="")
    name: str = Field("", title="Name", description="")
    dpi: int = Field(0, title="Output DPI", description="")
    report_ids: Optional[List[int]] = Field(None, title="Associated reports", description="Explicitly associated reports")
    default: Optional[bool] = Field(None, title="Default paper format?", description="")
    format: Optional[Any] = Field(None, title="Paper size", description="Select Proper Paper size")
    margin_top: Optional[Any] = Field(None, title="Top Margin (mm)", description="")
    margin_bottom: Optional[Any] = Field(None, title="Bottom Margin (mm)", description="")
    margin_left: Optional[Any] = Field(None, title="Left Margin (mm)", description="")
    margin_right: Optional[Any] = Field(None, title="Right Margin (mm)", description="")
    page_height: Optional[int] = Field(None, title="Page height (mm)", description="")
    page_width: Optional[int] = Field(None, title="Page width (mm)", description="")
    orientation: Optional[Any] = Field(None, title="Orientation", description="")
    header_line: Optional[bool] = Field(None, title="Display a header line", description="")
    header_spacing: Optional[int] = Field(None, title="Header spacing", description="")
    disable_shrinking: Optional[bool] = Field(None, title="Disable smart shrinking", description="")
    print_page_width: Optional[Any] = Field(None, title="Print page width (mm)", description="")
    print_page_height: Optional[Any] = Field(None, title="Print page height (mm)", description="")
    display_name: Optional[str] = Field(None, title="Display Name", description="")
    create_uid: Optional[int] = Field(None, title="Created by", description="")
    create_date: Optional[str] = Field(None, title="Created on", description="")
    write_uid: Optional[int] = Field(None, title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, title="Last Updated on", description="")

