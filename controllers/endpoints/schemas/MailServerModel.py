
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class MailServerModel(BaseModel):
    id: Optional[int] = Field(None, alias="id", title="ID", description="")
    name: str = Field("", alias="name", title="Name", description="")
    smtp_authentication: Any = Field(None, alias="smtp_authentication", title="Authenticate with", description="")
    smtp_encryption: Any = Field(None, alias="smtp_encryption", title="Connection Encryption", description="Choose the connection encryption scheme:\n- None: SMTP sessions are done in cleartext.\n- TLS (STARTTLS): TLS encryption is requested at start of SMTP session (Recommended)\n- SSL/TLS: SMTP sessions are encrypted with SSL/TLS through a dedicated port (default: 465)")
    mail_template_ids: Optional[List[int]] = Field(None, alias="mail_template_ids", title="Mail template using this mail server", description="")
    google_gmail_authorization_code: Optional[str] = Field(None, alias="google_gmail_authorization_code", title="Authorization Code", description="")
    google_gmail_refresh_token: Optional[str] = Field(None, alias="google_gmail_refresh_token", title="Refresh Token", description="")
    google_gmail_access_token: Optional[str] = Field(None, alias="google_gmail_access_token", title="Access Token", description="")
    google_gmail_access_token_expiration: Optional[int] = Field(None, alias="google_gmail_access_token_expiration", title="Access Token Expiration Timestamp", description="")
    google_gmail_uri: Optional[str] = Field(None, alias="google_gmail_uri", title="URI", description="The URL to generate the authorization code from Google")
    from_filter: Optional[str] = Field(None, alias="from_filter", title="FROM Filtering", description="Comma-separated list of addresses or domains for which this server can be used.\ne.g.: \"notification@odoo.com\" or \"odoo.com\"")
    smtp_host: Optional[str] = Field(None, alias="smtp_host", title="SMTP Server", description="Hostname or IP of SMTP server")
    smtp_port: Optional[int] = Field(None, alias="smtp_port", title="SMTP Port", description="SMTP Port. Usually 465 for SSL, and 25 or 587 for other cases.")
    smtp_authentication_info: Optional[Any] = Field(None, alias="smtp_authentication_info", title="Authentication Info", description="")
    smtp_user: Optional[str] = Field(None, alias="smtp_user", title="Username", description="Optional username for SMTP authentication")
    smtp_pass: Optional[str] = Field(None, alias="smtp_pass", title="Password", description="Optional password for SMTP authentication")
    smtp_ssl_certificate: Optional[Any] = Field(None, alias="smtp_ssl_certificate", title="SSL Certificate", description="SSL certificate used for authentication")
    smtp_ssl_private_key: Optional[Any] = Field(None, alias="smtp_ssl_private_key", title="SSL Private Key", description="SSL private key used for authentication")
    smtp_debug: Optional[bool] = Field(None, alias="smtp_debug", title="Debugging", description="If enabled, the full output of SMTP sessions will be written to the server log at DEBUG level (this is very verbose and may include confidential info!)")
    sequence: Optional[int] = Field(None, alias="sequence", title="Priority", description="When no specific mail server is requested for a mail, the highest priority one is used. Default priority is 10 (smaller number = higher priority)")
    active: Optional[bool] = Field(None, alias="active", title="Active", description="")
    display_name: Optional[str] = Field(None, alias="display_name", title="Display Name", description="")
    create_uid: Optional[int] = Field(None, alias="create_uid", title="Created by", description="")
    create_date: Optional[str] = Field(None, alias="create_date", title="Created on", description="")
    write_uid: Optional[int] = Field(None, alias="write_uid", title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, alias="write_date", title="Last Updated on", description="")

    class Config:
        from_attributes = True

    @classmethod
    def from_execute_kw(cls, data:List[dict], fields:List[str] = []) -> List['MailServerModel']:
        transformed = []
        schema = MailServerModel.model_json_schema()
        
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

            transformed.append(cls(**filtered_item))
        return transformed
