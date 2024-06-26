
from pydantic import BaseModel, Field
from typing import Optional, List, Any, Dict

class PaymentProviderModel(BaseModel):
    id: Optional[int] = Field(None, alias="id", title="ID", description="")
    name: str = Field("", alias="name", title="Name", description="")
    code: Any = Field(None, alias="code", title="Code", description="The technical code of this payment provider.")
    state: Any = Field(None, alias="state", title="State", description="In test mode, a fake payment is processed through a test payment interface.\nThis mode is advised when setting up the provider.")
    company_id: int = Field(0, alias="company_id", title="Company", description="")
    main_currency_id: Optional[int] = Field(None, alias="main_currency_id", title="Currency", description="The main currency of the company, used to display monetary fields.")
    redirect_form_view_id: Optional[int] = Field(None, alias="redirect_form_view_id", title="Redirect Form Template", description="The template rendering a form submitted to redirect the user when making a payment")
    inline_form_view_id: Optional[int] = Field(None, alias="inline_form_view_id", title="Inline Form Template", description="The template rendering the inline payment form when making a direct payment")
    token_inline_form_view_id: Optional[int] = Field(None, alias="token_inline_form_view_id", title="Token Inline Form Template", description="The template rendering the inline payment form when making a payment by token.")
    express_checkout_form_view_id: Optional[int] = Field(None, alias="express_checkout_form_view_id", title="Express Checkout Form Template", description="The template rendering the express payment methods' form.")
    module_id: Optional[int] = Field(None, alias="module_id", title="Corresponding Module", description="")
    payment_method_ids: Optional[List[int]] = Field(None, alias="payment_method_ids", title="Supported Payment Methods", description="")
    available_country_ids: Optional[List[int]] = Field(None, alias="available_country_ids", title="Countries", description="The countries in which this payment provider is available. Leave blank to make it available in all countries.")
    available_currency_ids: Optional[List[int]] = Field(None, alias="available_currency_ids", title="Currencies", description="The currencies available with this payment provider. Leave empty not to restrict any.")
    sequence: Optional[int] = Field(None, alias="sequence", title="Sequence", description="Define the display order")
    is_published: Optional[bool] = Field(None, alias="is_published", title="Published", description="Whether the provider is visible on the website or not. Tokens remain functional but are only visible on manage forms.")
    allow_tokenization: Optional[bool] = Field(None, alias="allow_tokenization", title="Allow Saving Payment Methods", description="This controls whether customers can save their payment methods as payment tokens.\nA payment token is an anonymous link to the payment method details saved in the\nprovider's database, allowing the customer to reuse it for a next purchase.")
    capture_manually: Optional[bool] = Field(None, alias="capture_manually", title="Capture Amount Manually", description="Capture the amount from Odoo, when the delivery is completed.\nUse this if you want to charge your customers cards only when\nyou are sure you can ship the goods to them.")
    allow_express_checkout: Optional[bool] = Field(None, alias="allow_express_checkout", title="Allow Express Checkout", description="This controls whether customers can use express payment methods. Express checkout enables customers to pay with Google Pay and Apple Pay from which address information is collected at payment.")
    maximum_amount: Optional[float] = Field(None, alias="maximum_amount", title="Maximum Amount", description="The maximum payment amount that this payment provider is available for. Leave blank to make it available for any payment amount.")
    pre_msg: Optional[Any] = Field(None, alias="pre_msg", title="Help Message", description="The message displayed to explain and help the payment process")
    pending_msg: Optional[Any] = Field(None, alias="pending_msg", title="Pending Message", description="The message displayed if the order pending after the payment process")
    auth_msg: Optional[Any] = Field(None, alias="auth_msg", title="Authorize Message", description="The message displayed if payment is authorized")
    done_msg: Optional[Any] = Field(None, alias="done_msg", title="Done Message", description="The message displayed if the order is successfully done after the payment process")
    cancel_msg: Optional[Any] = Field(None, alias="cancel_msg", title="Canceled Message", description="The message displayed if the order is canceled during the payment process")
    support_tokenization: Optional[bool] = Field(None, alias="support_tokenization", title="Tokenization Supported", description="")
    support_manual_capture: Optional[Any] = Field(None, alias="support_manual_capture", title="Manual Capture Supported", description="")
    support_express_checkout: Optional[bool] = Field(None, alias="support_express_checkout", title="Express Checkout Supported", description="")
    support_refund: Optional[Any] = Field(None, alias="support_refund", title="Type of Refund Supported", description="")
    image_128: Optional[Any] = Field(None, alias="image_128", title="Image", description="")
    color: Optional[int] = Field(None, alias="color", title="Color", description="The color of the card in kanban view")
    module_state: Optional[Any] = Field(None, alias="module_state", title="Installation State", description="")
    module_to_buy: Optional[bool] = Field(None, alias="module_to_buy", title="Odoo Enterprise Module", description="")
    show_credentials_page: Optional[bool] = Field(None, alias="show_credentials_page", title="Show Credentials Page", description="")
    show_allow_tokenization: Optional[bool] = Field(None, alias="show_allow_tokenization", title="Show Allow Tokenization", description="")
    show_allow_express_checkout: Optional[bool] = Field(None, alias="show_allow_express_checkout", title="Show Allow Express Checkout", description="")
    show_pre_msg: Optional[bool] = Field(None, alias="show_pre_msg", title="Show Pre Msg", description="")
    show_pending_msg: Optional[bool] = Field(None, alias="show_pending_msg", title="Show Pending Msg", description="")
    show_auth_msg: Optional[bool] = Field(None, alias="show_auth_msg", title="Show Auth Msg", description="")
    show_done_msg: Optional[bool] = Field(None, alias="show_done_msg", title="Show Done Msg", description="")
    show_cancel_msg: Optional[bool] = Field(None, alias="show_cancel_msg", title="Show Cancel Msg", description="")
    require_currency: Optional[bool] = Field(None, alias="require_currency", title="Require Currency", description="")
    display_name: Optional[str] = Field(None, alias="display_name", title="Display Name", description="")
    create_uid: Optional[int] = Field(None, alias="create_uid", title="Created by", description="")
    create_date: Optional[str] = Field(None, alias="create_date", title="Created on", description="")
    write_uid: Optional[int] = Field(None, alias="write_uid", title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, alias="write_date", title="Last Updated on", description="")

    class ConfigDict:
        from_attributes = True

    @classmethod
    def from_execute_kw(cls, item:Dict[str, Any]) -> 'PaymentProviderModel':
        filtered_item = {}
        schema = PaymentProviderModel.model_json_schema()

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
    def list_from_execute_kw(cls, data:List[dict], fields:List[str] = []) -> List['PaymentProviderModel']:
        transformed = []
        schema = PaymentProviderModel.model_json_schema()
        
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
