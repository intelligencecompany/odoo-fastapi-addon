
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class WebEditorConverterTestModel(BaseModel):
    id: Optional[int] = Field(None, alias="id", title="ID", description="")
    char: Optional[str] = Field(None, alias="char", title="Char", description="")
    integer: Optional[int] = Field(None, alias="integer", title="Integer", description="")
    float: Optional[Any] = Field(None, alias="float", title="Float", description="")
    numeric: Optional[Any] = Field(None, alias="numeric", title="Numeric", description="")
    many2one: Optional[int] = Field(None, alias="many2one", title="Many2One", description="")
    binary: Optional[Any] = Field(None, alias="binary", title="Binary", description="")
    date: Optional[str] = Field(None, alias="date", title="Date", description="")
    datetime: Optional[str] = Field(None, alias="datetime", title="Datetime", description="")
    selection_str: Optional[Any] = Field(None, alias="selection_str", title="Lorsqu'un pancake prend l'avion à destination de Toronto et qu'il fait une escale technique à St Claude, on dit:", description="")
    html: Optional[Any] = Field(None, alias="html", title="Html", description="")
    text: Optional[Any] = Field(None, alias="text", title="Text", description="")
    display_name: Optional[str] = Field(None, alias="display_name", title="Display Name", description="")
    create_uid: Optional[int] = Field(None, alias="create_uid", title="Created by", description="")
    create_date: Optional[str] = Field(None, alias="create_date", title="Created on", description="")
    write_uid: Optional[int] = Field(None, alias="write_uid", title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, alias="write_date", title="Last Updated on", description="")

    class ConfigDict:
        from_attributes = True

    @classmethod
    def from_execute_kw(cls, item:dict[str, any]) -> 'WebEditorConverterTestModel':
        filtered_item = {}
        schema = WebEditorConverterTestModel.model_json_schema()

        for key, value in item.items():
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
    def list_from_execute_kw(cls, data:List[dict], fields:List[str] = []) -> List['WebEditorConverterTestModel']:
        transformed = []
        schema = WebEditorConverterTestModel.model_json_schema()
        
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
