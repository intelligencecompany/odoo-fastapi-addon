
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class DefaultValuesModel(BaseModel):
    id: Optional[int] = Field(None, title="ID", description="")
    json_value: str = Field("", title="Default Value (JSON format)", description="")
    field_id: int = Field(0, title="Field", description="")
    user_id: Optional[int] = Field(None, title="User", description="If set, action binding only applies for this user.")
    company_id: Optional[int] = Field(None, title="Company", description="If set, action binding only applies for this company")
    condition: Optional[str] = Field(None, title="Condition", description="If set, applies the default upon condition.")
    display_name: Optional[str] = Field(None, title="Display Name", description="")
    create_uid: Optional[int] = Field(None, title="Created by", description="")
    create_date: Optional[str] = Field(None, title="Created on", description="")
    write_uid: Optional[int] = Field(None, title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, title="Last Updated on", description="")

