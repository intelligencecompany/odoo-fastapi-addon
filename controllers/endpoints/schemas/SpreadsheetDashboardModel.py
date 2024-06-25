
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class SpreadsheetDashboardModel(BaseModel):
    id: Optional[int] = Field(None, title="ID", description="")
    spreadsheet_binary_data: Any = Field(None, title="Spreadsheet file", description="")
    name: str = Field("", title="Name", description="")
    dashboard_group_id: int = Field(0, title="Dashboard Group", description="")
    group_ids: Optional[List[int]] = Field(None, title="Group", description="")
    spreadsheet_data: Optional[Any] = Field(None, title="Spreadsheet Data", description="")
    thumbnail: Optional[Any] = Field(None, title="Thumbnail", description="")
    sequence: Optional[int] = Field(None, title="Sequence", description="")
    display_name: Optional[str] = Field(None, title="Display Name", description="")
    create_uid: Optional[int] = Field(None, title="Created by", description="")
    create_date: Optional[str] = Field(None, title="Created on", description="")
    write_uid: Optional[int] = Field(None, title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, title="Last Updated on", description="")

