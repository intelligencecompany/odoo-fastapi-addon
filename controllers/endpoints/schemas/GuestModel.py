
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class GuestModel(BaseModel):
    id: Optional[int] = Field(None, alias="id", title="ID", description="")
    name: str = Field("", alias="name", title="Name", description="")
    access_token: str = Field("", alias="access_token", title="Access Token", description="")
    country_id: Optional[int] = Field(None, alias="country_id", title="Country", description="")
    channel_ids: Optional[List[int]] = Field(None, alias="channel_ids", title="Channels", description="")
    image_1920: Optional[Any] = Field(None, alias="image_1920", title="Image", description="")
    image_1024: Optional[Any] = Field(None, alias="image_1024", title="Image 1024", description="")
    image_512: Optional[Any] = Field(None, alias="image_512", title="Image 512", description="")
    image_256: Optional[Any] = Field(None, alias="image_256", title="Image 256", description="")
    image_128: Optional[Any] = Field(None, alias="image_128", title="Image 128", description="")
    avatar_1920: Optional[Any] = Field(None, alias="avatar_1920", title="Avatar", description="")
    avatar_1024: Optional[Any] = Field(None, alias="avatar_1024", title="Avatar 1024", description="")
    avatar_512: Optional[Any] = Field(None, alias="avatar_512", title="Avatar 512", description="")
    avatar_256: Optional[Any] = Field(None, alias="avatar_256", title="Avatar 256", description="")
    avatar_128: Optional[Any] = Field(None, alias="avatar_128", title="Avatar 128", description="")
    lang: Optional[Any] = Field(None, alias="lang", title="Language", description="")
    timezone: Optional[Any] = Field(None, alias="timezone", title="Timezone", description="")
    im_status: Optional[str] = Field(None, alias="im_status", title="IM Status", description="")
    display_name: Optional[str] = Field(None, alias="display_name", title="Display Name", description="")
    create_uid: Optional[int] = Field(None, alias="create_uid", title="Created by", description="")
    create_date: Optional[str] = Field(None, alias="create_date", title="Created on", description="")
    write_uid: Optional[int] = Field(None, alias="write_uid", title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, alias="write_date", title="Last Updated on", description="")

    class ConfigDict:
        from_attributes = True

    @classmethod
    def from_execute_kw(cls, item:dict[str, any]) -> 'GuestModel':
        filtered_item = {}
        schema = GuestModel.model_json_schema()

        for key in item:
            value = item[key]
            model_type = 'any'

            if 'anyOf' in schema['properties'][key] and 'type' in schema['properties'][key]['anyOf'][0]:
                model_type = schema['properties'][key]['anyOf'][0]['type']
            elif 'type' in schema['properties'][key]:
                model_type = schema['properties'][key]['type']

            if isinstance(value, list) and model_type != 'array':
                value = value[0] if item[key] else None
            
            if isinstance(value, bool) and model_type == 'string':
                value = ''

            if value is not None:
                filtered_item[key] = value

        return cls(**filtered_item).model_dump(by_alias=True)

    @classmethod
    def list_from_execute_kw(cls, data:List[dict], fields:List[str] = []) -> List['GuestModel']:
        transformed = []
        schema = GuestModel.model_json_schema()
        
        for item in data:
            filtered_item = {}

            if len(fields) == 0:
                fields = item.keys()

            for key in fields:
                if key in item:
                    value = item[key]
                    model_type = 'any'

                    if 'anyOf' in schema['properties'][key] and 'type' in schema['properties'][key]['anyOf'][0]:
                        model_type = schema['properties'][key]['anyOf'][0]['type']
                    elif 'type' in schema['properties'][key]:
                        model_type = schema['properties'][key]['type']

                    if isinstance(value, list) and model_type != 'array':
                        value = value[0] if item[key] else None
                    
                    if isinstance(value, bool) and model_type == 'string':
                        value = ''

                    if value is not None:
                        filtered_item[key] = value

            transformed.append(cls(**filtered_item).model_dump(by_alias=True))
        return transformed
