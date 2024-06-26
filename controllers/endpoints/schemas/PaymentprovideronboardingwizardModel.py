
from pydantic import BaseModel, Field
from typing import Optional, List, Any, Dict

class PaymentprovideronboardingwizardModel(BaseModel):
    id: Optional[int] = Field(None, alias="id", title="ID", description="")
    payment_method: Optional[Any] = Field(None, alias="payment_method", title="Payment Method", description="")
    paypal_email_account: Optional[str] = Field(None, alias="paypal_email_account", title="Email", description="")
    paypal_pdt_token: Optional[str] = Field(None, alias="paypal_pdt_token", title="PDT Identity Token", description="")
    manual_name: Optional[str] = Field(None, alias="manual_name", title="Method", description="")
    journal_name: Optional[str] = Field(None, alias="journal_name", title="Bank Name", description="")
    acc_number: Optional[str] = Field(None, alias="acc_number", title="Account Number", description="")
    manual_post_msg: Optional[Any] = Field(None, alias="manual_post_msg", title="Payment Instructions", description="")
    display_name: Optional[str] = Field(None, alias="display_name", title="Display Name", description="")
    create_uid: Optional[int] = Field(None, alias="create_uid", title="Created by", description="")
    create_date: Optional[str] = Field(None, alias="create_date", title="Created on", description="")
    write_uid: Optional[int] = Field(None, alias="write_uid", title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, alias="write_date", title="Last Updated on", description="")

    class ConfigDict:
        from_attributes = True

    @classmethod
    def from_execute_kw(cls, item:Dict[str, Any]) -> 'PaymentprovideronboardingwizardModel':
        filtered_item = {}
        schema = PaymentprovideronboardingwizardModel.model_json_schema()

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
    def list_from_execute_kw(cls, data:List[dict], fields:List[str] = []) -> List['PaymentprovideronboardingwizardModel']:
        transformed = []
        schema = PaymentprovideronboardingwizardModel.model_json_schema()
        
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
