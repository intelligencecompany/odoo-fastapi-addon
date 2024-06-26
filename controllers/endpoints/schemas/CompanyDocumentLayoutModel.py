
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class CompanyDocumentLayoutModel(BaseModel):
    id: Optional[int] = Field(None, alias="id", title="ID", description="")
    company_id: int = Field(0, alias="company_id", title="Company", description="")
    paperformat_id: Optional[int] = Field(None, alias="paperformat_id", title="Paper format", description="")
    external_report_layout_id: Optional[int] = Field(None, alias="external_report_layout_id", title="Document Template", description="")
    report_layout_id: Optional[int] = Field(None, alias="report_layout_id", title="Report Layout", description="")
    partner_id: Optional[int] = Field(None, alias="partner_id", title="Partner", description="")
    country_id: Optional[int] = Field(None, alias="country_id", title="Country", description="")
    logo: Optional[Any] = Field(None, alias="logo", title="Company Logo", description="")
    preview_logo: Optional[Any] = Field(None, alias="preview_logo", title="Preview logo", description="")
    report_header: Optional[Any] = Field(None, alias="report_header", title="Company Tagline", description="Company tagline, which is included in a printed document's header or footer (depending on the selected layout).")
    report_footer: Optional[Any] = Field(None, alias="report_footer", title="Report Footer", description="Footer text displayed at the bottom of all reports.")
    company_details: Optional[Any] = Field(None, alias="company_details", title="Company Details", description="Header text displayed at the top of all reports.")
    is_company_details_empty: Optional[bool] = Field(None, alias="is_company_details_empty", title="Is Company Details Empty", description="")
    font: Optional[Any] = Field(None, alias="font", title="Font", description="")
    primary_color: Optional[str] = Field(None, alias="primary_color", title="Primary Color", description="")
    secondary_color: Optional[str] = Field(None, alias="secondary_color", title="Secondary Color", description="")
    custom_colors: Optional[bool] = Field(None, alias="custom_colors", title="Custom Colors", description="")
    logo_primary_color: Optional[str] = Field(None, alias="logo_primary_color", title="Logo Primary Color", description="")
    logo_secondary_color: Optional[str] = Field(None, alias="logo_secondary_color", title="Logo Secondary Color", description="")
    layout_background: Optional[Any] = Field(None, alias="layout_background", title="Layout Background", description="")
    layout_background_image: Optional[Any] = Field(None, alias="layout_background_image", title="Background Image", description="")
    preview: Optional[Any] = Field(None, alias="preview", title="Preview", description="")
    phone: Optional[str] = Field(None, alias="phone", title="Phone", description="")
    email: Optional[str] = Field(None, alias="email", title="Email", description="")
    website: Optional[str] = Field(None, alias="website", title="Website Link", description="")
    vat: Optional[str] = Field(None, alias="vat", title="Tax ID", description="The Tax Identification Number. Values here will be validated based on the country format. You can use '/' to indicate that the partner is not subject to tax.")
    name: Optional[str] = Field(None, alias="name", title="Company Name", description="")
    display_name: Optional[str] = Field(None, alias="display_name", title="Display Name", description="")
    create_uid: Optional[int] = Field(None, alias="create_uid", title="Created by", description="")
    create_date: Optional[str] = Field(None, alias="create_date", title="Created on", description="")
    write_uid: Optional[int] = Field(None, alias="write_uid", title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, alias="write_date", title="Last Updated on", description="")

    class Config:
        from_attributes = True

    @classmethod
    def from_execute_kw(cls, data:List[dict], fields:List[str] = []) -> List['CompanyDocumentLayoutModel']:
        transformed = []
        schema = CompanyDocumentLayoutModel.model_json_schema()
        
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
