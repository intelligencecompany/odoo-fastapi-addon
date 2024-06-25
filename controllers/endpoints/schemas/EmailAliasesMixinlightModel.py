
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class EmailAliasesMixinlightModel(BaseModel):

    alias_id: Optional[int] = Field(None, title="Alias", description="")
    alias_domain_id: Optional[int] = Field(None, title="Alias Domain", description="")
    alias_name: Optional[str] = Field(None, title="Alias Name", description="The name of the email alias, e.g. 'jobs' if you want to catch emails for <jobs@example.odoo.com>")
    alias_domain: Optional[str] = Field(None, title="Alias Domain Name", description="Email domain e.g. 'example.com' in 'odoo@example.com'")
    alias_defaults: Optional[Any] = Field(None, title="Default Values", description="A Python dictionary that will be evaluated to provide default values when creating new records for this alias.")
    alias_email: Optional[str] = Field(None, title="Email Alias", description="")

