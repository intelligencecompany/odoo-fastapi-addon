
from pydantic import BaseModel, Field
from typing import Optional, List, Any, Dict

class ModuledependencyModel(BaseModel):
    id: Optional[int] = Field(None, alias="id", title="ID", description="")
    module_id: Optional[int] = Field(None, alias="module_id", title="Module", description="")
    depend_id: Optional[int] = Field(None, alias="depend_id", title="Dependency", description="")
    name: Optional[str] = Field(None, alias="name", title="Name", description="")
    state: Optional[Any] = Field(None, alias="state", title="Status", description="")
    auto_install_required: Optional[bool] = Field(None, alias="auto_install_required", title="Auto Install Required", description="Whether this dependency blocks automatic installation of the dependent")
    display_name: Optional[str] = Field(None, alias="display_name", title="Display Name", description="")

    class ConfigDict:
        from_attributes = True

    @classmethod
    def from_execute_kw(cls, item:Dict[str, Any]) -> 'ModuledependencyModel':
        filtered_item = {}
        schema = ModuledependencyModel.model_json_schema()

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
    def list_from_execute_kw(cls, data:List[dict], fields:List[str] = []) -> List['ModuledependencyModel']:
        transformed = []
        schema = ModuledependencyModel.model_json_schema()
        
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
