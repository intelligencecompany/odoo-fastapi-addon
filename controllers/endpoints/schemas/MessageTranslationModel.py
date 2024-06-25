
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class MessageTranslationModel(BaseModel):
    id: Optional[int] = Field(None, title="ID", description="")
    source_lang: str = Field("", title="Source Language", description="Result of the language detection based on its content.")
    target_lang: str = Field("", title="Target Language", description="Shortened language code used as the target for the translation request.")
    body: Any = Field(None, title="Translation Body", description="String received from the translation request.")
    message_id: int = Field(0, title="Message", description="")
    create_date: Optional[str] = Field(None, title="Create Date", description="")
    display_name: Optional[str] = Field(None, title="Display Name", description="")
    create_uid: Optional[int] = Field(None, title="Created by", description="")
    write_uid: Optional[int] = Field(None, title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, title="Last Updated on", description="")

