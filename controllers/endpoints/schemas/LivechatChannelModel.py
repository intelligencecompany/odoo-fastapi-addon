
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class LivechatChannelModel(BaseModel):
    id: Optional[int] = Field(None, alias="id", title="ID", description="")
    name: str = Field("", alias="name", title="Channel Name", description="")
    rating_ids: Optional[List[int]] = Field(None, alias="rating_ids", title="Ratings", description="")
    available_operator_ids: Optional[List[int]] = Field(None, alias="available_operator_ids", title="Available Operator", description="")
    user_ids: Optional[List[int]] = Field(None, alias="user_ids", title="Operators", description="")
    channel_ids: Optional[List[int]] = Field(None, alias="channel_ids", title="Sessions", description="")
    rule_ids: Optional[List[int]] = Field(None, alias="rule_ids", title="Rules", description="")
    website_published: Optional[bool] = Field(None, alias="website_published", title="Visible on current website", description="")
    is_published: Optional[bool] = Field(None, alias="is_published", title="Is Published", description="")
    can_publish: Optional[bool] = Field(None, alias="can_publish", title="Can Publish", description="")
    website_url: Optional[str] = Field(None, alias="website_url", title="Website URL", description="The full URL to access the document through the website.")
    rating_percentage_satisfaction: Optional[int] = Field(None, alias="rating_percentage_satisfaction", title="Rating Satisfaction", description="Percentage of happy ratings")
    rating_count: Optional[int] = Field(None, alias="rating_count", title="# Ratings", description="")
    rating_avg: Optional[Any] = Field(None, alias="rating_avg", title="Average Rating", description="")
    rating_avg_percentage: Optional[Any] = Field(None, alias="rating_avg_percentage", title="Average Rating (%)", description="")
    button_text: Optional[str] = Field(None, alias="button_text", title="Text of the Button", description="Default text displayed on the Livechat Support Button")
    default_message: Optional[str] = Field(None, alias="default_message", title="Welcome Message", description="This is an automated 'welcome' message that your visitor will see when they initiate a new conversation.")
    input_placeholder: Optional[str] = Field(None, alias="input_placeholder", title="Chat Input Placeholder", description="Text that prompts the user to initiate the chat.")
    header_background_color: Optional[str] = Field(None, alias="header_background_color", title="Header Background Color", description="Default background color of the channel header once open")
    title_color: Optional[str] = Field(None, alias="title_color", title="Title Color", description="Default title color of the channel once open")
    button_background_color: Optional[str] = Field(None, alias="button_background_color", title="Button Background Color", description="Default background color of the Livechat button")
    button_text_color: Optional[str] = Field(None, alias="button_text_color", title="Button Text Color", description="Default text color of the Livechat button")
    web_page: Optional[str] = Field(None, alias="web_page", title="Web Page", description="URL to a static page where you client can discuss with the operator of the channel.")
    are_you_inside: Optional[bool] = Field(None, alias="are_you_inside", title="Are you inside the matrix?", description="")
    script_external: Optional[Any] = Field(None, alias="script_external", title="Script (external)", description="")
    nbr_channel: Optional[int] = Field(None, alias="nbr_channel", title="Number of conversation", description="")
    image_128: Optional[Any] = Field(None, alias="image_128", title="Image", description="")
    chatbot_script_count: Optional[int] = Field(None, alias="chatbot_script_count", title="Number of Chatbot", description="")
    display_name: Optional[str] = Field(None, alias="display_name", title="Display Name", description="")
    create_uid: Optional[int] = Field(None, alias="create_uid", title="Created by", description="")
    create_date: Optional[str] = Field(None, alias="create_date", title="Created on", description="")
    write_uid: Optional[int] = Field(None, alias="write_uid", title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, alias="write_date", title="Last Updated on", description="")
    website_description: Optional[Any] = Field(None, alias="website_description", title="Website description", description="Description of the channel displayed on the website page")

    class Config:
        from_attributes = True

    @classmethod
    def from_execute_kw(cls, data:List[dict], fields:List[str] = []) -> List['LivechatChannelModel']:
        transformed = []
        schema = LivechatChannelModel.model_json_schema()
        
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
