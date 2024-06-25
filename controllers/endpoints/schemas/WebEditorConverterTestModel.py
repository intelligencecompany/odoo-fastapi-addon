
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class WebEditorConverterTestModel(BaseModel):
    id: Optional[int] = Field(None, title="ID", description="")
    char: Optional[str] = Field(None, title="Char", description="")
    integer: Optional[int] = Field(None, title="Integer", description="")
    float: Optional[Any] = Field(None, title="Float", description="")
    numeric: Optional[Any] = Field(None, title="Numeric", description="")
    many2one: Optional[int] = Field(None, title="Many2One", description="")
    binary: Optional[Any] = Field(None, title="Binary", description="")
    date: Optional[str] = Field(None, title="Date", description="")
    datetime: Optional[str] = Field(None, title="Datetime", description="")
    selection_str: Optional[Any] = Field(None, title="Lorsqu'un pancake prend l'avion à destination de Toronto et qu'il fait une escale technique à St Claude, on dit:", description="")
    html: Optional[Any] = Field(None, title="Html", description="")
    text: Optional[Any] = Field(None, title="Text", description="")
    display_name: Optional[str] = Field(None, title="Display Name", description="")
    create_uid: Optional[int] = Field(None, title="Created by", description="")
    create_date: Optional[str] = Field(None, title="Created on", description="")
    write_uid: Optional[int] = Field(None, title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, title="Last Updated on", description="")

