
from pydantic import BaseModel, Field
from typing import Optional, List, Any, Dict

class CopyofashareddashboardModel(BaseModel):
    id: Optional[int] = Field(None, alias="id", title="ID", description="")
    spreadsheet_binary_data: Any = Field(None, alias="spreadsheet_binary_data", title="Spreadsheet file", description="")
    access_token: str = Field("", alias="access_token", title="Access Token", description="")
    dashboard_id: int = Field(0, alias="dashboard_id", title="Dashboard", description="")
    spreadsheet_data: Optional[Any] = Field(None, alias="spreadsheet_data", title="Spreadsheet Data", description="")
    thumbnail: Optional[Any] = Field(None, alias="thumbnail", title="Thumbnail", description="")
    excel_export: Optional[Any] = Field(None, alias="excel_export", title="Excel Export", description="")
    full_url: Optional[str] = Field(None, alias="full_url", title="URL", description="")
    name: Optional[str] = Field(None, alias="name", title="Name", description="")
    display_name: Optional[str] = Field(None, alias="display_name", title="Display Name", description="")
    create_uid: Optional[int] = Field(None, alias="create_uid", title="Created by", description="")
    create_date: Optional[str] = Field(None, alias="create_date", title="Created on", description="")
    write_uid: Optional[int] = Field(None, alias="write_uid", title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, alias="write_date", title="Last Updated on", description="")

    class ConfigDict:
        from_attributes = True

    @classmethod
    def from_execute_kw(cls, item:dict) -> 'CopyofashareddashboardModel':
        filtered_item = {}
        schema = CopyofashareddashboardModel.model_json_schema()

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
    def list_from_execute_kw(cls, data:List[dict], fields:List[str] = []) -> List['CopyofashareddashboardModel']:
        transformed = []
        schema = CopyofashareddashboardModel.model_json_schema()
        
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
