
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class LivechatSupportChannelReportModel(BaseModel):
    id: Optional[int] = Field(None, alias="id", title="ID", description="")
    channel_id: Optional[int] = Field(None, alias="channel_id", title="Conversation", description="")
    livechat_channel_id: Optional[int] = Field(None, alias="livechat_channel_id", title="Channel", description="")
    country_id: Optional[int] = Field(None, alias="country_id", title="Country of the visitor", description="")
    partner_id: Optional[int] = Field(None, alias="partner_id", title="Operator", description="")
    uuid: Optional[str] = Field(None, alias="uuid", title="UUID", description="")
    channel_name: Optional[str] = Field(None, alias="channel_name", title="Channel Name", description="")
    technical_name: Optional[str] = Field(None, alias="technical_name", title="Code", description="")
    start_date: Optional[str] = Field(None, alias="start_date", title="Start Date of session", description="")
    start_hour: Optional[str] = Field(None, alias="start_hour", title="Start Hour of session", description="")
    day_number: Optional[str] = Field(None, alias="day_number", title="Day Number", description="1 is Monday, 7 is Sunday")
    time_to_answer: Optional[Any] = Field(None, alias="time_to_answer", title="Time to answer (sec)", description="Average time in seconds to give the first answer to the visitor")
    start_date_hour: Optional[str] = Field(None, alias="start_date_hour", title="Hour of start Date of session", description="")
    duration: Optional[Any] = Field(None, alias="duration", title="Average duration", description="Duration of the conversation (in seconds)")
    nbr_speaker: Optional[int] = Field(None, alias="nbr_speaker", title="# of speakers", description="Number of different speakers")
    nbr_message: Optional[int] = Field(None, alias="nbr_message", title="Average message", description="Number of message in the conversation")
    is_without_answer: Optional[int] = Field(None, alias="is_without_answer", title="Session(s) without answer", description="A session is without answer if the operator did not answer. \n                                       If the visitor is also the operator, the session will always be answered.")
    days_of_activity: Optional[int] = Field(None, alias="days_of_activity", title="Days of activity", description="Number of days since the first session of the operator")
    is_anonymous: Optional[int] = Field(None, alias="is_anonymous", title="Is visitor anonymous", description="")
    is_happy: Optional[int] = Field(None, alias="is_happy", title="Visitor is Happy", description="")
    rating: Optional[int] = Field(None, alias="rating", title="Rating", description="")
    rating_text: Optional[str] = Field(None, alias="rating_text", title="Satisfaction Rate", description="")
    is_unrated: Optional[int] = Field(None, alias="is_unrated", title="Session not rated", description="")
    display_name: Optional[str] = Field(None, alias="display_name", title="Display Name", description="")

    class ConfigDict:
        from_attributes = True

    @classmethod
    def from_execute_kw(cls, item:dict[str, any]) -> 'LivechatSupportChannelReportModel':
        filtered_item = {}
        schema = LivechatSupportChannelReportModel.model_json_schema()

        for key, value in item.items():
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
    def list_from_execute_kw(cls, data:List[dict], fields:List[str] = []) -> List['LivechatSupportChannelReportModel']:
        transformed = []
        schema = LivechatSupportChannelReportModel.model_json_schema()
        
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
