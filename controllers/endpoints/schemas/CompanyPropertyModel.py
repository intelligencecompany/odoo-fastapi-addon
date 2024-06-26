
from pydantic import BaseModel, Field
from typing import Optional, List, Any, Dict

class CompanyPropertyModel(BaseModel):
    id: Optional[int] = Field(None, alias="id", title="ID", description="")
    type: Any = Field(None, alias="type", title="Type", description="")
    res_id: Optional[str] = Field(None, alias="res_id", title="Resource", description="If not set, acts as a default value for new resources")
    company_id: Optional[int] = Field(None, alias="company_id", title="Company", description="")
    fields_id: int = Field(0, alias="fields_id", title="Field", description="")
    name: Optional[str] = Field(None, alias="name", title="Name", description="")
    value_float: Optional[Any] = Field(None, alias="value_float", title="Value Float", description="")
    value_integer: Optional[int] = Field(None, alias="value_integer", title="Value Integer", description="")
    value_text: Optional[Any] = Field(None, alias="value_text", title="Value Text", description="")
    value_binary: Optional[Any] = Field(None, alias="value_binary", title="Value Binary", description="")
    value_reference: Optional[str] = Field(None, alias="value_reference", title="Value Reference", description="")
    value_datetime: Optional[str] = Field(None, alias="value_datetime", title="Value Datetime", description="")
    display_name: Optional[str] = Field(None, alias="display_name", title="Display Name", description="")
    create_uid: Optional[int] = Field(None, alias="create_uid", title="Created by", description="")
    create_date: Optional[str] = Field(None, alias="create_date", title="Created on", description="")
    write_uid: Optional[int] = Field(None, alias="write_uid", title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, alias="write_date", title="Last Updated on", description="")

    class ConfigDict:
        from_attributes = True

    @classmethod
    def from_execute_kw(cls, item:dict) -> 'CompanyPropertyModel':
        filtered_item = {}
        schema = CompanyPropertyModel.model_json_schema()

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
    def list_from_execute_kw(cls, data:List[dict], fields:List[str] = []) -> List['CompanyPropertyModel']:
        transformed = []
        schema = CompanyPropertyModel.model_json_schema()
        
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
