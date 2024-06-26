
from pydantic import BaseModel, Field
from typing import Optional, List, Any, Dict

class IAPAccountInfoModel(BaseModel):
    id: Optional[int] = Field(None, alias="id", title="ID", description="")
    account_id: Optional[int] = Field(None, alias="account_id", title="IAP Account", description="")
    account_token: Optional[str] = Field(None, alias="account_token", title="Account Token", description="")
    balance: Optional[Any] = Field(None, alias="balance", title="Balance", description="")
    account_uuid_hashed: Optional[str] = Field(None, alias="account_uuid_hashed", title="Account UUID", description="")
    service_name: Optional[str] = Field(None, alias="service_name", title="Related Service", description="")
    description: Optional[str] = Field(None, alias="description", title="Description", description="")
    warn_me: Optional[bool] = Field(None, alias="warn_me", title="Warn me", description="")
    warning_threshold: Optional[Any] = Field(None, alias="warning_threshold", title="Threshold", description="")
    warning_email: Optional[str] = Field(None, alias="warning_email", title="Warning Email", description="")
    unit_name: Optional[str] = Field(None, alias="unit_name", title="Unit Name", description="")
    display_name: Optional[str] = Field(None, alias="display_name", title="Display Name", description="")
    create_uid: Optional[int] = Field(None, alias="create_uid", title="Created by", description="")
    create_date: Optional[str] = Field(None, alias="create_date", title="Created on", description="")
    write_uid: Optional[int] = Field(None, alias="write_uid", title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, alias="write_date", title="Last Updated on", description="")

    class ConfigDict:
        from_attributes = True

    @classmethod
    def from_execute_kw(cls, item:Dict[str, Any]) -> 'IAPAccountInfoModel':
        filtered_item = {}
        schema = IAPAccountInfoModel.model_json_schema()

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
    def list_from_execute_kw(cls, data:List[dict], fields:List[str] = []) -> List['IAPAccountInfoModel']:
        transformed = []
        schema = IAPAccountInfoModel.model_json_schema()
        
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
