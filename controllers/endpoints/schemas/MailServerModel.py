
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class MailServerModel(BaseModel):
    id: Optional[int] = Field(None, title="ID", description="")
    name: str = Field("", title="Name", description="")
    smtp_authentication: Any = Field(None, title="Authenticate with", description="")
    smtp_encryption: Any = Field(None, title="Connection Encryption", description="Choose the connection encryption scheme:\n- None: SMTP sessions are done in cleartext.\n- TLS (STARTTLS): TLS encryption is requested at start of SMTP session (Recommended)\n- SSL/TLS: SMTP sessions are encrypted with SSL/TLS through a dedicated port (default: 465)")
    mail_template_ids: Optional[List[int]] = Field(None, title="Mail template using this mail server", description="")
    google_gmail_authorization_code: Optional[str] = Field(None, title="Authorization Code", description="")
    google_gmail_refresh_token: Optional[str] = Field(None, title="Refresh Token", description="")
    google_gmail_access_token: Optional[str] = Field(None, title="Access Token", description="")
    google_gmail_access_token_expiration: Optional[int] = Field(None, title="Access Token Expiration Timestamp", description="")
    google_gmail_uri: Optional[str] = Field(None, title="URI", description="The URL to generate the authorization code from Google")
    from_filter: Optional[str] = Field(None, title="FROM Filtering", description="Comma-separated list of addresses or domains for which this server can be used.\ne.g.: \"notification@odoo.com\" or \"odoo.com\"")
    smtp_host: Optional[str] = Field(None, title="SMTP Server", description="Hostname or IP of SMTP server")
    smtp_port: Optional[int] = Field(None, title="SMTP Port", description="SMTP Port. Usually 465 for SSL, and 25 or 587 for other cases.")
    smtp_authentication_info: Optional[Any] = Field(None, title="Authentication Info", description="")
    smtp_user: Optional[str] = Field(None, title="Username", description="Optional username for SMTP authentication")
    smtp_pass: Optional[str] = Field(None, title="Password", description="Optional password for SMTP authentication")
    smtp_ssl_certificate: Optional[Any] = Field(None, title="SSL Certificate", description="SSL certificate used for authentication")
    smtp_ssl_private_key: Optional[Any] = Field(None, title="SSL Private Key", description="SSL private key used for authentication")
    smtp_debug: Optional[bool] = Field(None, title="Debugging", description="If enabled, the full output of SMTP sessions will be written to the server log at DEBUG level (this is very verbose and may include confidential info!)")
    sequence: Optional[int] = Field(None, title="Priority", description="When no specific mail server is requested for a mail, the highest priority one is used. Default priority is 10 (smaller number = higher priority)")
    active: Optional[bool] = Field(None, title="Active", description="")
    display_name: Optional[str] = Field(None, title="Display Name", description="")
    create_uid: Optional[int] = Field(None, title="Created by", description="")
    create_date: Optional[str] = Field(None, title="Created on", description="")
    write_uid: Optional[int] = Field(None, title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, title="Last Updated on", description="")

