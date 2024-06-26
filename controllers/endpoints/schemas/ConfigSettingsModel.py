
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class ConfigSettingsModel(BaseModel):
    id: Optional[int] = Field(None, alias="id", title="ID", description="")
    company_id: int = Field(0, alias="company_id", title="Company", description="")
    external_report_layout_id: Optional[int] = Field(None, alias="external_report_layout_id", title="Document Template", description="")
    geoloc_provider_id: Optional[int] = Field(None, alias="geoloc_provider_id", title="API", description="")
    alias_domain_id: Optional[int] = Field(None, alias="alias_domain_id", title="Alias Domain", description="If you have setup a catch-all email domain redirected to the Odoo server, enter the domain name here.")
    auth_signup_template_user_id: Optional[int] = Field(None, alias="auth_signup_template_user_id", title="Template user for new users created through signup", description="")
    unsplash_app_id: Optional[str] = Field(None, alias="unsplash_app_id", title="Application ID", description="")
    digest_id: Optional[int] = Field(None, alias="digest_id", title="Digest Email", description="")
    website_id: Optional[int] = Field(None, alias="website_id", title="website", description="")
    website_company_id: Optional[int] = Field(None, alias="website_company_id", title="Website Company", description="")
    website_default_lang_id: Optional[int] = Field(None, alias="website_default_lang_id", title="Default language", description="")
    channel_id: Optional[int] = Field(None, alias="channel_id", title="Website Live Channel", description="")
    language_ids: Optional[List[int]] = Field(None, alias="language_ids", title="Languages", description="")
    display_name: Optional[str] = Field(None, alias="display_name", title="Display Name", description="")
    create_uid: Optional[int] = Field(None, alias="create_uid", title="Created by", description="")
    create_date: Optional[str] = Field(None, alias="create_date", title="Created on", description="")
    write_uid: Optional[int] = Field(None, alias="write_uid", title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, alias="write_date", title="Last Updated on", description="")
    web_app_name: Optional[str] = Field(None, alias="web_app_name", title="Web App Name", description="")
    is_root_company: Optional[bool] = Field(None, alias="is_root_company", title="Is Root Company", description="")
    user_default_rights: Optional[bool] = Field(None, alias="user_default_rights", title="Default Access Rights", description="")
    module_base_import: Optional[bool] = Field(None, alias="module_base_import", title="Allow users to import data from CSV/XLS/XLSX/ODS files", description="")
    module_google_calendar: Optional[bool] = Field(None, alias="module_google_calendar", title="Allow the users to synchronize their calendar  with Google Calendar", description="")
    module_microsoft_calendar: Optional[bool] = Field(None, alias="module_microsoft_calendar", title="Allow the users to synchronize their calendar with Outlook Calendar", description="")
    module_mail_plugin: Optional[bool] = Field(None, alias="module_mail_plugin", title="Allow integration with the mail plugins", description="")
    module_auth_oauth: Optional[bool] = Field(None, alias="module_auth_oauth", title="Use external authentication providers (OAuth)", description="")
    module_auth_ldap: Optional[bool] = Field(None, alias="module_auth_ldap", title="LDAP Authentication", description="")
    module_account_inter_company_rules: Optional[bool] = Field(None, alias="module_account_inter_company_rules", title="Manage Inter Company", description="")
    module_voip: Optional[bool] = Field(None, alias="module_voip", title="Asterisk (VoIP)", description="")
    module_web_unsplash: Optional[bool] = Field(None, alias="module_web_unsplash", title="Unsplash Image Library", description="")
    module_partner_autocomplete: Optional[bool] = Field(None, alias="module_partner_autocomplete", title="Partner Autocomplete", description="")
    module_base_geolocalize: Optional[bool] = Field(None, alias="module_base_geolocalize", title="GeoLocalize", description="")
    module_google_recaptcha: Optional[bool] = Field(None, alias="module_google_recaptcha", title="reCAPTCHA", description="")
    module_website_cf_turnstile: Optional[bool] = Field(None, alias="module_website_cf_turnstile", title="Cloudflare Turnstile", description="")
    report_footer: Optional[Any] = Field(None, alias="report_footer", title="Custom Report Footer", description="Footer text displayed at the bottom of all reports.")
    group_multi_currency: Optional[bool] = Field(None, alias="group_multi_currency", title="Multi-Currencies", description="Allows to work in a multi currency environment")
    show_effect: Optional[bool] = Field(None, alias="show_effect", title="Show Effect", description="")
    company_count: Optional[int] = Field(None, alias="company_count", title="Number of Companies", description="")
    active_user_count: Optional[int] = Field(None, alias="active_user_count", title="Number of Active Users", description="")
    language_count: Optional[int] = Field(None, alias="language_count", title="Number of Languages", description="")
    company_name: Optional[str] = Field(None, alias="company_name", title="Company Name", description="")
    company_informations: Optional[Any] = Field(None, alias="company_informations", title="Company Informations", description="")
    company_country_code: Optional[str] = Field(None, alias="company_country_code", title="Company Country Code", description="The ISO country code in two chars. \nYou can use this field for quick search.")
    profiling_enabled_until: Optional[str] = Field(None, alias="profiling_enabled_until", title="Profiling enabled until", description="")
    module_product_images: Optional[bool] = Field(None, alias="module_product_images", title="Get product pictures using barcode", description="")
    geoloc_provider_techname: Optional[str] = Field(None, alias="geoloc_provider_techname", title="Technical Name", description="")
    geoloc_provider_googlemap_key: Optional[str] = Field(None, alias="geoloc_provider_googlemap_key", title="Google Map API Key", description="Visit https://developers.google.com/maps/documentation/geocoding/get-api-key for more information.")
    recaptcha_public_key: Optional[str] = Field(None, alias="recaptcha_public_key", title="Site Key", description="")
    recaptcha_private_key: Optional[str] = Field(None, alias="recaptcha_private_key", title="Secret Key", description="")
    recaptcha_min_score: Optional[Any] = Field(None, alias="recaptcha_min_score", title="Minimum score", description="By default, should be one of 0.1, 0.3, 0.7, 0.9.\n1.0 is very likely a good interaction, 0.0 is very likely a bot")
    external_email_server_default: Optional[bool] = Field(None, alias="external_email_server_default", title="Use Custom Email Servers", description="")
    fail_counter: Optional[int] = Field(None, alias="fail_counter", title="Fail Mail", description="")
    module_google_gmail: Optional[bool] = Field(None, alias="module_google_gmail", title="Support Gmail Authentication", description="")
    module_microsoft_outlook: Optional[bool] = Field(None, alias="module_microsoft_outlook", title="Support Outlook Authentication", description="")
    restrict_template_rendering: Optional[bool] = Field(None, alias="restrict_template_rendering", title="Restrict Template Rendering", description="Users will still be able to render templates.\nHowever only Mail Template Editors will be able to create new dynamic templates or modify existing ones.")
    use_twilio_rtc_servers: Optional[bool] = Field(None, alias="use_twilio_rtc_servers", title="Use Twilio ICE servers", description="If you want to use twilio as TURN/STUN server provider")
    twilio_account_sid: Optional[str] = Field(None, alias="twilio_account_sid", title="Twilio Account SID", description="")
    twilio_account_token: Optional[str] = Field(None, alias="twilio_account_token", title="Twilio Account Auth Token", description="")
    sfu_server_url: Optional[str] = Field(None, alias="sfu_server_url", title="SFU Server URL", description="")
    sfu_server_key: Optional[str] = Field(None, alias="sfu_server_key", title="SFU Server key", description="Base64 encoded key")
    email_primary_color: Optional[str] = Field(None, alias="email_primary_color", title="Email Header Color", description="")
    email_secondary_color: Optional[str] = Field(None, alias="email_secondary_color", title="Email Button Color", description="")
    tenor_api_key: Optional[str] = Field(None, alias="tenor_api_key", title="Tenor API key", description="Add a Tenor GIF API key to enable GIFs support. https://developers.google.com/tenor/guides/quickstart#setup")
    tenor_content_filter: Optional[Any] = Field(None, alias="tenor_content_filter", title="Tenor content filter", description="https://developers.google.com/tenor/guides/content-filtering")
    tenor_gif_limit: Optional[int] = Field(None, alias="tenor_gif_limit", title="Tenor Gif Limit", description="Fetch up to the specified number of GIF.")
    google_translate_api_key: Optional[str] = Field(None, alias="google_translate_api_key", title="Message Translation API Key", description="A valid Google API key is required to enable message translation. https://cloud.google.com/translate/docs/setup")
    group_analytic_accounting: Optional[bool] = Field(None, alias="group_analytic_accounting", title="Analytic Accounting", description="")
    auth_signup_reset_password: Optional[bool] = Field(None, alias="auth_signup_reset_password", title="Enable password reset from Login page", description="")
    auth_signup_uninvited: Optional[Any] = Field(None, alias="auth_signup_uninvited", title="Customer Account", description="")
    google_gmail_client_identifier: Optional[str] = Field(None, alias="google_gmail_client_identifier", title="Gmail Client Id", description="")
    google_gmail_client_secret: Optional[str] = Field(None, alias="google_gmail_client_secret", title="Gmail Client Secret", description="")
    group_discount_per_so_line: Optional[bool] = Field(None, alias="group_discount_per_so_line", title="Discounts", description="")
    group_uom: Optional[bool] = Field(None, alias="group_uom", title="Units of Measure", description="")
    group_product_variant: Optional[bool] = Field(None, alias="group_product_variant", title="Variants", description="")
    module_sale_product_matrix: Optional[bool] = Field(None, alias="module_sale_product_matrix", title="Sales Grid Entry", description="")
    module_loyalty: Optional[bool] = Field(None, alias="module_loyalty", title="Promotions, Coupons, Gift Card & Loyalty Program", description="")
    group_stock_packaging: Optional[bool] = Field(None, alias="group_stock_packaging", title="Product Packagings", description="")
    group_product_pricelist: Optional[bool] = Field(None, alias="group_product_pricelist", title="Pricelists", description="")
    group_sale_pricelist: Optional[bool] = Field(None, alias="group_sale_pricelist", title="Advanced Pricelists", description="Allows to manage different prices based on rules per category of customers.\n                Example: 10% for retailers, promotion of 5 EUR on this product, etc.")
    product_pricelist_setting: Optional[Any] = Field(None, alias="product_pricelist_setting", title="Pricelists Method", description="Multiple prices: Pricelists with fixed price rules by product,\nAdvanced rules: enables advanced price rules for pricelists.")
    product_weight_in_lbs: Optional[Any] = Field(None, alias="product_weight_in_lbs", title="Weight unit of measure", description="")
    product_volume_volume_in_cubic_feet: Optional[Any] = Field(None, alias="product_volume_volume_in_cubic_feet", title="Volume unit of measure", description="")
    unsplash_access_key: Optional[str] = Field(None, alias="unsplash_access_key", title="Access Key", description="")
    partner_autocomplete_insufficient_credit: Optional[bool] = Field(None, alias="partner_autocomplete_insufficient_credit", title="Insufficient credit", description="")
    portal_allow_api_keys: Optional[bool] = Field(None, alias="portal_allow_api_keys", title="Customer API Keys", description="")
    snailmail_color: Optional[bool] = Field(None, alias="snailmail_color", title="Print In Color", description="")
    snailmail_cover: Optional[bool] = Field(None, alias="snailmail_cover", title="Add a Cover Page", description="")
    snailmail_duplex: Optional[bool] = Field(None, alias="snailmail_duplex", title="Print Both sides", description="")
    digest_emails: Optional[bool] = Field(None, alias="digest_emails", title="Digest Emails", description="")
    website_name: Optional[str] = Field(None, alias="website_name", title="Website Name", description="")
    website_domain: Optional[str] = Field(None, alias="website_domain", title="Website Domain", description="E.g. https://www.mydomain.com")
    website_homepage_url: Optional[str] = Field(None, alias="website_homepage_url", title="Homepage Url", description="E.g. /contactus or /shop")
    website_logo: Optional[Any] = Field(None, alias="website_logo", title="Website Logo", description="Display this logo on the website.")
    website_language_count: Optional[int] = Field(None, alias="website_language_count", title="Number of languages", description="")
    website_default_lang_code: Optional[str] = Field(None, alias="website_default_lang_code", title="Default language code", description="This field is used to set/get locales for user")
    shared_user_account: Optional[bool] = Field(None, alias="shared_user_account", title="Shared Customer Accounts", description="")
    website_cookies_bar: Optional[bool] = Field(None, alias="website_cookies_bar", title="Cookies Bar", description="Display a customizable cookies bar on your website.")
    google_analytics_key: Optional[str] = Field(None, alias="google_analytics_key", title="Google Analytics Key", description="")
    google_search_console: Optional[str] = Field(None, alias="google_search_console", title="Google Search Console", description="Google key, or Enable to access first reply")
    plausible_shared_key: Optional[str] = Field(None, alias="plausible_shared_key", title="Plausible auth Key", description="")
    plausible_site: Optional[str] = Field(None, alias="plausible_site", title="Plausible Site (e.g. domain.com)", description="")
    cdn_activated: Optional[bool] = Field(None, alias="cdn_activated", title="Content Delivery Network (CDN)", description="")
    cdn_url: Optional[str] = Field(None, alias="cdn_url", title="CDN Base URL", description="")
    cdn_filters: Optional[Any] = Field(None, alias="cdn_filters", title="CDN Filters", description="URL matching those filters will be rewritten using the CDN Base URL")
    favicon: Optional[Any] = Field(None, alias="favicon", title="Favicon", description="This field holds the image used to display a favicon on the website.")
    social_default_image: Optional[Any] = Field(None, alias="social_default_image", title="Default Social Share Image", description="If set, replaces the website logo as the default social share image.")
    group_multi_website: Optional[bool] = Field(None, alias="group_multi_website", title="Multi-website", description="")
    has_google_analytics: Optional[bool] = Field(None, alias="has_google_analytics", title="Google Analytics", description="")
    has_google_search_console: Optional[bool] = Field(None, alias="has_google_search_console", title="Console Google Search", description="")
    has_default_share_image: Optional[bool] = Field(None, alias="has_default_share_image", title="Use a image by default for sharing", description="")
    has_plausible_shared_key: Optional[bool] = Field(None, alias="has_plausible_shared_key", title="Plausible Analytics", description="")
    module_website_livechat: Optional[bool] = Field(None, alias="module_website_livechat", title="Module Website Livechat", description="")
    module_marketing_automation: Optional[bool] = Field(None, alias="module_marketing_automation", title="Module Marketing Automation", description="")

    class ConfigDict:
        from_attributes = True

    @classmethod
    def from_execute_kw(cls, data:List[dict], fields:List[str] = []) -> List['ConfigSettingsModel']:
        transformed = []
        schema = ConfigSettingsModel.model_json_schema()
        
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
