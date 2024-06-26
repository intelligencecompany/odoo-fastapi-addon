
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class PaymentTransactionModel(BaseModel):
    id: Optional[int] = Field(None, alias="id", title="ID", description="")
    reference: str = Field("", alias="reference", title="Reference", description="The internal reference of the transaction")
    amount: float = Field(0.0, alias="amount", title="Amount", description="")
    state: Any = Field(None, alias="state", title="Status", description="")
    provider_id: int = Field(0, alias="provider_id", title="Provider", description="")
    company_id: Optional[int] = Field(None, alias="company_id", title="Company", description="")
    payment_method_id: int = Field(0, alias="payment_method_id", title="Payment Method", description="")
    currency_id: int = Field(0, alias="currency_id", title="Currency", description="")
    token_id: Optional[int] = Field(None, alias="token_id", title="Payment Token", description="")
    source_transaction_id: Optional[int] = Field(None, alias="source_transaction_id", title="Source Transaction", description="The source transaction of the related child transactions")
    callback_model_id: Optional[int] = Field(None, alias="callback_model_id", title="Callback Document Model", description="")
    callback_res_id: Optional[int] = Field(None, alias="callback_res_id", title="Callback Record ID", description="")
    partner_id: int = Field(0, alias="partner_id", title="Customer", description="")
    partner_state_id: Optional[int] = Field(None, alias="partner_state_id", title="State", description="")
    partner_country_id: Optional[int] = Field(None, alias="partner_country_id", title="Country", description="")
    child_transaction_ids: Optional[List[int]] = Field(None, alias="child_transaction_ids", title="Child Transactions", description="The child transactions of the transaction.")
    provider_code: Optional[Any] = Field(None, alias="provider_code", title="Provider Code", description="The technical code of this payment provider.")
    payment_method_code: Optional[str] = Field(None, alias="payment_method_code", title="Payment Method Code", description="The technical code of this payment method.")
    provider_reference: Optional[str] = Field(None, alias="provider_reference", title="Provider Reference", description="The provider reference of the transaction")
    state_message: Optional[Any] = Field(None, alias="state_message", title="Message", description="The complementary information message about the state")
    last_state_change: Optional[str] = Field(None, alias="last_state_change", title="Last State Change Date", description="")
    operation: Optional[Any] = Field(None, alias="operation", title="Operation", description="")
    refunds_count: Optional[int] = Field(None, alias="refunds_count", title="Refunds Count", description="")
    is_post_processed: Optional[bool] = Field(None, alias="is_post_processed", title="Is Post-processed", description="Has the payment been post-processed")
    tokenize: Optional[bool] = Field(None, alias="tokenize", title="Create Token", description="Whether a payment token should be created when post-processing the transaction")
    landing_route: Optional[str] = Field(None, alias="landing_route", title="Landing Route", description="The route the user is redirected to after the transaction")
    callback_method: Optional[str] = Field(None, alias="callback_method", title="Callback Method", description="")
    callback_hash: Optional[str] = Field(None, alias="callback_hash", title="Callback Hash", description="")
    callback_is_done: Optional[bool] = Field(None, alias="callback_is_done", title="Callback Done", description="Whether the callback has already been executed")
    partner_name: Optional[str] = Field(None, alias="partner_name", title="Partner Name", description="")
    partner_lang: Optional[Any] = Field(None, alias="partner_lang", title="Language", description="")
    partner_email: Optional[str] = Field(None, alias="partner_email", title="Email", description="")
    partner_address: Optional[str] = Field(None, alias="partner_address", title="Address", description="")
    partner_zip: Optional[str] = Field(None, alias="partner_zip", title="Zip", description="")
    partner_city: Optional[str] = Field(None, alias="partner_city", title="City", description="")
    partner_phone: Optional[str] = Field(None, alias="partner_phone", title="Phone", description="")
    display_name: Optional[str] = Field(None, alias="display_name", title="Display Name", description="")
    create_uid: Optional[int] = Field(None, alias="create_uid", title="Created by", description="")
    create_date: Optional[str] = Field(None, alias="create_date", title="Created on", description="")
    write_uid: Optional[int] = Field(None, alias="write_uid", title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, alias="write_date", title="Last Updated on", description="")

    class ConfigDict:
        from_attributes = True

    @classmethod
    def from_execute_kw(cls, item:dict) -> 'PaymentTransactionModel':
        filtered_item = {}
        schema = PaymentTransactionModel.model_json_schema()

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
    def list_from_execute_kw(cls, data:List[dict], fields:List[str] = []) -> List['PaymentTransactionModel']:
        transformed = []
        schema = PaymentTransactionModel.model_json_schema()
        
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
