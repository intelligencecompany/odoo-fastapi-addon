
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class InstallLanguageModel(BaseModel):
    id: Optional[int] = Field(None, title="ID", description="")
    first_lang_id: Optional[int] = Field(None, title="First Lang", description="Used when the user only selects one language and is given the option to switch to it")
    lang_ids: List[int] = Field([], title="Languages", description="")
    website_ids: Optional[List[int]] = Field(None, title="Websites to translate", description="")
    overwrite: Optional[bool] = Field(None, title="Overwrite Existing Terms", description="If you check this box, your customized translations will be overwritten and replaced by the official ones.")
    display_name: Optional[str] = Field(None, title="Display Name", description="")
    create_uid: Optional[int] = Field(None, title="Created by", description="")
    create_date: Optional[str] = Field(None, title="Created on", description="")
    write_uid: Optional[int] = Field(None, title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, title="Last Updated on", description="")

