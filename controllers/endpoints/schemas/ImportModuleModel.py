
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class ImportModuleModel(BaseModel):
    id: Optional[int] = Field(None, alias="id", title="ID", description="")
    module_file: Any = Field(None, alias="module_file", title="Module .ZIP file", description="")
    state: Optional[Any] = Field(None, alias="state", title="Status", description="")
    import_message: Optional[Any] = Field(None, alias="import_message", title="Import Message", description="")
    force: Optional[bool] = Field(None, alias="force", title="Force init", description="Force init mode even if installed. (will update `noupdate='1'` records)")
    with_demo: Optional[bool] = Field(None, alias="with_demo", title="Import demo data of module", description="")
    modules_dependencies: Optional[Any] = Field(None, alias="modules_dependencies", title="Modules Dependencies", description="")
    display_name: Optional[str] = Field(None, alias="display_name", title="Display Name", description="")
    create_uid: Optional[int] = Field(None, alias="create_uid", title="Created by", description="")
    create_date: Optional[str] = Field(None, alias="create_date", title="Created on", description="")
    write_uid: Optional[int] = Field(None, alias="write_uid", title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, alias="write_date", title="Last Updated on", description="")

    class Config:
        from_attributes = True

    @classmethod
    def from_execute_kw(cls, data:List[dict], fields:List[str] = []) -> List['ImportModuleModel']:
        transformed = []
        schema = ImportModuleModel.model_json_schema()
        
        for item in data:
            filtered_item = {}

            if len(fields) == 0:
                fields = item.keys()

            for key in fields:
                if key in item:
                    value = item[key]
                    model_type = 'any'

                    if 'anyOf' in schema['properties'][key] and 'type' in schema['properties'][key]['anyOf'][0]:
                        model_type = schema['properties'][key]['anyOf'][0]['type']
                    elif 'type' in schema['properties'][key]:
                        model_type = schema['properties'][key]['type']

                    if isinstance(value, list) and model_type != 'array':
                        value = value[0] if item[key] else None
                    
                    if isinstance(value, bool) and model_type == 'string':
                        value = ''

                    if value is not None:
                        filtered_item[key] = value

            transformed.append(cls(**filtered_item))
        return transformed
