
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class CompanyDocumentLayoutModel(BaseModel):
    id: Optional[int] = Field(None, title="ID", description="")
    company_id: int = Field(0, title="Company", description="")
    paperformat_id: Optional[int] = Field(None, title="Paper format", description="")
    external_report_layout_id: Optional[int] = Field(None, title="Document Template", description="")
    report_layout_id: Optional[int] = Field(None, title="Report Layout", description="")
    partner_id: Optional[int] = Field(None, title="Partner", description="")
    country_id: Optional[int] = Field(None, title="Country", description="")
    logo: Optional[Any] = Field(None, title="Company Logo", description="")
    preview_logo: Optional[Any] = Field(None, title="Preview logo", description="")
    report_header: Optional[Any] = Field(None, title="Company Tagline", description="Company tagline, which is included in a printed document's header or footer (depending on the selected layout).")
    report_footer: Optional[Any] = Field(None, title="Report Footer", description="Footer text displayed at the bottom of all reports.")
    company_details: Optional[Any] = Field(None, title="Company Details", description="Header text displayed at the top of all reports.")
    is_company_details_empty: Optional[bool] = Field(None, title="Is Company Details Empty", description="")
    font: Optional[Any] = Field(None, title="Font", description="")
    primary_color: Optional[str] = Field(None, title="Primary Color", description="")
    secondary_color: Optional[str] = Field(None, title="Secondary Color", description="")
    custom_colors: Optional[bool] = Field(None, title="Custom Colors", description="")
    logo_primary_color: Optional[str] = Field(None, title="Logo Primary Color", description="")
    logo_secondary_color: Optional[str] = Field(None, title="Logo Secondary Color", description="")
    layout_background: Optional[Any] = Field(None, title="Layout Background", description="")
    layout_background_image: Optional[Any] = Field(None, title="Background Image", description="")
    preview: Optional[Any] = Field(None, title="Preview", description="")
    phone: Optional[str] = Field(None, title="Phone", description="")
    email: Optional[str] = Field(None, title="Email", description="")
    website: Optional[str] = Field(None, title="Website Link", description="")
    vat: Optional[str] = Field(None, title="Tax ID", description="The Tax Identification Number. Values here will be validated based on the country format. You can use '/' to indicate that the partner is not subject to tax.")
    name: Optional[str] = Field(None, title="Company Name", description="")
    display_name: Optional[str] = Field(None, title="Display Name", description="")
    create_uid: Optional[int] = Field(None, title="Created by", description="")
    create_date: Optional[str] = Field(None, title="Created on", description="")
    write_uid: Optional[int] = Field(None, title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, title="Last Updated on", description="")

