
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class AnalyticMixinModel(BaseModel):

    analytic_distribution: Optional[Any] = Field(None, title="Analytic Distribution", description="")
    analytic_distribution_search: Optional[Any] = Field(None, title="Analytic Distribution Search", description="")
    analytic_precision: Optional[int] = Field(None, title="Analytic Precision", description="")

