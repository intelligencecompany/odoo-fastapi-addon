
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class UTMCampaignModel(BaseModel):
    id: Optional[int] = Field(None, alias="id", title="ID", description="")
    name: str = Field("", alias="name", title="Campaign Identifier", description="")
    title: str = Field("", alias="title", title="Campaign Name", description="")
    user_id: int = Field(0, alias="user_id", title="Responsible", description="")
    stage_id: int = Field(0, alias="stage_id", title="Stage", description="")
    tag_ids: Optional[List[int]] = Field(None, alias="tag_ids", title="Tags", description="")
    active: Optional[bool] = Field(None, alias="active", title="Active", description="")
    is_auto_campaign: Optional[bool] = Field(None, alias="is_auto_campaign", title="Automatically Generated Campaign", description="Allows us to filter relevant Campaigns")
    color: Optional[int] = Field(None, alias="color", title="Color Index", description="")
    display_name: Optional[str] = Field(None, alias="display_name", title="Display Name", description="")
    create_uid: Optional[int] = Field(None, alias="create_uid", title="Created by", description="")
    create_date: Optional[str] = Field(None, alias="create_date", title="Created on", description="")
    write_uid: Optional[int] = Field(None, alias="write_uid", title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, alias="write_date", title="Last Updated on", description="")

    class Config:
        from_attributes = True

    @classmethod
    def from_execute_kw(cls, data:List[dict], fields:List[str] = []) -> List['UTMCampaignModel']:
        transformed = []
        schema = UTMCampaignModel.model_json_schema()
        
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
