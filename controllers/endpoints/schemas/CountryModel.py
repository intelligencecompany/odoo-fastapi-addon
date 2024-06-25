
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class CountryModel(BaseModel):
    id: Optional[int] = Field(None, title="ID", description="")
    name: str = Field("", title="Country Name", description="")
    code: str = Field("", title="Country Code", description="The ISO country code in two chars. \nYou can use this field for quick search.")
    address_view_id: Optional[int] = Field(None, title="Input View", description="Use this field if you want to replace the usual way to encode a complete address. Note that the address_format field is used to modify the way to display addresses (in reports for example), while this field is used to modify the input form for addresses.")
    currency_id: Optional[int] = Field(None, title="Currency", description="")
    country_group_ids: Optional[List[int]] = Field(None, title="Country Groups", description="")
    state_ids: Optional[List[int]] = Field(None, title="States", description="")
    address_format: Optional[Any] = Field(None, title="Layout in Reports", description="Display format to use for addresses belonging to this country.\n\nYou can use python-style string pattern with all the fields of the address (for example, use '%(street)s' to display the field 'street') plus\n%(state_name)s: the name of the state\n%(state_code)s: the code of the state\n%(country_name)s: the name of the country\n%(country_code)s: the code of the country")
    image_url: Optional[str] = Field(None, title="Flag", description="Url of static flag image")
    phone_code: Optional[int] = Field(None, title="Country Calling Code", description="")
    name_position: Optional[Any] = Field(None, title="Customer Name Position", description="Determines where the customer/company name should be placed, i.e. after or before the address.")
    vat_label: Optional[str] = Field(None, title="Vat Label", description="Use this field if you want to change vat label.")
    state_required: Optional[bool] = Field(None, title="State Required", description="")
    zip_required: Optional[bool] = Field(None, title="Zip Required", description="")
    display_name: Optional[str] = Field(None, title="Display Name", description="")
    create_uid: Optional[int] = Field(None, title="Created by", description="")
    create_date: Optional[str] = Field(None, title="Created on", description="")
    write_uid: Optional[int] = Field(None, title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, title="Last Updated on", description="")

