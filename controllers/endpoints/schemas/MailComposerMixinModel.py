
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class MailComposerMixinModel(BaseModel):

    template_id: Optional[int] = Field(None, title="Mail Template", description="")
    lang: Optional[str] = Field(None, title="Language", description="Optional translation language (ISO code) to select when sending out an email. If not set, the english version will be used. This should usually be a placeholder expression that provides the appropriate language, e.g. {{ object.partner_id.lang }}.")
    render_model: Optional[str] = Field(None, title="Rendering Model", description="")
    subject: Optional[str] = Field(None, title="Subject", description="")
    body: Optional[Any] = Field(None, title="Contents", description="")
    body_has_template_value: Optional[bool] = Field(None, title="Body content is the same as the template", description="")
    is_mail_template_editor: Optional[bool] = Field(None, title="Is Editor", description="")
    can_edit_body: Optional[bool] = Field(None, title="Can Edit Body", description="")

