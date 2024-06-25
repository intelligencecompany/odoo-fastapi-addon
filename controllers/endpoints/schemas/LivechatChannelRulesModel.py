
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class LivechatChannelRulesModel(BaseModel):
    id: Optional[int] = Field(None, title="ID", description="")
    action: Any = Field(None, title="Live Chat Button", description="* 'Show' displays the chat button on the pages.\n* 'Show with notification' is 'Show' in addition to a floating text just next to the button.\n* 'Open automatically' displays the button and automatically opens the conversation pane.\n* 'Hide' hides the chat button on the pages.")
    chatbot_script_id: Optional[int] = Field(None, title="Chatbot", description="")
    channel_id: Optional[int] = Field(None, title="Channel", description="The channel of the rule")
    country_ids: Optional[List[int]] = Field(None, title="Country", description="The rule will only be applied for these countries. Example: if you select 'Belgium' and 'United States' and that you set the action to 'Hide', the chat button will be hidden on the specified URL from the visitors located in these 2 countries. This feature requires GeoIP installed on your server.")
    regex_url: Optional[str] = Field(None, title="URL Regex", description="Regular expression specifying the web pages this rule will be applied on.")
    auto_popup_timer: Optional[int] = Field(None, title="Open automatically timer", description="Delay (in seconds) to automatically open the conversation window. Note: the selected action must be 'Open automatically' otherwise this parameter will not be taken into account.")
    chatbot_only_if_no_operator: Optional[bool] = Field(None, title="Enabled only if no operator", description="Enable the bot only if there is no operator available")
    sequence: Optional[int] = Field(None, title="Matching order", description="Given the order to find a matching rule. If 2 rules are matching for the given url/country, the one with the lowest sequence will be chosen.")
    display_name: Optional[str] = Field(None, title="Display Name", description="")
    create_uid: Optional[int] = Field(None, title="Created by", description="")
    create_date: Optional[str] = Field(None, title="Created on", description="")
    write_uid: Optional[int] = Field(None, title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, title="Last Updated on", description="")

