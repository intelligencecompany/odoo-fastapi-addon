
from pydantic import BaseModel, Field
from typing import Optional, List, Any, Dict

class PaymentTokenModel(BaseModel):
    id: Optional[int] = Field(None, alias="id", title="ID", description="")
    provider_ref: str = Field("", alias="provider_ref", title="Provider Reference", description="The provider reference of the token of the transaction.")
    provider_id: int = Field(0, alias="provider_id", title="Provider", description="")
    company_id: Optional[int] = Field(None, alias="company_id", title="Company", description="")
    payment_method_id: int = Field(0, alias="payment_method_id", title="Payment Method", description="")
    partner_id: int = Field(0, alias="partner_id", title="Partner", description="")
    transaction_ids: Optional[List[int]] = Field(None, alias="transaction_ids", title="Payment Transactions", description="")
    provider_code: Optional[Any] = Field(None, alias="provider_code", title="Provider Code", description="The technical code of this payment provider.")
    payment_method_code: Optional[str] = Field(None, alias="payment_method_code", title="Payment Method Code", description="The technical code of this payment method.")
    payment_details: Optional[str] = Field(None, alias="payment_details", title="Payment Details", description="The clear part of the payment method's payment details.")
    active: Optional[bool] = Field(None, alias="active", title="Active", description="")
    display_name: Optional[str] = Field(None, alias="display_name", title="Display Name", description="")
    create_uid: Optional[int] = Field(None, alias="create_uid", title="Created by", description="")
    create_date: Optional[str] = Field(None, alias="create_date", title="Created on", description="")
    write_uid: Optional[int] = Field(None, alias="write_uid", title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, alias="write_date", title="Last Updated on", description="")

    class ConfigDict:
        from_attributes = True

    @classmethod
    def from_execute_kw(cls, item:Dict[str, Any]) -> 'PaymentTokenModel':
        filtered_item = {}
        schema = PaymentTokenModel.model_json_schema()

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
    def list_from_execute_kw(cls, data:List[dict], fields:List[str] = []) -> List['PaymentTokenModel']:
        transformed = []
        schema = PaymentTokenModel.model_json_schema()
        
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
