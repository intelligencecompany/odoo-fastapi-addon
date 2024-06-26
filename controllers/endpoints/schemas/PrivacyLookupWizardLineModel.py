
from pydantic import BaseModel, Field
from typing import Optional, List, Any, Dict

class PrivacyLookupWizardLineModel(BaseModel):
    id: Optional[int] = Field(None, alias="id", title="ID", description="")
    wizard_id: Optional[int] = Field(None, alias="wizard_id", title="Wizard", description="")
    res_id: int = Field(0, alias="res_id", title="Resource ID", description="")
    res_model_id: Optional[int] = Field(None, alias="res_model_id", title="Related Document Model", description="")
    res_name: Optional[str] = Field(None, alias="res_name", title="Resource name", description="")
    res_model: Optional[str] = Field(None, alias="res_model", title="Document Model", description="")
    resource_ref: Optional[Any] = Field(None, alias="resource_ref", title="Record", description="")
    has_active: Optional[bool] = Field(None, alias="has_active", title="Has Active", description="")
    is_active: Optional[bool] = Field(None, alias="is_active", title="Is Active", description="")
    is_unlinked: Optional[bool] = Field(None, alias="is_unlinked", title="Is Unlinked", description="")
    execution_details: Optional[str] = Field(None, alias="execution_details", title="Execution Details", description="")
    display_name: Optional[str] = Field(None, alias="display_name", title="Display Name", description="")
    create_uid: Optional[int] = Field(None, alias="create_uid", title="Created by", description="")
    create_date: Optional[str] = Field(None, alias="create_date", title="Created on", description="")
    write_uid: Optional[int] = Field(None, alias="write_uid", title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, alias="write_date", title="Last Updated on", description="")

    class ConfigDict:
        from_attributes = True

    @classmethod
    def from_execute_kw(cls, item:Dict[str, Any]) -> 'PrivacyLookupWizardLineModel':
        filtered_item = {}
        schema = PrivacyLookupWizardLineModel.model_json_schema()

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
    def list_from_execute_kw(cls, data:List[dict], fields:List[str] = []) -> List['PrivacyLookupWizardLineModel']:
        transformed = []
        schema = PrivacyLookupWizardLineModel.model_json_schema()
        
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
