
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class CountryModel(BaseModel):
    id: Optional[int] = Field(None, alias="id", title="ID", description="")
    name: str = Field("", alias="name", title="Country Name", description="")
    code: str = Field("", alias="code", title="Country Code", description="The ISO country code in two chars. \nYou can use this field for quick search.")
    address_view_id: Optional[int] = Field(None, alias="address_view_id", title="Input View", description="Use this field if you want to replace the usual way to encode a complete address. Note that the address_format field is used to modify the way to display addresses (in reports for example), while this field is used to modify the input form for addresses.")
    currency_id: Optional[int] = Field(None, alias="currency_id", title="Currency", description="")
    country_group_ids: Optional[List[int]] = Field(None, alias="country_group_ids", title="Country Groups", description="")
    state_ids: Optional[List[int]] = Field(None, alias="state_ids", title="States", description="")
    address_format: Optional[Any] = Field(None, alias="address_format", title="Layout in Reports", description="Display format to use for addresses belonging to this country.\n\nYou can use python-style string pattern with all the fields of the address (for example, use '%(street)s' to display the field 'street') plus\n%(state_name)s: the name of the state\n%(state_code)s: the code of the state\n%(country_name)s: the name of the country\n%(country_code)s: the code of the country")
    image_url: Optional[str] = Field(None, alias="image_url", title="Flag", description="Url of static flag image")
    phone_code: Optional[int] = Field(None, alias="phone_code", title="Country Calling Code", description="")
    name_position: Optional[Any] = Field(None, alias="name_position", title="Customer Name Position", description="Determines where the customer/company name should be placed, i.e. after or before the address.")
    vat_label: Optional[str] = Field(None, alias="vat_label", title="Vat Label", description="Use this field if you want to change vat label.")
    state_required: Optional[bool] = Field(None, alias="state_required", title="State Required", description="")
    zip_required: Optional[bool] = Field(None, alias="zip_required", title="Zip Required", description="")
    display_name: Optional[str] = Field(None, alias="display_name", title="Display Name", description="")
    create_uid: Optional[int] = Field(None, alias="create_uid", title="Created by", description="")
    create_date: Optional[str] = Field(None, alias="create_date", title="Created on", description="")
    write_uid: Optional[int] = Field(None, alias="write_uid", title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, alias="write_date", title="Last Updated on", description="")

    class Config:
        from_attributes = True

    @classmethod
    def from_execute_kw(cls, data:List[dict], fields:List[str] = []) -> List['CountryModel']:
        transformed = []
        schema = CountryModel.model_json_schema()
        
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
