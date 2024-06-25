
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class ImageMixinModel(BaseModel):

    image_1920: Optional[Any] = Field(None, title="Image", description="")
    image_1024: Optional[Any] = Field(None, title="Image 1024", description="")
    image_512: Optional[Any] = Field(None, title="Image 512", description="")
    image_256: Optional[Any] = Field(None, title="Image 256", description="")
    image_128: Optional[Any] = Field(None, title="Image 128", description="")

