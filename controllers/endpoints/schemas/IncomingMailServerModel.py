
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class IncomingMailServerModel(BaseModel):
    id: Optional[int] = Field(None, alias="id", title="ID", description="")
    name: str = Field("", alias="name", title="Name", description="")
    server_type: Any = Field(None, alias="server_type", title="Server Type", description="")
    object_id: Optional[int] = Field(None, alias="object_id", title="Create a New Record", description="Process each incoming mail as part of a conversation corresponding to this document type. This will create new documents for new conversations, or attach follow-up emails to the existing conversations (documents).")
    message_ids: Optional[List[int]] = Field(None, alias="message_ids", title="Messages", description="")
    google_gmail_authorization_code: Optional[str] = Field(None, alias="google_gmail_authorization_code", title="Authorization Code", description="")
    google_gmail_refresh_token: Optional[str] = Field(None, alias="google_gmail_refresh_token", title="Refresh Token", description="")
    google_gmail_access_token: Optional[str] = Field(None, alias="google_gmail_access_token", title="Access Token", description="")
    google_gmail_access_token_expiration: Optional[int] = Field(None, alias="google_gmail_access_token_expiration", title="Access Token Expiration Timestamp", description="")
    google_gmail_uri: Optional[str] = Field(None, alias="google_gmail_uri", title="URI", description="The URL to generate the authorization code from Google")
    active: Optional[bool] = Field(None, alias="active", title="Active", description="")
    state: Optional[Any] = Field(None, alias="state", title="Status", description="")
    server: Optional[str] = Field(None, alias="server", title="Server Name", description="Hostname or IP of the mail server")
    port: Optional[int] = Field(None, alias="port", title="Port", description="")
    server_type_info: Optional[Any] = Field(None, alias="server_type_info", title="Server Type Info", description="")
    is_ssl: Optional[bool] = Field(None, alias="is_ssl", title="SSL/TLS", description="Connections are encrypted with SSL/TLS through a dedicated port (default: IMAPS=993, POP3S=995)")
    attach: Optional[bool] = Field(None, alias="attach", title="Keep Attachments", description="Whether attachments should be downloaded. If not enabled, incoming emails will be stripped of any attachments before being processed")
    original: Optional[bool] = Field(None, alias="original", title="Keep Original", description="Whether a full original copy of each email should be kept for reference and attached to each processed message. This will usually double the size of your message database.")
    date: Optional[str] = Field(None, alias="date", title="Last Fetch Date", description="")
    user: Optional[str] = Field(None, alias="user", title="Username", description="")
    password: Optional[str] = Field(None, alias="password", title="Password", description="")
    priority: Optional[int] = Field(None, alias="priority", title="Server Priority", description="Defines the order of processing, lower values mean higher priority")
    configuration: Optional[Any] = Field(None, alias="configuration", title="Configuration", description="")
    script: Optional[str] = Field(None, alias="script", title="Script", description="")
    display_name: Optional[str] = Field(None, alias="display_name", title="Display Name", description="")
    create_uid: Optional[int] = Field(None, alias="create_uid", title="Created by", description="")
    create_date: Optional[str] = Field(None, alias="create_date", title="Created on", description="")
    write_uid: Optional[int] = Field(None, alias="write_uid", title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, alias="write_date", title="Last Updated on", description="")

    class ConfigDict:
        from_attributes = True

    @classmethod
    def from_execute_kw(cls, data:List[dict], fields:List[str] = []) -> List['IncomingMailServerModel']:
        transformed = []
        schema = IncomingMailServerModel.model_json_schema()
        
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
