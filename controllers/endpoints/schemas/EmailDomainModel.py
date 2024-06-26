
from pydantic import BaseModel, Field
from typing import Optional, List, Any, Dict

class EmailDomainModel(BaseModel):
    id: Optional[int] = Field(None, alias="id", title="ID", description="")
    name: str = Field("", alias="name", title="Name", description="Email domain e.g. 'example.com' in 'odoo@example.com'")
    bounce_alias: str = Field("", alias="bounce_alias", title="Bounce Alias", description="Local-part of email used for Return-Path used when emails bounce e.g. 'bounce' in 'bounce@example.com'")
    catchall_alias: str = Field("", alias="catchall_alias", title="Catchall Alias", description="Local-part of email used for Reply-To to catch answers e.g. 'catchall' in 'catchall@example.com'")
    company_ids: Optional[List[int]] = Field(None, alias="company_ids", title="Companies", description="Companies using this domain as default for sending mails")
    sequence: Optional[int] = Field(None, alias="sequence", title="Sequence", description="")
    bounce_email: Optional[str] = Field(None, alias="bounce_email", title="Bounce Email", description="")
    catchall_email: Optional[str] = Field(None, alias="catchall_email", title="Catchall Email", description="")
    default_from: Optional[str] = Field(None, alias="default_from", title="Default From Alias", description="Default from when it does not match outgoing server filters. Can be either a local-part e.g. 'notifications' either a complete email address e.g. 'notifications@example.com' to override all outgoing emails.")
    default_from_email: Optional[str] = Field(None, alias="default_from_email", title="Default From", description="")
    display_name: Optional[str] = Field(None, alias="display_name", title="Display Name", description="")
    create_uid: Optional[int] = Field(None, alias="create_uid", title="Created by", description="")
    create_date: Optional[str] = Field(None, alias="create_date", title="Created on", description="")
    write_uid: Optional[int] = Field(None, alias="write_uid", title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, alias="write_date", title="Last Updated on", description="")

    class ConfigDict:
        from_attributes = True

    @classmethod
    def from_execute_kw(cls, item:dict) -> 'EmailDomainModel':
        filtered_item = {}
        schema = EmailDomainModel.model_json_schema()

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
    def list_from_execute_kw(cls, data:List[dict], fields:List[str] = []) -> List['EmailDomainModel']:
        transformed = []
        schema = EmailDomainModel.model_json_schema()
        
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
