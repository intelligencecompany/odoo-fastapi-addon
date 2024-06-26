
from pydantic import BaseModel, Field
from typing import Optional, List, Any, Dict

class PaymentMethodModel(BaseModel):
    id: Optional[int] = Field(None, alias="id", title="ID", description="")
    name: str = Field("", alias="name", title="Name", description="")
    code: str = Field("", alias="code", title="Code", description="The technical code of this payment method.")
    image: Any = Field(None, alias="image", title="Image", description="The base image used for this payment method; in a 64x64 px format.")
    primary_payment_method_id: Optional[int] = Field(None, alias="primary_payment_method_id", title="Primary Payment Method", description="The primary payment method of the current payment method, if the latter is a brand.\nFor example, \"Card\" is the primary payment method of the card brand \"VISA\".")
    brand_ids: Optional[List[int]] = Field(None, alias="brand_ids", title="Brands", description="The brands of the payment methods that will be displayed on the payment form.")
    provider_ids: Optional[List[int]] = Field(None, alias="provider_ids", title="Providers", description="The list of providers supporting this payment method.")
    supported_country_ids: Optional[List[int]] = Field(None, alias="supported_country_ids", title="Supported Countries", description="The list of countries in which this payment method can be used (if the provider allows it). In other countries, this payment method is not available to customers.")
    supported_currency_ids: Optional[List[int]] = Field(None, alias="supported_currency_ids", title="Supported Currencies", description="The list of currencies for that are supported by this payment method (if the provider allows it). When paying with another currency, this payment method is not available to customers.")
    sequence: Optional[int] = Field(None, alias="sequence", title="Sequence", description="")
    is_primary: Optional[bool] = Field(None, alias="is_primary", title="Is Primary Payment Method", description="")
    active: Optional[bool] = Field(None, alias="active", title="Active", description="")
    image_payment_form: Optional[Any] = Field(None, alias="image_payment_form", title="The resized image displayed on the payment form.", description="The base image used for this payment method; in a 64x64 px format.")
    support_tokenization: Optional[bool] = Field(None, alias="support_tokenization", title="Tokenization Supported", description="Tokenization is the process of saving the payment details as a token that can later be reused without having to enter the payment details again.")
    support_express_checkout: Optional[bool] = Field(None, alias="support_express_checkout", title="Express Checkout Supported", description="Express checkout allows customers to pay faster by using a payment method that provides all required billing and shipping information, thus allowing to skip the checkout process.")
    support_refund: Optional[Any] = Field(None, alias="support_refund", title="Type of Refund Supported", description="Refund is a feature allowing to refund customers directly from the payment in Odoo.")
    display_name: Optional[str] = Field(None, alias="display_name", title="Display Name", description="")
    create_uid: Optional[int] = Field(None, alias="create_uid", title="Created by", description="")
    create_date: Optional[str] = Field(None, alias="create_date", title="Created on", description="")
    write_uid: Optional[int] = Field(None, alias="write_uid", title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, alias="write_date", title="Last Updated on", description="")

    class ConfigDict:
        from_attributes = True

    @classmethod
    def from_execute_kw(cls, item:dict) -> 'PaymentMethodModel':
        filtered_item = {}
        schema = PaymentMethodModel.model_json_schema()

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
    def list_from_execute_kw(cls, data:List[dict], fields:List[str] = []) -> List['PaymentMethodModel']:
        transformed = []
        schema = PaymentMethodModel.model_json_schema()
        
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
