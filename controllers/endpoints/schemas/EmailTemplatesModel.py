
from pydantic import BaseModel, Field
from typing import Optional, List, Any, Dict

class EmailTemplatesModel(BaseModel):
    id: Optional[int] = Field(None, alias="id", title="ID", description="")
    x_model_id: Optional[int] = Field(None, alias="x_model_id", title="Applies to", description="")
    user_id: Optional[int] = Field(None, alias="user_id", title="User", description="The template belongs to this user")
    mail_server_id: Optional[int] = Field(None, alias="mail_server_id", title="Outgoing Mail Server", description="Optional preferred server for outgoing mails. If not set, the highest priority one will be used.")
    attachment_ids: Optional[List[int]] = Field(None, alias="attachment_ids", title="Attachments", description="You may attach files to this template, to be added to all emails created from this template")
    report_template_ids: Optional[List[int]] = Field(None, alias="report_template_ids", title="Dynamic Reports", description="")
    template_fs: Optional[str] = Field(None, alias="template_fs", title="Template Filename", description="File from where the template originates. Used to reset broken template.")
    lang: Optional[str] = Field(None, alias="lang", title="Language", description="Optional translation language (ISO code) to select when sending out an email. If not set, the english version will be used. This should usually be a placeholder expression that provides the appropriate language, e.g. {{ object.partner_id.lang }}.")
    render_model: Optional[str] = Field(None, alias="render_model", title="Rendering Model", description="")
    name: Optional[str] = Field(None, alias="name", title="Name", description="")
    description: Optional[Any] = Field(None, alias="description", title="Template description", description="This field is used for internal description of the template's usage.")
    active: Optional[bool] = Field(None, alias="active", title="Active", description="")
    template_category: Optional[Any] = Field(None, alias="template_category", title="Template Category", description="")
    model: Optional[str] = Field(None, alias="model", title="Related Document Model", description="")
    subject: Optional[str] = Field(None, alias="subject", title="Subject", description="Subject (placeholders may be used here)")
    email_from: Optional[str] = Field(None, alias="email_from", title="From", description="Sender address (placeholders may be used here). If not set, the default value will be the author's email alias if configured, or email address.")
    use_default_to: Optional[bool] = Field(None, alias="use_default_to", title="Default recipients", description="Default recipients of the record:\n- partner (using id on a partner or the partner_id field) OR\n- email (using email_from or email field)")
    email_to: Optional[str] = Field(None, alias="email_to", title="To (Emails)", description="Comma-separated recipient addresses (placeholders may be used here)")
    partner_to: Optional[str] = Field(None, alias="partner_to", title="To (Partners)", description="Comma-separated ids of recipient partners (placeholders may be used here)")
    email_cc: Optional[str] = Field(None, alias="email_cc", title="Cc", description="Carbon copy recipients (placeholders may be used here)")
    reply_to: Optional[str] = Field(None, alias="reply_to", title="Reply To", description="Email address to which replies will be redirected when sending emails in mass; only used when the reply is not logged in the original discussion thread.")
    body_html: Optional[Any] = Field(None, alias="body_html", title="Body", description="")
    email_layout_xmlid: Optional[str] = Field(None, alias="email_layout_xmlid", title="Email Notification Layout", description="")
    scheduled_date: Optional[str] = Field(None, alias="scheduled_date", title="Scheduled Date", description="If set, the queue manager will send the email after the date. If not set, the email will be send as soon as possible. You can use dynamic expression.")
    auto_delete: Optional[bool] = Field(None, alias="auto_delete", title="Auto Delete", description="This option permanently removes any track of email after it's been sent, including from the Technical menu in the Settings, in order to preserve storage space of your Odoo database.")
    ref_ir_act_window: Optional[int] = Field(None, alias="ref_ir_act_window", title="Sidebar action", description="Sidebar action to make this template available on records of the related document model")
    can_write: Optional[bool] = Field(None, alias="can_write", title="Can Write", description="The current user can edit the template.")
    is_template_editor: Optional[bool] = Field(None, alias="is_template_editor", title="Is Template Editor", description="")
    display_name: Optional[str] = Field(None, alias="display_name", title="Display Name", description="")
    create_uid: Optional[int] = Field(None, alias="create_uid", title="Created by", description="")
    create_date: Optional[str] = Field(None, alias="create_date", title="Created on", description="")
    write_uid: Optional[int] = Field(None, alias="write_uid", title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, alias="write_date", title="Last Updated on", description="")

    class ConfigDict:
        from_attributes = True

    @classmethod
    def from_execute_kw(cls, item:Dict[str, Any]) -> 'EmailTemplatesModel':
        filtered_item = {}
        schema = EmailTemplatesModel.model_json_schema()

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
    def list_from_execute_kw(cls, data:List[dict], fields:List[str] = []) -> List['EmailTemplatesModel']:
        transformed = []
        schema = EmailTemplatesModel.model_json_schema()
        
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
