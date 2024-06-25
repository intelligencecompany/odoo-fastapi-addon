
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class CannedResponseShortcodeModel(BaseModel):
    id: Optional[int] = Field(None, title="ID", description="")
    source: str = Field("", title="Shortcut", description="Shortcut that will automatically be substituted with longer content in your messages. Type ':' followed by the name of your shortcut (e.g. :hello) to use in your messages.")
    substitution: Any = Field(None, title="Substitution", description="Content that will automatically replace the shortcut of your choosing. This content can still be adapted before sending your message.")
    description: Optional[str] = Field(None, title="Description", description="")
    last_used: Optional[str] = Field(None, title="Last Used", description="Last time this shortcode was used")
    display_name: Optional[str] = Field(None, title="Display Name", description="")
    create_uid: Optional[int] = Field(None, title="Created by", description="")
    create_date: Optional[str] = Field(None, title="Created on", description="")
    write_uid: Optional[int] = Field(None, title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, title="Last Updated on", description="")

