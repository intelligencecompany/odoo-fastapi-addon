
from pydantic import BaseModel, Field
from typing import Optional, List, Any, Dict

class LivechatSupportOperatorReportModel(BaseModel):
    id: Optional[int] = Field(None, alias="id", title="ID", description="")
    partner_id: Optional[int] = Field(None, alias="partner_id", title="Operator", description="")
    livechat_channel_id: Optional[int] = Field(None, alias="livechat_channel_id", title="Channel", description="")
    channel_id: Optional[int] = Field(None, alias="channel_id", title="Conversation", description="")
    nbr_channel: Optional[int] = Field(None, alias="nbr_channel", title="# of Sessions", description="")
    start_date: Optional[str] = Field(None, alias="start_date", title="Start Date of session", description="")
    time_to_answer: Optional[Any] = Field(None, alias="time_to_answer", title="Time to answer", description="Average time to give the first answer to the visitor")
    duration: Optional[Any] = Field(None, alias="duration", title="Average duration", description="Duration of the conversation (in seconds)")
    rating: Optional[Any] = Field(None, alias="rating", title="Average rating", description="Average rating given by the visitor")
    display_name: Optional[str] = Field(None, alias="display_name", title="Display Name", description="")

    class ConfigDict:
        from_attributes = True

    @classmethod
    def from_execute_kw(cls, item:Dict[str, Any]) -> 'LivechatSupportOperatorReportModel':
        filtered_item = {}
        schema = LivechatSupportOperatorReportModel.model_json_schema()

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
    def list_from_execute_kw(cls, data:List[dict], fields:List[str] = []) -> List['LivechatSupportOperatorReportModel']:
        transformed = []
        schema = LivechatSupportOperatorReportModel.model_json_schema()
        
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
