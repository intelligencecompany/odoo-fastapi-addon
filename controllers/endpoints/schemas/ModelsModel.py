
from pydantic import BaseModel, Field
from typing import Optional, List, Any, Dict

class ModelsModel(BaseModel):
    id: Optional[int] = Field(None, alias="id", title="ID", description="")
    name: str = Field("", alias="name", title="Model Description", description="")
    model: str = Field("", alias="model", title="Model", description="")
    order: str = Field("", alias="order", title="Order", description="SQL expression for ordering records in the model; e.g. \"x_sequence asc, id desc\"")
    field_id: List[int] = Field([], alias="field_id", title="Fields", description="")
    website_form_default_field_id: Optional[int] = Field(None, alias="website_form_default_field_id", title="Field for custom form data", description="Specify the field which will contain meta and custom form fields datas.")
    inherited_model_ids: Optional[List[int]] = Field(None, alias="inherited_model_ids", title="Inherited models", description="The list of models that extends the current model.")
    access_ids: Optional[List[int]] = Field(None, alias="access_ids", title="Access", description="")
    rule_ids: Optional[List[int]] = Field(None, alias="rule_ids", title="Record Rules", description="")
    view_ids: Optional[List[int]] = Field(None, alias="view_ids", title="Views", description="")
    info: Optional[Any] = Field(None, alias="info", title="Information", description="")
    state: Optional[Any] = Field(None, alias="state", title="Type", description="")
    transient: Optional[bool] = Field(None, alias="transient", title="Transient Model", description="")
    modules: Optional[str] = Field(None, alias="modules", title="In Apps", description="List of modules in which the object is defined or inherited")
    count: Optional[int] = Field(None, alias="count", title="Count (Incl. Archived)", description="Total number of records in this model")
    display_name: Optional[str] = Field(None, alias="display_name", title="Display Name", description="")
    create_uid: Optional[int] = Field(None, alias="create_uid", title="Created by", description="")
    create_date: Optional[str] = Field(None, alias="create_date", title="Created on", description="")
    write_uid: Optional[int] = Field(None, alias="write_uid", title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, alias="write_date", title="Last Updated on", description="")
    is_mail_thread: Optional[bool] = Field(None, alias="is_mail_thread", title="Has Mail Thread", description="")
    is_mail_activity: Optional[bool] = Field(None, alias="is_mail_activity", title="Has Mail Activity", description="")
    is_mail_blacklist: Optional[bool] = Field(None, alias="is_mail_blacklist", title="Has Mail Blacklist", description="")
    is_mail_thread_sms: Optional[bool] = Field(None, alias="is_mail_thread_sms", title="Mail Thread SMS", description="Whether this model supports messages and notifications through SMS")
    website_form_access: Optional[bool] = Field(None, alias="website_form_access", title="Allowed to use in forms", description="Enable the form builder feature for this model.")
    website_form_label: Optional[str] = Field(None, alias="website_form_label", title="Label for form action", description="Form action label. Ex: crm.lead could be 'Send an e-mail' and project.issue could be 'Create an Issue'.")
    website_form_key: Optional[str] = Field(None, alias="website_form_key", title="Website Form Key", description="Used in FormBuilder Registry")

    class ConfigDict:
        from_attributes = True

    @classmethod
    def from_execute_kw(cls, item:dict) -> 'ModelsModel':
        filtered_item = {}
        schema = ModelsModel.model_json_schema()

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
    def list_from_execute_kw(cls, data:List[dict], fields:List[str] = []) -> List['ModelsModel']:
        transformed = []
        schema = ModelsModel.model_json_schema()
        
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
