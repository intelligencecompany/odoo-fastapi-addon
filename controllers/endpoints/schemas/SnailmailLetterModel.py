
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class SnailmailLetterModel(BaseModel):
    id: Optional[int] = Field(None, alias="id", title="ID", description="")
    model: str = Field("", alias="model", title="Model", description="")
    state: Any = Field(None, alias="state", title="Status", description="When a letter is created, the status is 'Pending'.\nIf the letter is correctly sent, the status goes in 'Sent',\nIf not, it will got in state 'Error' and the error message will be displayed in the field 'Error Message'.")
    user_id: Optional[int] = Field(None, alias="user_id", title="Sent by", description="")
    res_id: int = Field(0, alias="res_id", title="Document ID", description="")
    partner_id: int = Field(0, alias="partner_id", title="Recipient", description="")
    company_id: int = Field(0, alias="company_id", title="Company", description="")
    attachment_id: Optional[int] = Field(None, alias="attachment_id", title="Attachment", description="")
    message_id: Optional[int] = Field(None, alias="message_id", title="Snailmail Status Message", description="")
    state_id: Optional[int] = Field(None, alias="state_id", title="State", description="")
    country_id: Optional[int] = Field(None, alias="country_id", title="Country", description="")
    notification_ids: Optional[List[int]] = Field(None, alias="notification_ids", title="Notifications", description="")
    report_template: Optional[int] = Field(None, alias="report_template", title="Optional report to print and attach", description="")
    attachment_datas: Optional[Any] = Field(None, alias="attachment_datas", title="Document", description="")
    attachment_fname: Optional[str] = Field(None, alias="attachment_fname", title="Attachment Filename", description="")
    color: Optional[bool] = Field(None, alias="color", title="Color", description="")
    cover: Optional[bool] = Field(None, alias="cover", title="Cover Page", description="")
    duplex: Optional[bool] = Field(None, alias="duplex", title="Both side", description="")
    error_code: Optional[Any] = Field(None, alias="error_code", title="Error", description="")
    info_msg: Optional[str] = Field(None, alias="info_msg", title="Information", description="")
    reference: Optional[str] = Field(None, alias="reference", title="Related Record", description="")
    street: Optional[str] = Field(None, alias="street", title="Street", description="")
    street2: Optional[str] = Field(None, alias="street2", title="Street2", description="")
    zip: Optional[str] = Field(None, alias="zip", title="Zip", description="")
    city: Optional[str] = Field(None, alias="city", title="City", description="")
    display_name: Optional[str] = Field(None, alias="display_name", title="Display Name", description="")
    create_uid: Optional[int] = Field(None, alias="create_uid", title="Created by", description="")
    create_date: Optional[str] = Field(None, alias="create_date", title="Created on", description="")
    write_uid: Optional[int] = Field(None, alias="write_uid", title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, alias="write_date", title="Last Updated on", description="")

    class Config:
        from_attributes = True

    @classmethod
    def from_execute_kw(cls, data:List[dict], fields:List[str] = []) -> List['SnailmailLetterModel']:
        transformed = []
        schema = SnailmailLetterModel.model_json_schema()
        
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

            transformed.append(cls(**filtered_item))
        return transformed
