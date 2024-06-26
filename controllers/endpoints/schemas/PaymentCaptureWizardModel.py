
from pydantic import BaseModel, Field
from typing import Optional, List, Any, Dict

class PaymentCaptureWizardModel(BaseModel):
    id: Optional[int] = Field(None, alias="id", title="ID", description="")
    currency_id: Optional[int] = Field(None, alias="currency_id", title="Currency", description="")
    transaction_ids: Optional[List[int]] = Field(None, alias="transaction_ids", title="Transaction", description="")
    authorized_amount: Optional[float] = Field(None, alias="authorized_amount", title="Authorized Amount", description="")
    captured_amount: Optional[float] = Field(None, alias="captured_amount", title="Already Captured", description="")
    voided_amount: Optional[float] = Field(None, alias="voided_amount", title="Already Voided", description="")
    available_amount: Optional[float] = Field(None, alias="available_amount", title="Maximum Capture Allowed", description="")
    amount_to_capture: Optional[float] = Field(None, alias="amount_to_capture", title="Amount To Capture", description="")
    is_amount_to_capture_valid: Optional[bool] = Field(None, alias="is_amount_to_capture_valid", title="Is Amount To Capture Valid", description="")
    void_remaining_amount: Optional[bool] = Field(None, alias="void_remaining_amount", title="Void Remaining Amount", description="")
    support_partial_capture: Optional[bool] = Field(None, alias="support_partial_capture", title="Support Partial Capture", description="Whether each of the transactions' provider supports the partial capture.")
    has_draft_children: Optional[bool] = Field(None, alias="has_draft_children", title="Has Draft Children", description="")
    has_remaining_amount: Optional[bool] = Field(None, alias="has_remaining_amount", title="Has Remaining Amount", description="")
    display_name: Optional[str] = Field(None, alias="display_name", title="Display Name", description="")
    create_uid: Optional[int] = Field(None, alias="create_uid", title="Created by", description="")
    create_date: Optional[str] = Field(None, alias="create_date", title="Created on", description="")
    write_uid: Optional[int] = Field(None, alias="write_uid", title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, alias="write_date", title="Last Updated on", description="")

    class ConfigDict:
        from_attributes = True

    @classmethod
    def from_execute_kw(cls, item:Dict[str, Any]) -> 'PaymentCaptureWizardModel':
        filtered_item = {}
        schema = PaymentCaptureWizardModel.model_json_schema()

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
    def list_from_execute_kw(cls, data:List[dict], fields:List[str] = []) -> List['PaymentCaptureWizardModel']:
        transformed = []
        schema = PaymentCaptureWizardModel.model_json_schema()
        
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
