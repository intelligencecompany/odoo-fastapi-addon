
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class ModelsModel(BaseModel):
    id: Optional[int] = Field(None, title="ID", description="")
    name: str = Field("", title="Model Description", description="")
    model: str = Field("", title="Model", description="")
    order: str = Field("", title="Order", description="SQL expression for ordering records in the model; e.g. \"x_sequence asc, id desc\"")
    field_id: List[int] = Field([], title="Fields", description="")
    website_form_default_field_id: Optional[int] = Field(None, title="Field for custom form data", description="Specify the field which will contain meta and custom form fields datas.")
    inherited_model_ids: Optional[List[int]] = Field(None, title="Inherited models", description="The list of models that extends the current model.")
    access_ids: Optional[List[int]] = Field(None, title="Access", description="")
    rule_ids: Optional[List[int]] = Field(None, title="Record Rules", description="")
    view_ids: Optional[List[int]] = Field(None, title="Views", description="")
    info: Optional[Any] = Field(None, title="Information", description="")
    state: Optional[Any] = Field(None, title="Type", description="")
    transient: Optional[bool] = Field(None, title="Transient Model", description="")
    modules: Optional[str] = Field(None, title="In Apps", description="List of modules in which the object is defined or inherited")
    count: Optional[int] = Field(None, title="Count (Incl. Archived)", description="Total number of records in this model")
    display_name: Optional[str] = Field(None, title="Display Name", description="")
    create_uid: Optional[int] = Field(None, title="Created by", description="")
    create_date: Optional[str] = Field(None, title="Created on", description="")
    write_uid: Optional[int] = Field(None, title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, title="Last Updated on", description="")
    is_mail_thread: Optional[bool] = Field(None, title="Has Mail Thread", description="")
    is_mail_activity: Optional[bool] = Field(None, title="Has Mail Activity", description="")
    is_mail_blacklist: Optional[bool] = Field(None, title="Has Mail Blacklist", description="")
    is_mail_thread_sms: Optional[bool] = Field(None, title="Mail Thread SMS", description="Whether this model supports messages and notifications through SMS")
    website_form_access: Optional[bool] = Field(None, title="Allowed to use in forms", description="Enable the form builder feature for this model.")
    website_form_label: Optional[str] = Field(None, title="Label for form action", description="Form action label. Ex: crm.lead could be 'Send an e-mail' and project.issue could be 'Create an Issue'.")
    website_form_key: Optional[str] = Field(None, title="Website Form Key", description="Used in FormBuilder Registry")

