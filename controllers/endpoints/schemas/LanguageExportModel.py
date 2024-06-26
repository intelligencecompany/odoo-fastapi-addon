
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class LanguageExportModel(BaseModel):
    id: Optional[int] = Field(None, alias="id", title="ID", description="")
    lang: Any = Field(None, alias="lang", title="Language", description="")
    format: Any = Field(None, alias="format", title="File Format", description="")
    export_type: Any = Field(None, alias="export_type", title="Export Type", description="")
    x_model_id: Optional[int] = Field(None, alias="x_model_id", title="Model to Export", description="")
    name: Optional[str] = Field(None, alias="name", title="File Name", description="")
    modules: Optional[List[int]] = Field(None, alias="modules", title="Apps To Export", description="")
    x_model_name: Optional[str] = Field(None, alias="x_model_name", title="Model Name", description="")
    domain: Optional[str] = Field(None, alias="domain", title="Model Domain", description="")
    data: Optional[Any] = Field(None, alias="data", title="File", description="")
    state: Optional[Any] = Field(None, alias="state", title="State", description="")
    display_name: Optional[str] = Field(None, alias="display_name", title="Display Name", description="")
    create_uid: Optional[int] = Field(None, alias="create_uid", title="Created by", description="")
    create_date: Optional[str] = Field(None, alias="create_date", title="Created on", description="")
    write_uid: Optional[int] = Field(None, alias="write_uid", title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, alias="write_date", title="Last Updated on", description="")

    class ConfigDict:
        from_attributes = True

    @classmethod
    def from_execute_kw(cls, item:dict) -> 'LanguageExportModel':
        filtered_item = {}
        schema = LanguageExportModel.model_json_schema()

        for key in item.keys():
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

        return cls(**filtered_item).model_dump(by_alias=True)

    @classmethod
    def list_from_execute_kw(cls, data:List[dict], fields:List[str] = []) -> List['LanguageExportModel']:
        transformed = []
        schema = LanguageExportModel.model_json_schema()
        
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

            transformed.append(cls(**filtered_item).model_dump(by_alias=True))
        return transformed
