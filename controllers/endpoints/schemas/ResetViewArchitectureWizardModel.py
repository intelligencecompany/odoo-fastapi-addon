
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class ResetViewArchitectureWizardModel(BaseModel):
    id: Optional[int] = Field(None, alias="id", title="ID", description="")
    reset_mode: Any = Field(None, alias="reset_mode", title="Reset Mode", description="")
    view_id: Optional[int] = Field(None, alias="view_id", title="View", description="")
    compare_view_id: Optional[int] = Field(None, alias="compare_view_id", title="Compare To View", description="")
    view_name: Optional[str] = Field(None, alias="view_name", title="View Name", description="")
    has_diff: Optional[bool] = Field(None, alias="has_diff", title="Has Diff", description="")
    arch_diff: Optional[Any] = Field(None, alias="arch_diff", title="Architecture Diff", description="")
    arch_to_compare: Optional[Any] = Field(None, alias="arch_to_compare", title="Arch To Compare To", description="")
    display_name: Optional[str] = Field(None, alias="display_name", title="Display Name", description="")
    create_uid: Optional[int] = Field(None, alias="create_uid", title="Created by", description="")
    create_date: Optional[str] = Field(None, alias="create_date", title="Created on", description="")
    write_uid: Optional[int] = Field(None, alias="write_uid", title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, alias="write_date", title="Last Updated on", description="")

    class ConfigDict:
        from_attributes = True

    @classmethod
    def from_execute_kw(cls, item:dict) -> 'ResetViewArchitectureWizardModel':
        filtered_item = {}
        schema = ResetViewArchitectureWizardModel.model_json_schema()

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
    def list_from_execute_kw(cls, data:List[dict], fields:List[str] = []) -> List['ResetViewArchitectureWizardModel']:
        transformed = []
        schema = ResetViewArchitectureWizardModel.model_json_schema()
        
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
