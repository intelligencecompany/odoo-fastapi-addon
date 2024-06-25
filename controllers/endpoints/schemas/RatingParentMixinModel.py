
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class RatingParentMixinModel(BaseModel):

    rating_ids: Optional[List[int]] = Field(None, title="Ratings", description="")
    rating_percentage_satisfaction: Optional[int] = Field(None, title="Rating Satisfaction", description="Percentage of happy ratings")
    rating_count: Optional[int] = Field(None, title="# Ratings", description="")
    rating_avg: Optional[Any] = Field(None, title="Average Rating", description="")
    rating_avg_percentage: Optional[Any] = Field(None, title="Average Rating (%)", description="")

