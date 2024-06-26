
from pydantic import BaseModel, Field
from typing import Optional, List, Any, Dict

class CurrencyModel(BaseModel):
    id: Optional[int] = Field(None, alias="id", title="ID", description="")
    name: str = Field("", alias="name", title="Currency", description="Currency Code (ISO 4217)")
    symbol: str = Field("", alias="symbol", title="Symbol", description="Currency sign, to be used when printing amounts.")
    rate_ids: Optional[List[int]] = Field(None, alias="rate_ids", title="Rates", description="")
    full_name: Optional[str] = Field(None, alias="full_name", title="Name", description="")
    rate: Optional[Any] = Field(None, alias="rate", title="Current Rate", description="The rate of the currency to the currency of rate 1.")
    inverse_rate: Optional[Any] = Field(None, alias="inverse_rate", title="Inverse Rate", description="The currency of rate 1 to the rate of the currency.")
    rate_string: Optional[str] = Field(None, alias="rate_string", title="Rate String", description="")
    rounding: Optional[Any] = Field(None, alias="rounding", title="Rounding Factor", description="Amounts in this currency are rounded off to the nearest multiple of the rounding factor.")
    decimal_places: Optional[int] = Field(None, alias="decimal_places", title="Decimal Places", description="Decimal places taken into account for operations on amounts in this currency. It is determined by the rounding factor.")
    active: Optional[bool] = Field(None, alias="active", title="Active", description="")
    position: Optional[Any] = Field(None, alias="position", title="Symbol Position", description="Determines where the currency symbol should be placed after or before the amount.")
    date: Optional[str] = Field(None, alias="date", title="Date", description="")
    currency_unit_label: Optional[str] = Field(None, alias="currency_unit_label", title="Currency Unit", description="")
    currency_subunit_label: Optional[str] = Field(None, alias="currency_subunit_label", title="Currency Subunit", description="")
    is_current_company_currency: Optional[bool] = Field(None, alias="is_current_company_currency", title="Is Current Company Currency", description="")
    display_name: Optional[str] = Field(None, alias="display_name", title="Display Name", description="")
    create_uid: Optional[int] = Field(None, alias="create_uid", title="Created by", description="")
    create_date: Optional[str] = Field(None, alias="create_date", title="Created on", description="")
    write_uid: Optional[int] = Field(None, alias="write_uid", title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, alias="write_date", title="Last Updated on", description="")

    class ConfigDict:
        from_attributes = True

    @classmethod
    def from_execute_kw(cls, item:Dict[str, Any]) -> 'CurrencyModel':
        filtered_item = {}
        schema = CurrencyModel.model_json_schema()

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
    def list_from_execute_kw(cls, data:List[dict], fields:List[str] = []) -> List['CurrencyModel']:
        transformed = []
        schema = CurrencyModel.model_json_schema()
        
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
