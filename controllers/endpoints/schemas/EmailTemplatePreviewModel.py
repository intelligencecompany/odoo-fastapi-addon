
from pydantic import BaseModel, Field
from typing import Optional, List, Any, Dict

class EmailTemplatePreviewModel(BaseModel):
    id: Optional[int] = Field(None, alias="id", title="ID", description="")
    mail_template_id: int = Field(0, alias="mail_template_id", title="Related Mail Template", description="")
    x_model_id: Optional[int] = Field(None, alias="x_model_id", title="Targeted model", description="")
    attachment_ids: Optional[List[int]] = Field(None, alias="attachment_ids", title="Attachment", description="")
    partner_ids: Optional[List[int]] = Field(None, alias="partner_ids", title="Recipients", description="")
    resource_ref: Optional[Any] = Field(None, alias="resource_ref", title="Record", description="")
    lang: Optional[Any] = Field(None, alias="lang", title="Template Preview Language", description="")
    no_record: Optional[bool] = Field(None, alias="no_record", title="No Record", description="")
    error_msg: Optional[str] = Field(None, alias="error_msg", title="Error Message", description="")
    subject: Optional[str] = Field(None, alias="subject", title="Subject", description="")
    email_from: Optional[str] = Field(None, alias="email_from", title="From", description="Sender address")
    email_to: Optional[str] = Field(None, alias="email_to", title="To", description="Comma-separated recipient addresses")
    email_cc: Optional[str] = Field(None, alias="email_cc", title="Cc", description="Carbon copy recipients")
    reply_to: Optional[str] = Field(None, alias="reply_to", title="Reply-To", description="Preferred response address")
    scheduled_date: Optional[str] = Field(None, alias="scheduled_date", title="Scheduled Date", description="The queue manager will send the email after the date")
    body_html: Optional[Any] = Field(None, alias="body_html", title="Body", description="")
    display_name: Optional[str] = Field(None, alias="display_name", title="Display Name", description="")
    create_uid: Optional[int] = Field(None, alias="create_uid", title="Created by", description="")
    create_date: Optional[str] = Field(None, alias="create_date", title="Created on", description="")
    write_uid: Optional[int] = Field(None, alias="write_uid", title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, alias="write_date", title="Last Updated on", description="")

    class ConfigDict:
        from_attributes = True

    @classmethod
    def from_execute_kw(cls, item:Dict[str, Any]) -> 'EmailTemplatePreviewModel':
        filtered_item = {}
        schema = EmailTemplatePreviewModel.model_json_schema()

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
    def list_from_execute_kw(cls, data:List[dict], fields:List[str] = []) -> List['EmailTemplatePreviewModel']:
        transformed = []
        schema = EmailTemplatePreviewModel.model_json_schema()
        
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
