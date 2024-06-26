
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class PortalSharingModel(BaseModel):
    id: Optional[int] = Field(None, alias="id", title="ID", description="")
    res_model: str = Field("", alias="res_model", title="Related Document Model", description="")
    res_id: int = Field(0, alias="res_id", title="Related Document ID", description="")
    partner_ids: List[int] = Field([], alias="partner_ids", title="Recipients", description="")
    resource_ref: Optional[Any] = Field(None, alias="resource_ref", title="Related Document", description="")
    note: Optional[Any] = Field(None, alias="note", title="Note", description="Add extra content to display in the email")
    share_link: Optional[str] = Field(None, alias="share_link", title="Link", description="")
    access_warning: Optional[Any] = Field(None, alias="access_warning", title="Access warning", description="")
    display_name: Optional[str] = Field(None, alias="display_name", title="Display Name", description="")
    create_uid: Optional[int] = Field(None, alias="create_uid", title="Created by", description="")
    create_date: Optional[str] = Field(None, alias="create_date", title="Created on", description="")
    write_uid: Optional[int] = Field(None, alias="write_uid", title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, alias="write_date", title="Last Updated on", description="")

    class ConfigDict:
        from_attributes = True

    @classmethod
    def from_execute_kw(cls, data:List[dict], fields:List[str] = []) -> List['PortalSharingModel']:
        transformed = []
        schema = PortalSharingModel.model_json_schema()
        
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
