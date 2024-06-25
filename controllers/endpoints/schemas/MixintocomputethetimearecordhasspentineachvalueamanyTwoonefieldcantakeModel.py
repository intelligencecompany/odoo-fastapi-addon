
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class MixintocomputethetimearecordhasspentineachvalueamanyTwoonefieldcantakeModel(BaseModel):

    duration_tracking: Optional[Any] = Field(None, title="Status time", description="JSON that maps ids from a many2one field to seconds spent")

