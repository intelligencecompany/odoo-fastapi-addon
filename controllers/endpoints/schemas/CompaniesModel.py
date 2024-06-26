
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class CompaniesModel(BaseModel):
    id: Optional[int] = Field(None, alias="id", title="ID", description="")
    name: str = Field("", alias="name", title="Company Name", description="")
    layout_background: Any = Field(None, alias="layout_background", title="Layout Background", description="")
    parent_id: Optional[int] = Field(None, alias="parent_id", title="Parent Company", description="")
    root_id: Optional[int] = Field(None, alias="root_id", title="Root", description="")
    partner_id: int = Field(0, alias="partner_id", title="Partner", description="")
    currency_id: int = Field(0, alias="currency_id", title="Currency", description="")
    state_id: Optional[int] = Field(None, alias="state_id", title="Fed. State", description="")
    country_id: Optional[int] = Field(None, alias="country_id", title="Country", description="")
    paperformat_id: Optional[int] = Field(None, alias="paperformat_id", title="Paper format", description="")
    external_report_layout_id: Optional[int] = Field(None, alias="external_report_layout_id", title="Document Template", description="")
    nomenclature_id: Optional[int] = Field(None, alias="nomenclature_id", title="Nomenclature", description="")
    resource_calendar_id: Optional[int] = Field(None, alias="resource_calendar_id", title="Default Working Hours", description="")
    alias_domain_id: Optional[int] = Field(None, alias="alias_domain_id", title="Email Domain", description="")
    website_id: Optional[int] = Field(None, alias="website_id", title="Website", description="")
    child_ids: Optional[List[int]] = Field(None, alias="child_ids", title="Branches", description="")
    all_child_ids: Optional[List[int]] = Field(None, alias="all_child_ids", title="All Child", description="")
    parent_ids: Optional[List[int]] = Field(None, alias="parent_ids", title="Parent", description="")
    user_ids: Optional[List[int]] = Field(None, alias="user_ids", title="Accepted Users", description="")
    bank_ids: Optional[List[int]] = Field(None, alias="bank_ids", title="Banks", description="")
    resource_calendar_ids: Optional[List[int]] = Field(None, alias="resource_calendar_ids", title="Working Hours", description="")
    active: Optional[bool] = Field(None, alias="active", title="Active", description="")
    sequence: Optional[int] = Field(None, alias="sequence", title="Sequence", description="Used to order Companies in the company switcher")
    parent_path: Optional[str] = Field(None, alias="parent_path", title="Parent Path", description="")
    report_header: Optional[Any] = Field(None, alias="report_header", title="Company Tagline", description="Company tagline, which is included in a printed document's header or footer (depending on the selected layout).")
    report_footer: Optional[Any] = Field(None, alias="report_footer", title="Report Footer", description="Footer text displayed at the bottom of all reports.")
    company_details: Optional[Any] = Field(None, alias="company_details", title="Company Details", description="Header text displayed at the top of all reports.")
    is_company_details_empty: Optional[bool] = Field(None, alias="is_company_details_empty", title="Is Company Details Empty", description="")
    logo: Optional[Any] = Field(None, alias="logo", title="Company Logo", description="")
    logo_web: Optional[Any] = Field(None, alias="logo_web", title="Logo Web", description="")
    uses_default_logo: Optional[bool] = Field(None, alias="uses_default_logo", title="Uses Default Logo", description="")
    street: Optional[str] = Field(None, alias="street", title="Street", description="")
    street2: Optional[str] = Field(None, alias="street2", title="Street2", description="")
    zip: Optional[str] = Field(None, alias="zip", title="Zip", description="")
    city: Optional[str] = Field(None, alias="city", title="City", description="")
    email: Optional[str] = Field(None, alias="email", title="Email", description="")
    phone: Optional[str] = Field(None, alias="phone", title="Phone", description="")
    mobile: Optional[str] = Field(None, alias="mobile", title="Mobile", description="")
    website: Optional[str] = Field(None, alias="website", title="Website Link", description="")
    vat: Optional[str] = Field(None, alias="vat", title="Tax ID", description="The Tax Identification Number. Values here will be validated based on the country format. You can use '/' to indicate that the partner is not subject to tax.")
    company_registry: Optional[str] = Field(None, alias="company_registry", title="Company ID", description="The registry number of the company. Use it if it is different from the Tax ID. It must be unique across all partners of a same country")
    font: Optional[Any] = Field(None, alias="font", title="Font", description="")
    primary_color: Optional[str] = Field(None, alias="primary_color", title="Primary Color", description="")
    secondary_color: Optional[str] = Field(None, alias="secondary_color", title="Secondary Color", description="")
    color: Optional[int] = Field(None, alias="color", title="Color", description="")
    layout_background_image: Optional[Any] = Field(None, alias="layout_background_image", title="Background Image", description="")
    display_name: Optional[str] = Field(None, alias="display_name", title="Display Name", description="")
    create_uid: Optional[int] = Field(None, alias="create_uid", title="Created by", description="")
    create_date: Optional[str] = Field(None, alias="create_date", title="Created on", description="")
    write_uid: Optional[int] = Field(None, alias="write_uid", title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, alias="write_date", title="Last Updated on", description="")
    social_twitter: Optional[str] = Field(None, alias="social_twitter", title="Twitter Account", description="")
    social_facebook: Optional[str] = Field(None, alias="social_facebook", title="Facebook Account", description="")
    social_github: Optional[str] = Field(None, alias="social_github", title="GitHub Account", description="")
    social_linkedin: Optional[str] = Field(None, alias="social_linkedin", title="LinkedIn Account", description="")
    social_youtube: Optional[str] = Field(None, alias="social_youtube", title="Youtube Account", description="")
    social_instagram: Optional[str] = Field(None, alias="social_instagram", title="Instagram Account", description="")
    social_tiktok: Optional[str] = Field(None, alias="social_tiktok", title="TikTok Account", description="")
    alias_domain_name: Optional[str] = Field(None, alias="alias_domain_name", title="Alias Domain Name", description="Email domain e.g. 'example.com' in 'odoo@example.com'")
    bounce_email: Optional[str] = Field(None, alias="bounce_email", title="Bounce Email", description="")
    bounce_formatted: Optional[str] = Field(None, alias="bounce_formatted", title="Bounce", description="")
    catchall_email: Optional[str] = Field(None, alias="catchall_email", title="Catchall Email", description="")
    catchall_formatted: Optional[str] = Field(None, alias="catchall_formatted", title="Catchall", description="")
    default_from_email: Optional[str] = Field(None, alias="default_from_email", title="Default From", description="")
    email_formatted: Optional[str] = Field(None, alias="email_formatted", title="Formatted Email", description="")
    email_primary_color: Optional[str] = Field(None, alias="email_primary_color", title="Email Header Color", description="")
    email_secondary_color: Optional[str] = Field(None, alias="email_secondary_color", title="Email Button Color", description="")
    partner_gid: Optional[int] = Field(None, alias="partner_gid", title="Company database ID", description="")
    iap_enrich_auto_done: Optional[bool] = Field(None, alias="iap_enrich_auto_done", title="Enrich Done", description="")
    snailmail_color: Optional[bool] = Field(None, alias="snailmail_color", title="Snailmail Color", description="")
    snailmail_cover: Optional[bool] = Field(None, alias="snailmail_cover", title="Add a Cover Page", description="")
    snailmail_duplex: Optional[bool] = Field(None, alias="snailmail_duplex", title="Both sides", description="")
    payment_onboarding_payment_method: Optional[Any] = Field(None, alias="payment_onboarding_payment_method", title="Selected onboarding payment method", description="")

    class ConfigDict:
        from_attributes = True

    @classmethod
    def from_execute_kw(cls, data:List[dict], fields:List[str] = []) -> List['CompaniesModel']:
        transformed = []
        schema = CompaniesModel.model_json_schema()
        
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
