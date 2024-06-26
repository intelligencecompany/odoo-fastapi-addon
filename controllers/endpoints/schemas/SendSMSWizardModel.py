
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class SendSMSWizardModel(BaseModel):
    id: Optional[int] = Field(None, alias="id", title="ID", description="")
    composition_mode: Any = Field(None, alias="composition_mode", title="Composition Mode", description="")
    body: Any = Field(None, alias="body", title="Message", description="")
    res_id: Optional[int] = Field(None, alias="res_id", title="Document ID", description="")
    template_id: Optional[int] = Field(None, alias="template_id", title="Use Template", description="")
    res_ids: Optional[str] = Field(None, alias="res_ids", title="Document IDs", description="")
    res_model: Optional[str] = Field(None, alias="res_model", title="Document Model Name", description="")
    res_model_description: Optional[str] = Field(None, alias="res_model_description", title="Document Model Description", description="")
    res_ids_count: Optional[int] = Field(None, alias="res_ids_count", title="Visible records count", description="Number of recipients that will receive the SMS if sent in mass mode, without applying the Active Domain value")
    comment_single_recipient: Optional[bool] = Field(None, alias="comment_single_recipient", title="Single Mode", description="Indicates if the SMS composer targets a single specific recipient")
    mass_keep_log: Optional[bool] = Field(None, alias="mass_keep_log", title="Keep a note on document", description="")
    mass_force_send: Optional[bool] = Field(None, alias="mass_force_send", title="Send directly", description="")
    mass_use_blacklist: Optional[bool] = Field(None, alias="mass_use_blacklist", title="Use blacklist", description="")
    recipient_valid_count: Optional[int] = Field(None, alias="recipient_valid_count", title="# Valid recipients", description="")
    recipient_invalid_count: Optional[int] = Field(None, alias="recipient_invalid_count", title="# Invalid recipients", description="")
    recipient_single_description: Optional[Any] = Field(None, alias="recipient_single_description", title="Recipients (Partners)", description="")
    recipient_single_number: Optional[str] = Field(None, alias="recipient_single_number", title="Stored Recipient Number", description="")
    recipient_single_number_itf: Optional[str] = Field(None, alias="recipient_single_number_itf", title="Recipient Number", description="Phone number of the recipient. If changed, it will be recorded on recipient's profile.")
    recipient_single_valid: Optional[bool] = Field(None, alias="recipient_single_valid", title="Is valid", description="")
    number_field_name: Optional[str] = Field(None, alias="number_field_name", title="Number Field", description="")
    numbers: Optional[str] = Field(None, alias="numbers", title="Recipients (Numbers)", description="")
    sanitized_numbers: Optional[str] = Field(None, alias="sanitized_numbers", title="Sanitized Number", description="")
    display_name: Optional[str] = Field(None, alias="display_name", title="Display Name", description="")
    create_uid: Optional[int] = Field(None, alias="create_uid", title="Created by", description="")
    create_date: Optional[str] = Field(None, alias="create_date", title="Created on", description="")
    write_uid: Optional[int] = Field(None, alias="write_uid", title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, alias="write_date", title="Last Updated on", description="")

    class ConfigDict:
        from_attributes = True

    @classmethod
    def from_execute_kw(cls, item:dict) -> 'SendSMSWizardModel':
        filtered_item = {}
        schema = SendSMSWizardModel.model_json_schema()

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
    def list_from_execute_kw(cls, data:List[dict], fields:List[str] = []) -> List['SendSMSWizardModel']:
        transformed = []
        schema = SendSMSWizardModel.model_json_schema()
        
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
