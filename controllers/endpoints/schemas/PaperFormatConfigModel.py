
from pydantic import BaseModel, Field
from typing import Optional, List, Any, Dict

class PaperFormatConfigModel(BaseModel):
    id: Optional[int] = Field(None, alias="id", title="ID", description="")
    name: str = Field("", alias="name", title="Name", description="")
    dpi: int = Field(0, alias="dpi", title="Output DPI", description="")
    report_ids: Optional[List[int]] = Field(None, alias="report_ids", title="Associated reports", description="Explicitly associated reports")
    default: Optional[bool] = Field(None, alias="default", title="Default paper format?", description="")
    format: Optional[Any] = Field(None, alias="format", title="Paper size", description="Select Proper Paper size")
    margin_top: Optional[Any] = Field(None, alias="margin_top", title="Top Margin (mm)", description="")
    margin_bottom: Optional[Any] = Field(None, alias="margin_bottom", title="Bottom Margin (mm)", description="")
    margin_left: Optional[Any] = Field(None, alias="margin_left", title="Left Margin (mm)", description="")
    margin_right: Optional[Any] = Field(None, alias="margin_right", title="Right Margin (mm)", description="")
    page_height: Optional[int] = Field(None, alias="page_height", title="Page height (mm)", description="")
    page_width: Optional[int] = Field(None, alias="page_width", title="Page width (mm)", description="")
    orientation: Optional[Any] = Field(None, alias="orientation", title="Orientation", description="")
    header_line: Optional[bool] = Field(None, alias="header_line", title="Display a header line", description="")
    header_spacing: Optional[int] = Field(None, alias="header_spacing", title="Header spacing", description="")
    disable_shrinking: Optional[bool] = Field(None, alias="disable_shrinking", title="Disable smart shrinking", description="")
    print_page_width: Optional[Any] = Field(None, alias="print_page_width", title="Print page width (mm)", description="")
    print_page_height: Optional[Any] = Field(None, alias="print_page_height", title="Print page height (mm)", description="")
    display_name: Optional[str] = Field(None, alias="display_name", title="Display Name", description="")
    create_uid: Optional[int] = Field(None, alias="create_uid", title="Created by", description="")
    create_date: Optional[str] = Field(None, alias="create_date", title="Created on", description="")
    write_uid: Optional[int] = Field(None, alias="write_uid", title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, alias="write_date", title="Last Updated on", description="")

    class ConfigDict:
        from_attributes = True

    @classmethod
    def from_execute_kw(cls, item:Dict[str, Any]) -> 'PaperFormatConfigModel':
        filtered_item = {}
        schema = PaperFormatConfigModel.model_json_schema()

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
    def list_from_execute_kw(cls, data:List[dict], fields:List[str] = []) -> List['PaperFormatConfigModel']:
        transformed = []
        schema = PaperFormatConfigModel.model_json_schema()
        
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
