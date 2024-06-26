
from pydantic import BaseModel, Field
from typing import Optional, List, Any, Dict

class ClientActionModel(BaseModel):
    id: Optional[int] = Field(None, alias="id", title="ID", description="")
    name: str = Field("", alias="name", title="Action Name", description="")
    type: str = Field("", alias="type", title="Action Type", description="")
    binding_type: Any = Field(None, alias="binding_type", title="Binding Type", description="")
    tag: str = Field("", alias="tag", title="Client action tag", description="An arbitrary string, interpreted by the client according to its own needs and wishes. There is no central tag repository across clients.")
    context: str = Field("", alias="context", title="Context Value", description="Context dictionary as Python expression, empty by default (Default: {})")
    xml_id: Optional[str] = Field(None, alias="xml_id", title="External ID", description="")
    binding_model_id: Optional[int] = Field(None, alias="binding_model_id", title="Binding Model", description="Setting a value makes this action available in the sidebar for the given model.")
    help: Optional[Any] = Field(None, alias="help", title="Action Description", description="Optional help text for the users with a description of the target view, such as its usage and purpose.")
    binding_view_types: Optional[str] = Field(None, alias="binding_view_types", title="Binding View Types", description="")
    display_name: Optional[str] = Field(None, alias="display_name", title="Display Name", description="")
    create_uid: Optional[int] = Field(None, alias="create_uid", title="Created by", description="")
    create_date: Optional[str] = Field(None, alias="create_date", title="Created on", description="")
    write_uid: Optional[int] = Field(None, alias="write_uid", title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, alias="write_date", title="Last Updated on", description="")
    target: Optional[Any] = Field(None, alias="target", title="Target Window", description="")
    res_model: Optional[str] = Field(None, alias="res_model", title="Destination Model", description="Optional model, mostly used for needactions.")
    params: Optional[Any] = Field(None, alias="params", title="Supplementary arguments", description="Arguments sent to the client along with the view tag")
    params_store: Optional[Any] = Field(None, alias="params_store", title="Params storage", description="")

    class ConfigDict:
        from_attributes = True

    @classmethod
    def from_execute_kw(cls, item:dict) -> 'ClientActionModel':
        filtered_item = {}
        schema = ClientActionModel.model_json_schema()

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
    def list_from_execute_kw(cls, data:List[dict], fields:List[str] = []) -> List['ClientActionModel']:
        transformed = []
        schema = ClientActionModel.model_json_schema()
        
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
