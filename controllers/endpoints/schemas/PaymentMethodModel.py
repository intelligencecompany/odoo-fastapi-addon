
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class PaymentMethodModel(BaseModel):
    id: Optional[int] = Field(None, title="ID", description="")
    name: str = Field("", title="Name", description="")
    code: str = Field("", title="Code", description="The technical code of this payment method.")
    image: Any = Field(None, title="Image", description="The base image used for this payment method; in a 64x64 px format.")
    primary_payment_method_id: Optional[int] = Field(None, title="Primary Payment Method", description="The primary payment method of the current payment method, if the latter is a brand.\nFor example, \"Card\" is the primary payment method of the card brand \"VISA\".")
    brand_ids: Optional[List[int]] = Field(None, title="Brands", description="The brands of the payment methods that will be displayed on the payment form.")
    provider_ids: Optional[List[int]] = Field(None, title="Providers", description="The list of providers supporting this payment method.")
    supported_country_ids: Optional[List[int]] = Field(None, title="Supported Countries", description="The list of countries in which this payment method can be used (if the provider allows it). In other countries, this payment method is not available to customers.")
    supported_currency_ids: Optional[List[int]] = Field(None, title="Supported Currencies", description="The list of currencies for that are supported by this payment method (if the provider allows it). When paying with another currency, this payment method is not available to customers.")
    sequence: Optional[int] = Field(None, title="Sequence", description="")
    is_primary: Optional[bool] = Field(None, title="Is Primary Payment Method", description="")
    active: Optional[bool] = Field(None, title="Active", description="")
    image_payment_form: Optional[Any] = Field(None, title="The resized image displayed on the payment form.", description="The base image used for this payment method; in a 64x64 px format.")
    support_tokenization: Optional[bool] = Field(None, title="Tokenization Supported", description="Tokenization is the process of saving the payment details as a token that can later be reused without having to enter the payment details again.")
    support_express_checkout: Optional[bool] = Field(None, title="Express Checkout Supported", description="Express checkout allows customers to pay faster by using a payment method that provides all required billing and shipping information, thus allowing to skip the checkout process.")
    support_refund: Optional[Any] = Field(None, title="Type of Refund Supported", description="Refund is a feature allowing to refund customers directly from the payment in Odoo.")
    display_name: Optional[str] = Field(None, title="Display Name", description="")
    create_uid: Optional[int] = Field(None, title="Created by", description="")
    create_date: Optional[str] = Field(None, title="Created on", description="")
    write_uid: Optional[int] = Field(None, title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, title="Last Updated on", description="")

