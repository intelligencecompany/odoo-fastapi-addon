
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class BlogTagModel(BaseModel):
    id: Optional[int] = Field(None, title="ID", description="")
    name: str = Field("", title="Name", description="")
    category_id: Optional[int] = Field(None, title="Category", description="")
    post_ids: Optional[List[int]] = Field(None, title="Posts", description="")
    is_seo_optimized: Optional[bool] = Field(None, title="SEO optimized", description="")
    website_meta_title: Optional[str] = Field(None, title="Website meta title", description="")
    website_meta_description: Optional[Any] = Field(None, title="Website meta description", description="")
    website_meta_keywords: Optional[str] = Field(None, title="Website meta keywords", description="")
    website_meta_og_img: Optional[str] = Field(None, title="Website opengraph image", description="")
    seo_name: Optional[str] = Field(None, title="Seo name", description="")
    display_name: Optional[str] = Field(None, title="Display Name", description="")
    create_uid: Optional[int] = Field(None, title="Created by", description="")
    create_date: Optional[str] = Field(None, title="Created on", description="")
    write_uid: Optional[int] = Field(None, title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, title="Last Updated on", description="")

