
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class PartnerwithadditionalinformationformailresendModel(BaseModel):
    id: Optional[int] = Field(None, alias="id", title="ID", description="")
    notification_id: int = Field(0, alias="notification_id", title="Notification", description="")
    partner_id: Optional[int] = Field(None, alias="partner_id", title="Partner", description="")
    resend_wizard_id: Optional[int] = Field(None, alias="resend_wizard_id", title="Resend wizard", description="")
    name: Optional[str] = Field(None, alias="name", title="Recipient Name", description="")
    email: Optional[str] = Field(None, alias="email", title="Email Address", description="")
    failure_reason: Optional[Any] = Field(None, alias="failure_reason", title="Failure Reason", description="")
    resend: Optional[bool] = Field(None, alias="resend", title="Try Again", description="")
    message: Optional[str] = Field(None, alias="message", title="Error message", description="")
    partner_readonly: Optional[bool] = Field(None, alias="partner_readonly", title="Partner Readonly", description="")
    display_name: Optional[str] = Field(None, alias="display_name", title="Display Name", description="")
    create_uid: Optional[int] = Field(None, alias="create_uid", title="Created by", description="")
    create_date: Optional[str] = Field(None, alias="create_date", title="Created on", description="")
    write_uid: Optional[int] = Field(None, alias="write_uid", title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, alias="write_date", title="Last Updated on", description="")

    class ConfigDict:
        from_attributes = True

    @classmethod
    def from_execute_kw(cls, item:dict[str, any]) -> 'PartnerwithadditionalinformationformailresendModel':
        filtered_item = {}
        schema = PartnerwithadditionalinformationformailresendModel.model_json_schema()

        for key, value in item.items():
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
    def list_from_execute_kw(cls, data:List[dict], fields:List[str] = []) -> List['PartnerwithadditionalinformationformailresendModel']:
        transformed = []
        schema = PartnerwithadditionalinformationformailresendModel.model_json_schema()
        
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
