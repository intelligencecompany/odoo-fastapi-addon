
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class DigestModel(BaseModel):
    id: Optional[int] = Field(None, alias="id", title="ID", description="")
    name: str = Field("", alias="name", title="Name", description="")
    periodicity: Any = Field(None, alias="periodicity", title="Periodicity", description="")
    currency_id: Optional[int] = Field(None, alias="currency_id", title="Currency", description="")
    company_id: Optional[int] = Field(None, alias="company_id", title="Company", description="")
    user_ids: Optional[List[int]] = Field(None, alias="user_ids", title="Recipients", description="")
    next_run_date: Optional[str] = Field(None, alias="next_run_date", title="Next Mailing Date", description="")
    available_fields: Optional[str] = Field(None, alias="available_fields", title="Available Fields", description="")
    is_subscribed: Optional[bool] = Field(None, alias="is_subscribed", title="Is user subscribed", description="")
    state: Optional[Any] = Field(None, alias="state", title="Status", description="")
    kpi_res_users_connected: Optional[bool] = Field(None, alias="kpi_res_users_connected", title="Connected Users", description="")
    kpi_res_users_connected_value: Optional[int] = Field(None, alias="kpi_res_users_connected_value", title="Kpi Res Users Connected Value", description="")
    kpi_mail_message_total: Optional[bool] = Field(None, alias="kpi_mail_message_total", title="Messages Sent", description="")
    kpi_mail_message_total_value: Optional[int] = Field(None, alias="kpi_mail_message_total_value", title="Kpi Mail Message Total Value", description="")
    display_name: Optional[str] = Field(None, alias="display_name", title="Display Name", description="")
    create_uid: Optional[int] = Field(None, alias="create_uid", title="Created by", description="")
    create_date: Optional[str] = Field(None, alias="create_date", title="Created on", description="")
    write_uid: Optional[int] = Field(None, alias="write_uid", title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, alias="write_date", title="Last Updated on", description="")
    kpi_livechat_rating: Optional[bool] = Field(None, alias="kpi_livechat_rating", title="% of Happiness", description="")
    kpi_livechat_rating_value: Optional[Any] = Field(None, alias="kpi_livechat_rating_value", title="Kpi Livechat Rating Value", description="")
    kpi_livechat_conversations: Optional[bool] = Field(None, alias="kpi_livechat_conversations", title="Conversations handled", description="")
    kpi_livechat_conversations_value: Optional[int] = Field(None, alias="kpi_livechat_conversations_value", title="Kpi Livechat Conversations Value", description="")
    kpi_livechat_response: Optional[bool] = Field(None, alias="kpi_livechat_response", title="Time to answer (sec)", description="")
    kpi_livechat_response_value: Optional[Any] = Field(None, alias="kpi_livechat_response_value", title="Kpi Livechat Response Value", description="")

    class ConfigDict:
        from_attributes = True

    @classmethod
    def from_execute_kw(cls, item:dict) -> 'DigestModel':
        filtered_item = {}
        schema = DigestModel.model_json_schema()

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
    def list_from_execute_kw(cls, data:List[dict], fields:List[str] = []) -> List['DigestModel']:
        transformed = []
        schema = DigestModel.model_json_schema()
        
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
