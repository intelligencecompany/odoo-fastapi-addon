
from pydantic import BaseModel, Field
from typing import Optional, List, Any, Dict

class CalendarProviderConfigurationWizardModel(BaseModel):
    id: Optional[int] = Field(None, alias="id", title="ID", description="")
    cal_client_id: Optional[str] = Field(None, alias="cal_client_id", title="Google Client_id", description="")
    external_calendar_provider: Optional[Any] = Field(None, alias="external_calendar_provider", title="Choose an external calendar to configure", description="")
    cal_client_secret: Optional[str] = Field(None, alias="cal_client_secret", title="Google Client_key", description="")
    cal_sync_paused: Optional[bool] = Field(None, alias="cal_sync_paused", title="Google Synchronization Paused", description="")
    microsoft_outlook_client_identifier: Optional[str] = Field(None, alias="microsoft_outlook_client_identifier", title="Outlook Client Id", description="")
    microsoft_outlook_client_secret: Optional[str] = Field(None, alias="microsoft_outlook_client_secret", title="Outlook Client Secret", description="")
    microsoft_outlook_sync_paused: Optional[bool] = Field(None, alias="microsoft_outlook_sync_paused", title="Outlook Synchronization Paused", description="")
    display_name: Optional[str] = Field(None, alias="display_name", title="Display Name", description="")
    create_uid: Optional[int] = Field(None, alias="create_uid", title="Created by", description="")
    create_date: Optional[str] = Field(None, alias="create_date", title="Created on", description="")
    write_uid: Optional[int] = Field(None, alias="write_uid", title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, alias="write_date", title="Last Updated on", description="")

    class ConfigDict:
        from_attributes = True

    @classmethod
    def from_execute_kw(cls, item:dict) -> 'CalendarProviderConfigurationWizardModel':
        filtered_item = {}
        schema = CalendarProviderConfigurationWizardModel.model_json_schema()

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
    def list_from_execute_kw(cls, data:List[dict], fields:List[str] = []) -> List['CalendarProviderConfigurationWizardModel']:
        transformed = []
        schema = CalendarProviderConfigurationWizardModel.model_json_schema()
        
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
