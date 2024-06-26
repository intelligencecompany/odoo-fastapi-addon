
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class SMSTemplatesModel(BaseModel):
    id: Optional[int] = Field(None, alias="id", title="ID", description="")
    body: str = Field("", alias="body", title="Body", description="")
    x_model_id: int = Field(0, alias="x_model_id", title="Applies to", description="The type of document this template can be used with")
    sidebar_action_id: Optional[int] = Field(None, alias="sidebar_action_id", title="Sidebar action", description="Sidebar action to make this template available on records of the related document model")
    template_fs: Optional[str] = Field(None, alias="template_fs", title="Template Filename", description="File from where the template originates. Used to reset broken template.")
    lang: Optional[str] = Field(None, alias="lang", title="Language", description="Optional translation language (ISO code) to select when sending out an email. If not set, the english version will be used. This should usually be a placeholder expression that provides the appropriate language, e.g. {{ object.partner_id.lang }}.")
    render_model: Optional[str] = Field(None, alias="render_model", title="Rendering Model", description="")
    name: Optional[str] = Field(None, alias="name", title="Name", description="")
    model: Optional[str] = Field(None, alias="model", title="Related Document Model", description="")
    display_name: Optional[str] = Field(None, alias="display_name", title="Display Name", description="")
    create_uid: Optional[int] = Field(None, alias="create_uid", title="Created by", description="")
    create_date: Optional[str] = Field(None, alias="create_date", title="Created on", description="")
    write_uid: Optional[int] = Field(None, alias="write_uid", title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, alias="write_date", title="Last Updated on", description="")

    class ConfigDict:
        from_attributes = True

    @classmethod
    def from_execute_kw(cls, data:List[dict], fields:List[str] = []) -> List['SMSTemplatesModel']:
        transformed = []
        schema = SMSTemplatesModel.model_json_schema()
        
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
