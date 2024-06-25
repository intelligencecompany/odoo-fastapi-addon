
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class SMSTemplatesModel(BaseModel):
    id: Optional[int] = Field(None, title="ID", description="")
    body: str = Field("", title="Body", description="")
    model_id: int = Field(0, title="Applies to", description="The type of document this template can be used with")
    sidebar_action_id: Optional[int] = Field(None, title="Sidebar action", description="Sidebar action to make this template available on records of the related document model")
    template_fs: Optional[str] = Field(None, title="Template Filename", description="File from where the template originates. Used to reset broken template.")
    lang: Optional[str] = Field(None, title="Language", description="Optional translation language (ISO code) to select when sending out an email. If not set, the english version will be used. This should usually be a placeholder expression that provides the appropriate language, e.g. {{ object.partner_id.lang }}.")
    render_model: Optional[str] = Field(None, title="Rendering Model", description="")
    name: Optional[str] = Field(None, title="Name", description="")
    model: Optional[str] = Field(None, title="Related Document Model", description="")
    display_name: Optional[str] = Field(None, title="Display Name", description="")
    create_uid: Optional[int] = Field(None, title="Created by", description="")
    create_date: Optional[str] = Field(None, title="Created on", description="")
    write_uid: Optional[int] = Field(None, title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, title="Last Updated on", description="")

