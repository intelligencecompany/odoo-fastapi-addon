
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class EmailcompositionwizardModel(BaseModel):
    id: Optional[int] = Field(None, alias="id", title="ID", description="")
    message_type: Any = Field(None, alias="message_type", title="Type", description="Message type: email for email message, notification for system message, comment for other messages such as user replies")
    template_id: Optional[int] = Field(None, alias="template_id", title="Use template", description="")
    parent_id: Optional[int] = Field(None, alias="parent_id", title="Parent Message", description="")
    author_id: Optional[int] = Field(None, alias="author_id", title="Author", description="Author of the message. If not set, email_from may hold an email address that did not match any partner.")
    res_domain_user_id: Optional[int] = Field(None, alias="res_domain_user_id", title="Responsible", description="Used as context used to evaluate composer domain")
    record_alias_domain_id: Optional[int] = Field(None, alias="record_alias_domain_id", title="Alias Domain", description="")
    record_company_id: Optional[int] = Field(None, alias="record_company_id", title="Company", description="")
    subtype_id: Optional[int] = Field(None, alias="subtype_id", title="Subtype", description="")
    mail_activity_type_id: Optional[int] = Field(None, alias="mail_activity_type_id", title="Mail Activity Type", description="")
    mail_server_id: Optional[int] = Field(None, alias="mail_server_id", title="Outgoing mail server", description="")
    attachment_ids: Optional[List[int]] = Field(None, alias="attachment_ids", title="Attachments", description="")
    res_ids: Optional[Any] = Field(None, alias="res_ids", title="Related Document IDs", description="")
    partner_ids: Optional[List[int]] = Field(None, alias="partner_ids", title="Additional Contacts", description="")
    lang: Optional[str] = Field(None, alias="lang", title="Language", description="Optional translation language (ISO code) to select when sending out an email. If not set, the english version will be used. This should usually be a placeholder expression that provides the appropriate language, e.g. {{ object.partner_id.lang }}.")
    render_model: Optional[str] = Field(None, alias="render_model", title="Rendering Model", description="")
    subject: Optional[str] = Field(None, alias="subject", title="Subject", description="")
    body: Optional[Any] = Field(None, alias="body", title="Contents", description="")
    body_has_template_value: Optional[bool] = Field(None, alias="body_has_template_value", title="Body content is the same as the template", description="")
    is_mail_template_editor: Optional[bool] = Field(None, alias="is_mail_template_editor", title="Is Editor", description="")
    can_edit_body: Optional[bool] = Field(None, alias="can_edit_body", title="Can Edit Body", description="")
    email_layout_xmlid: Optional[str] = Field(None, alias="email_layout_xmlid", title="Email Notification Layout", description="")
    email_add_signature: Optional[bool] = Field(None, alias="email_add_signature", title="Add signature", description="")
    email_from: Optional[str] = Field(None, alias="email_from", title="From", description="Email address of the sender. This field is set when no matching partner is found and replaces the author_id field in the chatter.")
    composition_mode: Optional[Any] = Field(None, alias="composition_mode", title="Composition mode", description="")
    composition_batch: Optional[bool] = Field(None, alias="composition_batch", title="Batch composition", description="")
    model: Optional[str] = Field(None, alias="model", title="Related Document Model", description="")
    x_model_is_thread: Optional[bool] = Field(None, alias="x_model_is_thread", title="Thread-Enabled", description="")
    res_domain: Optional[Any] = Field(None, alias="res_domain", title="Active domain", description="")
    record_name: Optional[str] = Field(None, alias="record_name", title="Record Name", description="")
    subtype_is_log: Optional[bool] = Field(None, alias="subtype_is_log", title="Is a log", description="")
    reply_to: Optional[str] = Field(None, alias="reply_to", title="Reply To", description="Reply email address. Setting the reply_to bypasses the automatic thread creation.")
    reply_to_force_new: Optional[bool] = Field(None, alias="reply_to_force_new", title="Considers answers as new thread", description="Manage answers as new incoming emails instead of replies going to the same thread.")
    reply_to_mode: Optional[Any] = Field(None, alias="reply_to_mode", title="Replies", description="Original Discussion: Answers go in the original document discussion thread. \n Another Email Address: Answers go to the email address mentioned in the tracking message-id instead of original document discussion thread. \n This has an impact on the generated message-id.")
    auto_delete: Optional[bool] = Field(None, alias="auto_delete", title="Delete Emails", description="This option permanently removes any track of email after it's been sent, including from the Technical menu in the Settings, in order to preserve storage space of your Odoo database.")
    auto_delete_keep_log: Optional[bool] = Field(None, alias="auto_delete_keep_log", title="Keep Message Copy", description="Keep a copy of the email content if emails are removed (mass mailing only)")
    force_send: Optional[bool] = Field(None, alias="force_send", title="Send mailing or notifications directly", description="")
    scheduled_date: Optional[str] = Field(None, alias="scheduled_date", title="Scheduled Date", description="In comment mode: if set, postpone notifications sending. In mass mail mode: if sent, send emails after that date. This date is considered as being in UTC timezone.")
    use_exclusion_list: Optional[bool] = Field(None, alias="use_exclusion_list", title="Check Exclusion List", description="")
    display_name: Optional[str] = Field(None, alias="display_name", title="Display Name", description="")
    create_uid: Optional[int] = Field(None, alias="create_uid", title="Created by", description="")
    create_date: Optional[str] = Field(None, alias="create_date", title="Created on", description="")
    write_uid: Optional[int] = Field(None, alias="write_uid", title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, alias="write_date", title="Last Updated on", description="")

    class ConfigDict:
        from_attributes = True

    @classmethod
    def from_execute_kw(cls, item:dict[str, any]) -> 'EmailcompositionwizardModel':
        filtered_item = {}
        schema = EmailcompositionwizardModel.model_json_schema()

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
    def list_from_execute_kw(cls, data:List[dict], fields:List[str] = []) -> List['EmailcompositionwizardModel']:
        transformed = []
        schema = EmailcompositionwizardModel.model_json_schema()
        
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
