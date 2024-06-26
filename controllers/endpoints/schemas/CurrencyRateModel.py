
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class CurrencyRateModel(BaseModel):
    id: Optional[int] = Field(None, alias="id", title="ID", description="")
    name: str = Field("", alias="name", title="Date", description="")
    currency_id: int = Field(0, alias="currency_id", title="Currency", description="")
    company_id: Optional[int] = Field(None, alias="company_id", title="Company", description="")
    rate: Optional[Any] = Field(None, alias="rate", title="Technical Rate", description="The rate of the currency to the currency of rate 1")
    company_rate: Optional[Any] = Field(None, alias="company_rate", title="Company Rate", description="The currency of rate 1 to the rate of the currency.")
    inverse_company_rate: Optional[Any] = Field(None, alias="inverse_company_rate", title="Inverse Company Rate", description="The rate of the currency to the currency of rate 1")
    display_name: Optional[str] = Field(None, alias="display_name", title="Display Name", description="")
    create_uid: Optional[int] = Field(None, alias="create_uid", title="Created by", description="")
    create_date: Optional[str] = Field(None, alias="create_date", title="Created on", description="")
    write_uid: Optional[int] = Field(None, alias="write_uid", title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, alias="write_date", title="Last Updated on", description="")

    class Config:
        from_attributes = True

    @classmethod
    def from_execute_kw(cls, data:List[dict], fields:List[str] = []) -> List['CurrencyRateModel']:
        transformed = []
        schema = CurrencyRateModel.model_json_schema()
        
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
