
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class WebsiteVisitorModel(BaseModel):
    id: Optional[int] = Field(None, alias="id", title="ID", description="")
    access_token: str = Field("", alias="access_token", title="Access Token", description="")
    website_id: Optional[int] = Field(None, alias="website_id", title="Website", description="")
    partner_id: Optional[int] = Field(None, alias="partner_id", title="Contact", description="Partner of the last logged in user.")
    country_id: Optional[int] = Field(None, alias="country_id", title="Country", description="")
    lang_id: Optional[int] = Field(None, alias="lang_id", title="Language", description="Language from the website when visitor has been created")
    last_visited_page_id: Optional[int] = Field(None, alias="last_visited_page_id", title="Last Visited Page", description="")
    livechat_operator_id: Optional[int] = Field(None, alias="livechat_operator_id", title="Speaking with", description="")
    website_track_ids: Optional[List[int]] = Field(None, alias="website_track_ids", title="Visited Pages History", description="")
    page_ids: Optional[List[int]] = Field(None, alias="page_ids", title="Visited Pages", description="")
    discuss_channel_ids: Optional[List[int]] = Field(None, alias="discuss_channel_ids", title="Visitor's livechat channels", description="")
    name: Optional[str] = Field(None, alias="name", title="Name", description="")
    partner_image: Optional[Any] = Field(None, alias="partner_image", title="Image", description="")
    country_flag: Optional[str] = Field(None, alias="country_flag", title="Country Flag", description="Url of static flag image")
    timezone: Optional[Any] = Field(None, alias="timezone", title="Timezone", description="")
    email: Optional[str] = Field(None, alias="email", title="Email", description="")
    mobile: Optional[str] = Field(None, alias="mobile", title="Mobile", description="")
    visit_count: Optional[int] = Field(None, alias="visit_count", title="# Visits", description="A new visit is considered if last connection was more than 8 hours ago.")
    visitor_page_count: Optional[int] = Field(None, alias="visitor_page_count", title="Page Views", description="Total number of visits on tracked pages")
    page_count: Optional[int] = Field(None, alias="page_count", title="# Visited Pages", description="Total number of tracked page visited")
    create_date: Optional[str] = Field(None, alias="create_date", title="First Connection", description="")
    last_connection_datetime: Optional[str] = Field(None, alias="last_connection_datetime", title="Last Connection", description="Last page view date")
    time_since_last_action: Optional[str] = Field(None, alias="time_since_last_action", title="Last action", description="Time since last page view. E.g.: 2 minutes ago")
    is_connected: Optional[bool] = Field(None, alias="is_connected", title="Is connected?", description="A visitor is considered as connected if his last page view was within the last 5 minutes.")
    display_name: Optional[str] = Field(None, alias="display_name", title="Display Name", description="")
    create_uid: Optional[int] = Field(None, alias="create_uid", title="Created by", description="")
    write_uid: Optional[int] = Field(None, alias="write_uid", title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, alias="write_date", title="Last Updated on", description="")
    livechat_operator_name: Optional[str] = Field(None, alias="livechat_operator_name", title="Operator Name", description="")
    session_count: Optional[int] = Field(None, alias="session_count", title="# Sessions", description="")

    class ConfigDict:
        from_attributes = True

    @classmethod
    def from_execute_kw(cls, item:dict[str, any]) -> 'WebsiteVisitorModel':
        filtered_item = {}
        schema = WebsiteVisitorModel.model_json_schema()

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
    def list_from_execute_kw(cls, data:List[dict], fields:List[str] = []) -> List['WebsiteVisitorModel']:
        transformed = []
        schema = WebsiteVisitorModel.model_json_schema()
        
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
