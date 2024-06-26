
from pydantic import BaseModel, Field
from typing import Optional, List, Any, Dict

class ProductDocumentModel(BaseModel):
    id: Optional[int] = Field(None, alias="id", title="ID", description="")
    name: str = Field("", alias="name", title="Name", description="")
    type: Any = Field(None, alias="type", title="Type", description="You can either upload a file from your computer or copy/paste an internet link to your file.")
    ir_attachment_id: int = Field(0, alias="ir_attachment_id", title="Related attachment", description="")
    res_id: Optional[Any] = Field(None, alias="res_id", title="Resource ID", description="")
    company_id: Optional[int] = Field(None, alias="company_id", title="Company", description="")
    original_id: Optional[int] = Field(None, alias="original_id", title="Original (unoptimized, unresized) attachment", description="")
    website_id: Optional[int] = Field(None, alias="website_id", title="Website", description="")
    theme_template_id: Optional[int] = Field(None, alias="theme_template_id", title="Theme Template", description="")
    voice_ids: Optional[List[int]] = Field(None, alias="voice_ids", title="Voice", description="")
    active: Optional[bool] = Field(None, alias="active", title="Active", description="")
    display_name: Optional[str] = Field(None, alias="display_name", title="Display Name", description="")
    create_uid: Optional[int] = Field(None, alias="create_uid", title="Created by", description="")
    create_date: Optional[str] = Field(None, alias="create_date", title="Created on", description="")
    write_uid: Optional[int] = Field(None, alias="write_uid", title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, alias="write_date", title="Last Updated on", description="")
    description: Optional[Any] = Field(None, alias="description", title="Description", description="")
    res_name: Optional[str] = Field(None, alias="res_name", title="Resource Name", description="")
    res_model: Optional[str] = Field(None, alias="res_model", title="Resource Model", description="")
    res_field: Optional[str] = Field(None, alias="res_field", title="Resource Field", description="")
    url: Optional[str] = Field(None, alias="url", title="Url", description="")
    public: Optional[bool] = Field(None, alias="public", title="Is public document", description="")
    access_token: Optional[str] = Field(None, alias="access_token", title="Access Token", description="")
    raw: Optional[Any] = Field(None, alias="raw", title="File Content (raw)", description="")
    datas: Optional[Any] = Field(None, alias="datas", title="File Content (base64)", description="")
    db_datas: Optional[Any] = Field(None, alias="db_datas", title="Database Data", description="")
    store_fname: Optional[str] = Field(None, alias="store_fname", title="Stored Filename", description="")
    file_size: Optional[int] = Field(None, alias="file_size", title="File Size", description="")
    checksum: Optional[str] = Field(None, alias="checksum", title="Checksum/SHA1", description="")
    mimetype: Optional[str] = Field(None, alias="mimetype", title="Mime Type", description="")
    index_content: Optional[Any] = Field(None, alias="index_content", title="Indexed Content", description="")
    local_url: Optional[str] = Field(None, alias="local_url", title="Attachment URL", description="")
    image_src: Optional[str] = Field(None, alias="image_src", title="Image Src", description="")
    image_width: Optional[int] = Field(None, alias="image_width", title="Image Width", description="")
    image_height: Optional[int] = Field(None, alias="image_height", title="Image Height", description="")
    key: Optional[str] = Field(None, alias="key", title="Key", description="")

    class ConfigDict:
        from_attributes = True

    @classmethod
    def from_execute_kw(cls, item:dict) -> 'ProductDocumentModel':
        filtered_item = {}
        schema = ProductDocumentModel.model_json_schema()

        for key in item.keys():
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
    def list_from_execute_kw(cls, data:List[dict], fields:List[str] = []) -> List['ProductDocumentModel']:
        transformed = []
        schema = ProductDocumentModel.model_json_schema()
        
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
