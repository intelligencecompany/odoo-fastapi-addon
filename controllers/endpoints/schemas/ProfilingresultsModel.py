
from pydantic import BaseModel, Field
from typing import Optional, List, Any, Dict

class ProfilingresultsModel(BaseModel):
    id: Optional[int] = Field(None, alias="id", title="ID", description="")
    create_date: Optional[str] = Field(None, alias="create_date", title="Creation Date", description="")
    session: Optional[str] = Field(None, alias="session", title="Session", description="")
    name: Optional[str] = Field(None, alias="name", title="Description", description="")
    duration: Optional[Any] = Field(None, alias="duration", title="Duration", description="")
    init_stack_trace: Optional[Any] = Field(None, alias="init_stack_trace", title="Initial stack trace", description="")
    sql: Optional[Any] = Field(None, alias="sql", title="Sql", description="")
    sql_count: Optional[int] = Field(None, alias="sql_count", title="Queries Count", description="")
    traces_async: Optional[Any] = Field(None, alias="traces_async", title="Traces Async", description="")
    traces_sync: Optional[Any] = Field(None, alias="traces_sync", title="Traces Sync", description="")
    qweb: Optional[Any] = Field(None, alias="qweb", title="Qweb", description="")
    entry_count: Optional[int] = Field(None, alias="entry_count", title="Entry count", description="")
    speedscope: Optional[Any] = Field(None, alias="speedscope", title="Speedscope", description="")
    speedscope_url: Optional[Any] = Field(None, alias="speedscope_url", title="Open", description="")
    display_name: Optional[str] = Field(None, alias="display_name", title="Display Name", description="")

    class ConfigDict:
        from_attributes = True

    @classmethod
    def from_execute_kw(cls, item:dict) -> 'ProfilingresultsModel':
        filtered_item = {}
        schema = ProfilingresultsModel.model_json_schema()

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
    def list_from_execute_kw(cls, data:List[dict], fields:List[str] = []) -> List['ProfilingresultsModel']:
        transformed = []
        schema = ProfilingresultsModel.model_json_schema()
        
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
