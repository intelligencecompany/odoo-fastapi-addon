
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class BankModel(BaseModel):
    id: Optional[int] = Field(None, alias="id", title="ID", description="")
    name: str = Field("", alias="name", title="Name", description="")
    street: Optional[str] = Field(None, alias="street", title="Street", description="")
    street2: Optional[str] = Field(None, alias="street2", title="Street2", description="")
    zip: Optional[str] = Field(None, alias="zip", title="Zip", description="")
    city: Optional[str] = Field(None, alias="city", title="City", description="")
    state: Optional[int] = Field(None, alias="state", title="Fed. State", description="")
    country: Optional[int] = Field(None, alias="country", title="Country", description="")
    email: Optional[str] = Field(None, alias="email", title="Email", description="")
    phone: Optional[str] = Field(None, alias="phone", title="Phone", description="")
    active: Optional[bool] = Field(None, alias="active", title="Active", description="")
    bic: Optional[str] = Field(None, alias="bic", title="Bank Identifier Code", description="Sometimes called BIC or Swift.")
    display_name: Optional[str] = Field(None, alias="display_name", title="Display Name", description="")
    create_uid: Optional[int] = Field(None, alias="create_uid", title="Created by", description="")
    create_date: Optional[str] = Field(None, alias="create_date", title="Created on", description="")
    write_uid: Optional[int] = Field(None, alias="write_uid", title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, alias="write_date", title="Last Updated on", description="")

    class Config:
        from_attributes = True

    @classmethod
    def from_execute_kw(cls, data:List[dict], fields:List[str] = []) -> List['BankModel']:
        transformed = []
        schema = BankModel.model_json_schema()
        
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