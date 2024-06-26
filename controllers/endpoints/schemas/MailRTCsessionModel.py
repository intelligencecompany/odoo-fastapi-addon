
from pydantic import BaseModel, Field
from typing import Optional, List, Any, Dict

class MailRTCsessionModel(BaseModel):
    id: Optional[int] = Field(None, alias="id", title="ID", description="")
    channel_member_id: int = Field(0, alias="channel_member_id", title="Channel Member", description="")
    channel_id: Optional[int] = Field(None, alias="channel_id", title="Channel", description="")
    partner_id: Optional[int] = Field(None, alias="partner_id", title="Partner", description="")
    guest_id: Optional[int] = Field(None, alias="guest_id", title="Guest", description="")
    write_date: Optional[str] = Field(None, alias="write_date", title="Last Updated On", description="")
    is_screen_sharing_on: Optional[bool] = Field(None, alias="is_screen_sharing_on", title="Is sharing the screen", description="")
    is_camera_on: Optional[bool] = Field(None, alias="is_camera_on", title="Is sending user video", description="")
    is_muted: Optional[bool] = Field(None, alias="is_muted", title="Is microphone muted", description="")
    is_deaf: Optional[bool] = Field(None, alias="is_deaf", title="Has disabled incoming sound", description="")
    display_name: Optional[str] = Field(None, alias="display_name", title="Display Name", description="")
    create_uid: Optional[int] = Field(None, alias="create_uid", title="Created by", description="")
    create_date: Optional[str] = Field(None, alias="create_date", title="Created on", description="")
    write_uid: Optional[int] = Field(None, alias="write_uid", title="Last Updated by", description="")

    class ConfigDict:
        from_attributes = True

    @classmethod
    def from_execute_kw(cls, item:Dict[str, Any]) -> 'MailRTCsessionModel':
        filtered_item = {}
        schema = MailRTCsessionModel.model_json_schema()

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
    def list_from_execute_kw(cls, data:List[dict], fields:List[str] = []) -> List['MailRTCsessionModel']:
        transformed = []
        schema = MailRTCsessionModel.model_json_schema()
        
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
