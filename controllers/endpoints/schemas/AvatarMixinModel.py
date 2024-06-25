
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class AvatarMixinModel(BaseModel):

    image_1920: Optional[Any] = Field(None, title="Image", description="")
    image_1024: Optional[Any] = Field(None, title="Image 1024", description="")
    image_512: Optional[Any] = Field(None, title="Image 512", description="")
    image_256: Optional[Any] = Field(None, title="Image 256", description="")
    image_128: Optional[Any] = Field(None, title="Image 128", description="")
    avatar_1920: Optional[Any] = Field(None, title="Avatar", description="")
    avatar_1024: Optional[Any] = Field(None, title="Avatar 1024", description="")
    avatar_512: Optional[Any] = Field(None, title="Avatar 512", description="")
    avatar_256: Optional[Any] = Field(None, title="Avatar 256", description="")
    avatar_128: Optional[Any] = Field(None, title="Avatar 128", description="")

