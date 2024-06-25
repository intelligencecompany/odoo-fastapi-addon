
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class EmailDomainModel(BaseModel):
    id: Optional[int] = Field(None, title="ID", description="")
    name: str = Field("", title="Name", description="Email domain e.g. 'example.com' in 'odoo@example.com'")
    bounce_alias: str = Field("", title="Bounce Alias", description="Local-part of email used for Return-Path used when emails bounce e.g. 'bounce' in 'bounce@example.com'")
    catchall_alias: str = Field("", title="Catchall Alias", description="Local-part of email used for Reply-To to catch answers e.g. 'catchall' in 'catchall@example.com'")
    company_ids: Optional[List[int]] = Field(None, title="Companies", description="Companies using this domain as default for sending mails")
    sequence: Optional[int] = Field(None, title="Sequence", description="")
    bounce_email: Optional[str] = Field(None, title="Bounce Email", description="")
    catchall_email: Optional[str] = Field(None, title="Catchall Email", description="")
    default_from: Optional[str] = Field(None, title="Default From Alias", description="Default from when it does not match outgoing server filters. Can be either a local-part e.g. 'notifications' either a complete email address e.g. 'notifications@example.com' to override all outgoing emails.")
    default_from_email: Optional[str] = Field(None, title="Default From", description="")
    display_name: Optional[str] = Field(None, title="Display Name", description="")
    create_uid: Optional[int] = Field(None, title="Created by", description="")
    create_date: Optional[str] = Field(None, title="Created on", description="")
    write_uid: Optional[int] = Field(None, title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, title="Last Updated on", description="")

