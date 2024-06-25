
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class CopyofashareddashboardModel(BaseModel):
    id: Optional[int] = Field(None, title="ID", description="")
    spreadsheet_binary_data: Any = Field(None, title="Spreadsheet file", description="")
    access_token: str = Field("", title="Access Token", description="")
    dashboard_id: int = Field(0, title="Dashboard", description="")
    spreadsheet_data: Optional[Any] = Field(None, title="Spreadsheet Data", description="")
    thumbnail: Optional[Any] = Field(None, title="Thumbnail", description="")
    excel_export: Optional[Any] = Field(None, title="Excel Export", description="")
    full_url: Optional[str] = Field(None, title="URL", description="")
    name: Optional[str] = Field(None, title="Name", description="")
    display_name: Optional[str] = Field(None, title="Display Name", description="")
    create_uid: Optional[int] = Field(None, title="Created by", description="")
    create_date: Optional[str] = Field(None, title="Created on", description="")
    write_uid: Optional[int] = Field(None, title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, title="Last Updated on", description="")

