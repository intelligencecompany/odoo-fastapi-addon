
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class TemplateResetMixinModel(BaseModel):

    template_fs: Optional[str] = Field(None, title="Template Filename", description="File from where the template originates. Used to reset broken template.")

