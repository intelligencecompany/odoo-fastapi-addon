
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class AnalyticPlansApplicabilitiesModel(BaseModel):
    id: Optional[int] = Field(None, title="ID", description="")
    business_domain: Any = Field(None, title="Domain", description="")
    applicability: Any = Field(None, title="Applicability", description="")
    analytic_plan_id: Optional[int] = Field(None, title="Analytic Plan", description="")
    company_id: Optional[int] = Field(None, title="Company", description="")
    display_name: Optional[str] = Field(None, title="Display Name", description="")
    create_uid: Optional[int] = Field(None, title="Created by", description="")
    create_date: Optional[str] = Field(None, title="Created on", description="")
    write_uid: Optional[int] = Field(None, title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, title="Last Updated on", description="")

