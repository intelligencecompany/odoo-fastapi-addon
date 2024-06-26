
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class IAPAccountModel(BaseModel):
    id: Optional[int] = Field(None, alias="id", title="ID", description="")
    account_info_id: Optional[int] = Field(None, alias="account_info_id", title="Account Info", description="")
    company_ids: Optional[List[int]] = Field(None, alias="company_ids", title="Company", description="")
    account_info_ids: Optional[List[int]] = Field(None, alias="account_info_ids", title="Accounts from IAP", description="")
    name: Optional[str] = Field(None, alias="name", title="Name", description="")
    service_name: Optional[str] = Field(None, alias="service_name", title="Service Name", description="")
    account_token: Optional[str] = Field(None, alias="account_token", title="Account Token", description="Account token is your authentication key for this service. Do not share it.")
    balance: Optional[str] = Field(None, alias="balance", title="Balance", description="")
    description: Optional[str] = Field(None, alias="description", title="Description", description="")
    warn_me: Optional[bool] = Field(None, alias="warn_me", title="Warn me", description="We will send you an email when your balance gets below that threshold")
    warning_threshold: Optional[Any] = Field(None, alias="warning_threshold", title="Threshold", description="")
    warning_email: Optional[str] = Field(None, alias="warning_email", title="Warning Email", description="")
    show_token: Optional[bool] = Field(None, alias="show_token", title="Show Token", description="")
    display_name: Optional[str] = Field(None, alias="display_name", title="Display Name", description="")
    create_uid: Optional[int] = Field(None, alias="create_uid", title="Created by", description="")
    create_date: Optional[str] = Field(None, alias="create_date", title="Created on", description="")
    write_uid: Optional[int] = Field(None, alias="write_uid", title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, alias="write_date", title="Last Updated on", description="")

    class ConfigDict:
        from_attributes = True

    @classmethod
    def from_execute_kw(cls, item:dict) -> 'IAPAccountModel':
        filtered_item = {}
        schema = IAPAccountModel.model_json_schema()

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
    def list_from_execute_kw(cls, data:List[dict], fields:List[str] = []) -> List['IAPAccountModel']:
        transformed = []
        schema = IAPAccountModel.model_json_schema()
        
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
