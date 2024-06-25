
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class EmailAliasesModel(BaseModel):
    id: Optional[int] = Field(None, title="ID", description="")
    alias_defaults: Any = Field(None, title="Default Values", description="A Python dictionary that will be evaluated to provide default values when creating new records for this alias.")
    alias_contact: Any = Field(None, title="Alias Contact Security", description="Policy to post a message on the document using the mailgateway.\n- everyone: everyone can post\n- partners: only authenticated partners\n- followers: only followers of the related document or members of following channels")
    alias_domain_id: Optional[int] = Field(None, title="Alias Domain", description="")
    alias_model_id: int = Field(0, title="Aliased Model", description="The model (Odoo Document Kind) to which this alias corresponds. Any incoming email that does not reply to an existing record will cause the creation of a new record of this model (e.g. a Project Task)")
    alias_force_thread_id: Optional[int] = Field(None, title="Record Thread ID", description="Optional ID of a thread (record) to which all incoming messages will be attached, even if they did not reply to it. If set, this will disable the creation of new records completely.")
    alias_parent_model_id: Optional[int] = Field(None, title="Parent Model", description="Parent model holding the alias. The model holding the alias reference is not necessarily the model given by alias_model_id (example: project (parent_model) and task (model))")
    alias_parent_thread_id: Optional[int] = Field(None, title="Parent Record Thread ID", description="ID of the parent record holding the alias (example: project holding the task creation alias)")
    alias_name: Optional[str] = Field(None, title="Alias Name", description="The name of the email alias, e.g. 'jobs' if you want to catch emails for <jobs@example.odoo.com>")
    alias_full_name: Optional[str] = Field(None, title="Alias Email", description="")
    display_name: Optional[str] = Field(None, title="Display Name", description="")
    alias_domain: Optional[str] = Field(None, title="Alias domain name", description="Email domain e.g. 'example.com' in 'odoo@example.com'")
    alias_incoming_local: Optional[bool] = Field(None, title="Local-part based incoming detection", description="")
    alias_bounced_content: Optional[Any] = Field(None, title="Custom Bounced Message", description="If set, this content will automatically be sent out to unauthorized users instead of the default message.")
    alias_status: Optional[Any] = Field(None, title="Alias Status", description="Alias status assessed on the last message received.")
    create_uid: Optional[int] = Field(None, title="Created by", description="")
    create_date: Optional[str] = Field(None, title="Created on", description="")
    write_uid: Optional[int] = Field(None, title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, title="Last Updated on", description="")

