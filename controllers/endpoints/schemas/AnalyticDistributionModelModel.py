
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class AnalyticDistributionModelModel(BaseModel):
    id: Optional[int] = Field(None, title="ID", description="")
    partner_id: Optional[int] = Field(None, title="Partner", description="Select a partner for which the analytic distribution will be used (e.g. create new customer invoice or Sales order if we select this partner, it will automatically take this as an analytic account)")
    partner_category_id: Optional[int] = Field(None, title="Partner Category", description="Select a partner category for which the analytic distribution will be used (e.g. create new customer invoice or Sales order if we select this partner, it will automatically take this as an analytic account)")
    company_id: Optional[int] = Field(None, title="Company", description="Select a company for which the analytic distribution will be used (e.g. create new customer invoice or Sales order if we select this company, it will automatically take this as an analytic account)")
    analytic_distribution: Optional[Any] = Field(None, title="Analytic Distribution", description="")
    analytic_distribution_search: Optional[Any] = Field(None, title="Analytic Distribution Search", description="")
    analytic_precision: Optional[int] = Field(None, title="Analytic Precision", description="")
    display_name: Optional[str] = Field(None, title="Display Name", description="")
    create_uid: Optional[int] = Field(None, title="Created by", description="")
    create_date: Optional[str] = Field(None, title="Created on", description="")
    write_uid: Optional[int] = Field(None, title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, title="Last Updated on", description="")

