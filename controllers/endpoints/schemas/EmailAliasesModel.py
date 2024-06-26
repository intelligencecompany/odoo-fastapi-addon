
from pydantic import BaseModel, Field
from typing import Optional, List, Any, Dict

class EmailAliasesModel(BaseModel):
    id: Optional[int] = Field(None, alias="id", title="ID", description="")
    alias_defaults: Any = Field(None, alias="alias_defaults", title="Default Values", description="A Python dictionary that will be evaluated to provide default values when creating new records for this alias.")
    alias_contact: Any = Field(None, alias="alias_contact", title="Alias Contact Security", description="Policy to post a message on the document using the mailgateway.\n- everyone: everyone can post\n- partners: only authenticated partners\n- followers: only followers of the related document or members of following channels")
    alias_domain_id: Optional[int] = Field(None, alias="alias_domain_id", title="Alias Domain", description="")
    alias_model_id: int = Field(0, alias="alias_model_id", title="Aliased Model", description="The model (Odoo Document Kind) to which this alias corresponds. Any incoming email that does not reply to an existing record will cause the creation of a new record of this model (e.g. a Project Task)")
    alias_force_thread_id: Optional[int] = Field(None, alias="alias_force_thread_id", title="Record Thread ID", description="Optional ID of a thread (record) to which all incoming messages will be attached, even if they did not reply to it. If set, this will disable the creation of new records completely.")
    alias_parent_model_id: Optional[int] = Field(None, alias="alias_parent_model_id", title="Parent Model", description="Parent model holding the alias. The model holding the alias reference is not necessarily the model given by alias_model_id (example: project (parent_model) and task (model))")
    alias_parent_thread_id: Optional[int] = Field(None, alias="alias_parent_thread_id", title="Parent Record Thread ID", description="ID of the parent record holding the alias (example: project holding the task creation alias)")
    alias_name: Optional[str] = Field(None, alias="alias_name", title="Alias Name", description="The name of the email alias, e.g. 'jobs' if you want to catch emails for <jobs@example.odoo.com>")
    alias_full_name: Optional[str] = Field(None, alias="alias_full_name", title="Alias Email", description="")
    display_name: Optional[str] = Field(None, alias="display_name", title="Display Name", description="")
    alias_domain: Optional[str] = Field(None, alias="alias_domain", title="Alias domain name", description="Email domain e.g. 'example.com' in 'odoo@example.com'")
    alias_incoming_local: Optional[bool] = Field(None, alias="alias_incoming_local", title="Local-part based incoming detection", description="")
    alias_bounced_content: Optional[Any] = Field(None, alias="alias_bounced_content", title="Custom Bounced Message", description="If set, this content will automatically be sent out to unauthorized users instead of the default message.")
    alias_status: Optional[Any] = Field(None, alias="alias_status", title="Alias Status", description="Alias status assessed on the last message received.")
    create_uid: Optional[int] = Field(None, alias="create_uid", title="Created by", description="")
    create_date: Optional[str] = Field(None, alias="create_date", title="Created on", description="")
    write_uid: Optional[int] = Field(None, alias="write_uid", title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, alias="write_date", title="Last Updated on", description="")

    class ConfigDict:
        from_attributes = True

    @classmethod
    def from_execute_kw(cls, item:Dict[str, Any]) -> 'EmailAliasesModel':
        filtered_item = {}
        schema = EmailAliasesModel.model_json_schema()

        for key in item:
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
    def list_from_execute_kw(cls, data:List[dict], fields:List[str] = []) -> List['EmailAliasesModel']:
        transformed = []
        schema = EmailAliasesModel.model_json_schema()
        
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
