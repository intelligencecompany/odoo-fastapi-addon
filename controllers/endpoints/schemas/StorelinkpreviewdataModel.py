
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class StorelinkpreviewdataModel(BaseModel):
    id: Optional[int] = Field(None, alias="id", title="ID", description="")
    source_url: str = Field("", alias="source_url", title="URL", description="")
    message_id: int = Field(0, alias="message_id", title="Message", description="")
    og_type: Optional[str] = Field(None, alias="og_type", title="Type", description="")
    og_title: Optional[str] = Field(None, alias="og_title", title="Title", description="")
    og_site_name: Optional[str] = Field(None, alias="og_site_name", title="Site name", description="")
    og_image: Optional[str] = Field(None, alias="og_image", title="Image", description="")
    og_description: Optional[Any] = Field(None, alias="og_description", title="Description", description="")
    og_mimetype: Optional[str] = Field(None, alias="og_mimetype", title="MIME type", description="")
    image_mimetype: Optional[str] = Field(None, alias="image_mimetype", title="Image MIME type", description="")
    create_date: Optional[str] = Field(None, alias="create_date", title="Create Date", description="")
    display_name: Optional[str] = Field(None, alias="display_name", title="Display Name", description="")
    create_uid: Optional[int] = Field(None, alias="create_uid", title="Created by", description="")
    write_uid: Optional[int] = Field(None, alias="write_uid", title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, alias="write_date", title="Last Updated on", description="")

    class Config:
        from_attributes = True

    @classmethod
    def from_execute_kw(cls, data:List[dict], fields:List[str] = []) -> List['StorelinkpreviewdataModel']:
        transformed = []
        schema = StorelinkpreviewdataModel.model_json_schema()
        
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

            transformed.append(cls(**filtered_item))
        return transformed