
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class SpreadsheetmixinModel(BaseModel):

    spreadsheet_binary_data: Any = Field(None, title="Spreadsheet file", description="")
    spreadsheet_data: Optional[Any] = Field(None, title="Spreadsheet Data", description="")
    thumbnail: Optional[Any] = Field(None, title="Thumbnail", description="")

