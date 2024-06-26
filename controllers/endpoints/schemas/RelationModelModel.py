
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class RelationModelModel(BaseModel):
    id: Optional[int] = Field(None, alias="id", title="ID", description="")
    name: str = Field("", alias="name", title="Relation Name", description="PostgreSQL table name implementing a many2many relation.")
    model: int = Field(0, alias="model", title="Model", description="")
    module: int = Field(0, alias="module", title="Module", description="")
    write_date: Optional[str] = Field(None, alias="write_date", title="Write Date", description="")
    create_date: Optional[str] = Field(None, alias="create_date", title="Create Date", description="")
    display_name: Optional[str] = Field(None, alias="display_name", title="Display Name", description="")
    create_uid: Optional[int] = Field(None, alias="create_uid", title="Created by", description="")
    write_uid: Optional[int] = Field(None, alias="write_uid", title="Last Updated by", description="")

    class ConfigDict:
        from_attributes = True

    @classmethod
    def from_execute_kw(cls, item:dict[str, any]) -> 'RelationModelModel':
        filtered_item = {}
        schema = RelationModelModel.model_json_schema()

        for key in item:
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
    def list_from_execute_kw(cls, data:List[dict], fields:List[str] = []) -> List['RelationModelModel']:
        transformed = []
        schema = RelationModelModel.model_json_schema()
        
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
