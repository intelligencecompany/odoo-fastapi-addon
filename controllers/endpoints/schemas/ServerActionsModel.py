
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class ServerActionsModel(BaseModel):
    id: Optional[int] = Field(None, alias="id", title="ID", description="")
    name: str = Field("", alias="name", title="Action Name", description="")
    type: str = Field("", alias="type", title="Action Type", description="")
    binding_type: Any = Field(None, alias="binding_type", title="Binding Type", description="")
    usage: Any = Field(None, alias="usage", title="Usage", description="")
    state: Any = Field(None, alias="state", title="Type", description="Type of server action. The following values are available:\n- 'Update a Record': update the values of a record\n- 'Create Activity': create an activity (Discuss)\n- 'Send Email': post a message, a note or send an email (Discuss)\n- 'Send SMS': send SMS, log them on documents (SMS)- 'Add/Remove Followers': add or remove followers to a record (Discuss)\n- 'Create Record': create a new record with new values\n- 'Execute Code': a block of Python code that will be executed\n- 'Send Webhook Notification': send a POST request to an external system, also known as a Webhook\n- 'Execute Existing Actions': define an action that triggers several other server actions")
    xml_id: Optional[str] = Field(None, alias="xml_id", title="External ID", description="ID of the action if defined in a XML file")
    binding_model_id: Optional[int] = Field(None, alias="binding_model_id", title="Binding Model", description="Setting a value makes this action available in the sidebar for the given model.")
    x_model_id: int = Field(0, alias="x_model_id", title="Model", description="Model on which the server action runs.")
    crud_model_id: Optional[int] = Field(None, alias="crud_model_id", title="Record to Create", description="Specify which kind of record should be created. Set this field only to specify a different model than the base model.")
    link_field_id: Optional[int] = Field(None, alias="link_field_id", title="Link Field", description="Specify a field used to link the newly created record on the record used by the server action.")
    groups_id: Optional[List[int]] = Field(None, alias="groups_id", title="Allowed Groups", description="Groups that can execute the server action. Leave empty to allow everybody.")
    update_field_id: Optional[int] = Field(None, alias="update_field_id", title="Field to Update", description="")
    update_related_model_id: Optional[int] = Field(None, alias="update_related_model_id", title="Update Related Model", description="")
    template_id: Optional[int] = Field(None, alias="template_id", title="Email Template", description="")
    activity_type_id: Optional[int] = Field(None, alias="activity_type_id", title="Activity Type", description="")
    activity_user_id: Optional[int] = Field(None, alias="activity_user_id", title="Responsible", description="")
    sms_template_id: Optional[int] = Field(None, alias="sms_template_id", title="SMS Template", description="")
    available_model_ids: Optional[List[int]] = Field(None, alias="available_model_ids", title="Available Models", description="")
    child_ids: Optional[List[int]] = Field(None, alias="child_ids", title="Child Actions", description="Child server actions that will be executed. Note that the last return returned action value will be used as global return value.")
    webhook_field_ids: Optional[List[int]] = Field(None, alias="webhook_field_ids", title="Webhook Fields", description="Fields to send in the POST request. The id and model of the record are always sent as '_id' and '_model'. The name of the action that triggered the webhook is always sent as '_name'.")
    partner_ids: Optional[List[int]] = Field(None, alias="partner_ids", title="Partner", description="")
    help: Optional[Any] = Field(None, alias="help", title="Action Description", description="Optional help text for the users with a description of the target view, such as its usage and purpose.")
    binding_view_types: Optional[str] = Field(None, alias="binding_view_types", title="Binding View Types", description="")
    display_name: Optional[str] = Field(None, alias="display_name", title="Display Name", description="")
    create_uid: Optional[int] = Field(None, alias="create_uid", title="Created by", description="")
    create_date: Optional[str] = Field(None, alias="create_date", title="Created on", description="")
    write_uid: Optional[int] = Field(None, alias="write_uid", title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, alias="write_date", title="Last Updated on", description="")
    sequence: Optional[int] = Field(None, alias="sequence", title="Sequence", description="When dealing with multiple actions, the execution order is based on the sequence. Low number means high priority.")
    x_model_name: Optional[str] = Field(None, alias="x_model_name", title="Model Name", description="")
    code: Optional[Any] = Field(None, alias="code", title="Python Code", description="Write Python code that the action will execute. Some variables are available for use; help about python expression is given in the help tab.")
    crud_model_name: Optional[str] = Field(None, alias="crud_model_name", title="Target Model Name", description="")
    update_path: Optional[str] = Field(None, alias="update_path", title="Field to Update Path", description="Path to the field to update, e.g. 'partner_id.name'")
    update_field_type: Optional[Any] = Field(None, alias="update_field_type", title="Field Type", description="")
    update_m2m_operation: Optional[Any] = Field(None, alias="update_m2m_operation", title="Many2many Operations", description="")
    update_boolean_value: Optional[Any] = Field(None, alias="update_boolean_value", title="Boolean Value", description="")
    value: Optional[Any] = Field(None, alias="value", title="Value", description="For Python expressions, this field may hold a Python expression that can use the same values as for the code field on the server action,e.g. `env.user.name` to set the current user's name as the value or `record.id` to set the ID of the record on which the action is run.\n\nFor Static values, the value will be used directly without evaluation, e.g.`42` or `My custom name` or the selected record.")
    evaluation_type: Optional[Any] = Field(None, alias="evaluation_type", title="Value Type", description="")
    resource_ref: Optional[Any] = Field(None, alias="resource_ref", title="Record", description="")
    selection_value: Optional[int] = Field(None, alias="selection_value", title="Custom Value", description="")
    value_field_to_show: Optional[Any] = Field(None, alias="value_field_to_show", title="Value Field To Show", description="")
    webhook_url: Optional[str] = Field(None, alias="webhook_url", title="Webhook URL", description="URL to send the POST request to.")
    webhook_sample_payload: Optional[Any] = Field(None, alias="webhook_sample_payload", title="Sample Payload", description="")
    mail_post_autofollow: Optional[bool] = Field(None, alias="mail_post_autofollow", title="Subscribe Recipients", description="")
    mail_post_method: Optional[Any] = Field(None, alias="mail_post_method", title="Send Email As", description="")
    activity_summary: Optional[str] = Field(None, alias="activity_summary", title="Title", description="")
    activity_note: Optional[Any] = Field(None, alias="activity_note", title="Note", description="")
    activity_date_deadline_range: Optional[int] = Field(None, alias="activity_date_deadline_range", title="Due Date In", description="")
    activity_date_deadline_range_type: Optional[Any] = Field(None, alias="activity_date_deadline_range_type", title="Due type", description="")
    activity_user_type: Optional[Any] = Field(None, alias="activity_user_type", title="User Type", description="Use 'Specific User' to always assign the same user on the next activity. Use 'Dynamic User' to specify the field name of the user to choose on the record.")
    activity_user_field_name: Optional[str] = Field(None, alias="activity_user_field_name", title="User Field", description="")
    sms_method: Optional[Any] = Field(None, alias="sms_method", title="Send SMS As", description="")
    website_path: Optional[str] = Field(None, alias="website_path", title="Website Path", description="")
    website_url: Optional[str] = Field(None, alias="website_url", title="Website Url", description="The full URL to access the server action through the website.")
    website_published: Optional[bool] = Field(None, alias="website_published", title="Available on the Website", description="A code server action can be executed from the website, using a dedicated controller. The address is <base>/website/action/<website_path>. Set this field as True to allow users to run this action. If it is set to False the action cannot be run through the website.")

    class ConfigDict:
        from_attributes = True

    @classmethod
    def from_execute_kw(cls, item:dict[str, any]) -> 'ServerActionsModel':
        filtered_item = {}
        schema = ServerActionsModel.model_json_schema()

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
    def list_from_execute_kw(cls, data:List[dict], fields:List[str] = []) -> List['ServerActionsModel']:
        transformed = []
        schema = ServerActionsModel.model_json_schema()
        
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
