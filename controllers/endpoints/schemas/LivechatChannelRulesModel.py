
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class LivechatChannelRulesModel(BaseModel):
    id: Optional[int] = Field(None, alias="id", title="ID", description="")
    action: Any = Field(None, alias="action", title="Live Chat Button", description="* 'Show' displays the chat button on the pages.\n* 'Show with notification' is 'Show' in addition to a floating text just next to the button.\n* 'Open automatically' displays the button and automatically opens the conversation pane.\n* 'Hide' hides the chat button on the pages.")
    chatbot_script_id: Optional[int] = Field(None, alias="chatbot_script_id", title="Chatbot", description="")
    channel_id: Optional[int] = Field(None, alias="channel_id", title="Channel", description="The channel of the rule")
    country_ids: Optional[List[int]] = Field(None, alias="country_ids", title="Country", description="The rule will only be applied for these countries. Example: if you select 'Belgium' and 'United States' and that you set the action to 'Hide', the chat button will be hidden on the specified URL from the visitors located in these 2 countries. This feature requires GeoIP installed on your server.")
    regex_url: Optional[str] = Field(None, alias="regex_url", title="URL Regex", description="Regular expression specifying the web pages this rule will be applied on.")
    auto_popup_timer: Optional[int] = Field(None, alias="auto_popup_timer", title="Open automatically timer", description="Delay (in seconds) to automatically open the conversation window. Note: the selected action must be 'Open automatically' otherwise this parameter will not be taken into account.")
    chatbot_only_if_no_operator: Optional[bool] = Field(None, alias="chatbot_only_if_no_operator", title="Enabled only if no operator", description="Enable the bot only if there is no operator available")
    sequence: Optional[int] = Field(None, alias="sequence", title="Matching order", description="Given the order to find a matching rule. If 2 rules are matching for the given url/country, the one with the lowest sequence will be chosen.")
    display_name: Optional[str] = Field(None, alias="display_name", title="Display Name", description="")
    create_uid: Optional[int] = Field(None, alias="create_uid", title="Created by", description="")
    create_date: Optional[str] = Field(None, alias="create_date", title="Created on", description="")
    write_uid: Optional[int] = Field(None, alias="write_uid", title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, alias="write_date", title="Last Updated on", description="")

    class Config:
        from_attributes = True

    @classmethod
    def from_execute_kw(cls, data:List[dict], fields:List[str] = []) -> List['LivechatChannelRulesModel']:
        transformed = []
        schema = LivechatChannelRulesModel.model_json_schema()
        
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
