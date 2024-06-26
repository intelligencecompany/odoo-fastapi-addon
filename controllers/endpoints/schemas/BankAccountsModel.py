
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class BankAccountsModel(BaseModel):
    id: Optional[int] = Field(None, alias="id", title="ID", description="")
    acc_number: str = Field("", alias="acc_number", title="Account Number", description="")
    partner_id: int = Field(0, alias="partner_id", title="Account Holder", description="")
    bank_id: Optional[int] = Field(None, alias="bank_id", title="Bank", description="")
    currency_id: Optional[int] = Field(None, alias="currency_id", title="Currency", description="")
    company_id: Optional[int] = Field(None, alias="company_id", title="Company", description="")
    active: Optional[bool] = Field(None, alias="active", title="Active", description="")
    acc_type: Optional[Any] = Field(None, alias="acc_type", title="Type", description="Bank account type: Normal or IBAN. Inferred from the bank account number.")
    sanitized_acc_number: Optional[str] = Field(None, alias="sanitized_acc_number", title="Sanitized Account Number", description="")
    acc_holder_name: Optional[str] = Field(None, alias="acc_holder_name", title="Account Holder Name", description="Account holder name, in case it is different than the name of the Account Holder")
    allow_out_payment: Optional[bool] = Field(None, alias="allow_out_payment", title="Send Money", description="This account can be used for outgoing payments")
    bank_name: Optional[str] = Field(None, alias="bank_name", title="Name", description="")
    bank_bic: Optional[str] = Field(None, alias="bank_bic", title="Bank Identifier Code", description="Sometimes called BIC or Swift.")
    sequence: Optional[int] = Field(None, alias="sequence", title="Sequence", description="")
    display_name: Optional[str] = Field(None, alias="display_name", title="Display Name", description="")
    create_uid: Optional[int] = Field(None, alias="create_uid", title="Created by", description="")
    create_date: Optional[str] = Field(None, alias="create_date", title="Created on", description="")
    write_uid: Optional[int] = Field(None, alias="write_uid", title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, alias="write_date", title="Last Updated on", description="")

    class ConfigDict:
        from_attributes = True

    @classmethod
    def from_execute_kw(cls, data:List[dict], fields:List[str] = []) -> List['BankAccountsModel']:
        transformed = []
        schema = BankAccountsModel.model_json_schema()
        
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
