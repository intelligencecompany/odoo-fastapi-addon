
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class ImportModuleModel(BaseModel):
    id: Optional[int] = Field(None, title="ID", description="")
    module_file: Any = Field(None, title="Module .ZIP file", description="")
    state: Optional[Any] = Field(None, title="Status", description="")
    import_message: Optional[Any] = Field(None, title="Import Message", description="")
    force: Optional[bool] = Field(None, title="Force init", description="Force init mode even if installed. (will update `noupdate='1'` records)")
    with_demo: Optional[bool] = Field(None, title="Import demo data of module", description="")
    modules_dependencies: Optional[Any] = Field(None, title="Modules Dependencies", description="")
    display_name: Optional[str] = Field(None, title="Display Name", description="")
    create_uid: Optional[int] = Field(None, title="Created by", description="")
    create_date: Optional[str] = Field(None, title="Created on", description="")
    write_uid: Optional[int] = Field(None, title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, title="Last Updated on", description="")

