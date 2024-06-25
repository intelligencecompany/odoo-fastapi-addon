
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class SEOmetadataModel(BaseModel):

    is_seo_optimized: Optional[bool] = Field(None, title="SEO optimized", description="")
    website_meta_title: Optional[str] = Field(None, title="Website meta title", description="")
    website_meta_description: Optional[Any] = Field(None, title="Website meta description", description="")
    website_meta_keywords: Optional[str] = Field(None, title="Website meta keywords", description="")
    website_meta_og_img: Optional[str] = Field(None, title="Website opengraph image", description="")
    seo_name: Optional[str] = Field(None, title="Seo name", description="")

