
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class CompanyPropertyModel(BaseModel):
    id: Optional[int] = Field(None, title="ID", description="")
    type: Any = Field(None, title="Type", description="")
    res_id: Optional[str] = Field(None, title="Resource", description="If not set, acts as a default value for new resources")
    company_id: Optional[int] = Field(None, title="Company", description="")
    fields_id: int = Field(0, title="Field", description="")
    name: Optional[str] = Field(None, title="Name", description="")
    value_float: Optional[Any] = Field(None, title="Value Float", description="")
    value_integer: Optional[int] = Field(None, title="Value Integer", description="")
    value_text: Optional[Any] = Field(None, title="Value Text", description="")
    value_binary: Optional[Any] = Field(None, title="Value Binary", description="")
    value_reference: Optional[str] = Field(None, title="Value Reference", description="")
    value_datetime: Optional[str] = Field(None, title="Value Datetime", description="")
    display_name: Optional[str] = Field(None, title="Display Name", description="")
    create_uid: Optional[int] = Field(None, title="Created by", description="")
    create_date: Optional[str] = Field(None, title="Created on", description="")
    write_uid: Optional[int] = Field(None, title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, title="Last Updated on", description="")

