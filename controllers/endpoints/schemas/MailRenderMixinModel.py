
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class MailRenderMixinModel(BaseModel):

    lang: Optional[str] = Field(None, title="Language", description="Optional translation language (ISO code) to select when sending out an email. If not set, the english version will be used. This should usually be a placeholder expression that provides the appropriate language, e.g. {{ object.partner_id.lang }}.")
    render_model: Optional[str] = Field(None, title="Rendering Model", description="")

