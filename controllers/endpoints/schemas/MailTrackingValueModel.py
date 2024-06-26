
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class MailTrackingValueModel(BaseModel):
    id: Optional[int] = Field(None, alias="id", title="ID", description="")
    field_id: Optional[int] = Field(None, alias="field_id", title="Field", description="")
    currency_id: Optional[int] = Field(None, alias="currency_id", title="Currency", description="Used to display the currency when tracking monetary values")
    mail_message_id: int = Field(0, alias="mail_message_id", title="Message ID", description="")
    field_info: Optional[Any] = Field(None, alias="field_info", title="Removed field information", description="")
    field_groups: Optional[str] = Field(None, alias="field_groups", title="Field Groups", description="")
    old_value_integer: Optional[int] = Field(None, alias="old_value_integer", title="Old Value Integer", description="")
    old_value_float: Optional[Any] = Field(None, alias="old_value_float", title="Old Value Float", description="")
    old_value_char: Optional[str] = Field(None, alias="old_value_char", title="Old Value Char", description="")
    old_value_text: Optional[Any] = Field(None, alias="old_value_text", title="Old Value Text", description="")
    old_value_datetime: Optional[str] = Field(None, alias="old_value_datetime", title="Old Value DateTime", description="")
    new_value_integer: Optional[int] = Field(None, alias="new_value_integer", title="New Value Integer", description="")
    new_value_float: Optional[Any] = Field(None, alias="new_value_float", title="New Value Float", description="")
    new_value_char: Optional[str] = Field(None, alias="new_value_char", title="New Value Char", description="")
    new_value_text: Optional[Any] = Field(None, alias="new_value_text", title="New Value Text", description="")
    new_value_datetime: Optional[str] = Field(None, alias="new_value_datetime", title="New Value Datetime", description="")
    display_name: Optional[str] = Field(None, alias="display_name", title="Display Name", description="")
    create_uid: Optional[int] = Field(None, alias="create_uid", title="Created by", description="")
    create_date: Optional[str] = Field(None, alias="create_date", title="Created on", description="")
    write_uid: Optional[int] = Field(None, alias="write_uid", title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, alias="write_date", title="Last Updated on", description="")

    class ConfigDict:
        from_attributes = True

    @classmethod
    def from_execute_kw(cls, item:dict[str, any]) -> 'MailTrackingValueModel':
        filtered_item = {}
        schema = MailTrackingValueModel.model_json_schema()

        for key, value in item.items():
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
    def list_from_execute_kw(cls, data:List[dict], fields:List[str] = []) -> List['MailTrackingValueModel']:
        transformed = []
        schema = MailTrackingValueModel.model_json_schema()
        
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
