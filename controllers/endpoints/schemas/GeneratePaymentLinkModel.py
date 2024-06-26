
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class GeneratePaymentLinkModel(BaseModel):
    id: Optional[int] = Field(None, alias="id", title="ID", description="")
    res_model: str = Field("", alias="res_model", title="Related Document Model", description="")
    amount: float = Field(0.0, alias="amount", title="Amount", description="")
    res_id: int = Field(0, alias="res_id", title="Related Document ID", description="")
    currency_id: Optional[int] = Field(None, alias="currency_id", title="Currency", description="")
    partner_id: Optional[int] = Field(None, alias="partner_id", title="Partner", description="")
    company_id: Optional[int] = Field(None, alias="company_id", title="Company", description="")
    amount_max: Optional[float] = Field(None, alias="amount_max", title="Amount Max", description="")
    partner_email: Optional[str] = Field(None, alias="partner_email", title="Email", description="")
    link: Optional[str] = Field(None, alias="link", title="Payment Link", description="")
    warning_message: Optional[str] = Field(None, alias="warning_message", title="Warning Message", description="")
    display_name: Optional[str] = Field(None, alias="display_name", title="Display Name", description="")
    create_uid: Optional[int] = Field(None, alias="create_uid", title="Created by", description="")
    create_date: Optional[str] = Field(None, alias="create_date", title="Created on", description="")
    write_uid: Optional[int] = Field(None, alias="write_uid", title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, alias="write_date", title="Last Updated on", description="")

    class Config:
        from_attributes = True

    @classmethod
    def from_execute_kw(cls, data:List[dict], fields:List[str] = []) -> List['GeneratePaymentLinkModel']:
        transformed = []
        schema = GeneratePaymentLinkModel.model_json_schema()
        
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
