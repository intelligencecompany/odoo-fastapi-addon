
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class GuestModel(BaseModel):
    id: Optional[int] = Field(None, title="ID", description="")
    name: str = Field("", title="Name", description="")
    access_token: str = Field("", title="Access Token", description="")
    country_id: Optional[int] = Field(None, title="Country", description="")
    channel_ids: Optional[List[int]] = Field(None, title="Channels", description="")
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
    lang: Optional[Any] = Field(None, title="Language", description="")
    timezone: Optional[Any] = Field(None, title="Timezone", description="")
    im_status: Optional[str] = Field(None, title="IM Status", description="")
    display_name: Optional[str] = Field(None, title="Display Name", description="")
    create_uid: Optional[int] = Field(None, title="Created by", description="")
    create_date: Optional[str] = Field(None, title="Created on", description="")
    write_uid: Optional[int] = Field(None, title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, title="Last Updated on", description="")

