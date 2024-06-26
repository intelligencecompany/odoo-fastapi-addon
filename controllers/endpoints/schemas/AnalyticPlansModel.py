
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class AnalyticPlansModel(BaseModel):
    id: Optional[int] = Field(None, alias="id", title="ID", description="")
    name: str = Field("", alias="name", title="Name", description="")
    default_applicability: Any = Field(None, alias="default_applicability", title="Default Applicability", description="")
    parent_id: Optional[int] = Field(None, alias="parent_id", title="Parent", description="")
    root_id: Optional[int] = Field(None, alias="root_id", title="Root", description="")
    children_ids: Optional[List[int]] = Field(None, alias="children_ids", title="Childrens", description="")
    account_ids: Optional[List[int]] = Field(None, alias="account_ids", title="Accounts", description="")
    applicability_ids: Optional[List[int]] = Field(None, alias="applicability_ids", title="Applicability", description="")
    description: Optional[Any] = Field(None, alias="description", title="Description", description="")
    parent_path: Optional[str] = Field(None, alias="parent_path", title="Parent Path", description="")
    children_count: Optional[int] = Field(None, alias="children_count", title="Children Plans Count", description="")
    complete_name: Optional[str] = Field(None, alias="complete_name", title="Complete Name", description="")
    account_count: Optional[int] = Field(None, alias="account_count", title="Analytic Accounts Count", description="")
    all_account_count: Optional[int] = Field(None, alias="all_account_count", title="All Analytic Accounts Count", description="")
    color: Optional[int] = Field(None, alias="color", title="Color", description="")
    sequence: Optional[int] = Field(None, alias="sequence", title="Sequence", description="")
    display_name: Optional[str] = Field(None, alias="display_name", title="Display Name", description="")
    create_uid: Optional[int] = Field(None, alias="create_uid", title="Created by", description="")
    create_date: Optional[str] = Field(None, alias="create_date", title="Created on", description="")
    write_uid: Optional[int] = Field(None, alias="write_uid", title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, alias="write_date", title="Last Updated on", description="")

    class ConfigDict:
        from_attributes = True

    @classmethod
    def from_execute_kw(cls, item:dict[str, any]) -> 'AnalyticPlansModel':
        filtered_item = {}
        schema = AnalyticPlansModel.model_json_schema()

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
    def list_from_execute_kw(cls, data:List[dict], fields:List[str] = []) -> List['AnalyticPlansModel']:
        transformed = []
        schema = AnalyticPlansModel.model_json_schema()
        
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
