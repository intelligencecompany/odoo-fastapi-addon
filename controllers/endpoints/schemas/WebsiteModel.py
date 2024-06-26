
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class WebsiteModel(BaseModel):
    id: Optional[int] = Field(None, alias="id", title="ID", description="")
    name: str = Field("", alias="name", title="Website Name", description="")
    company_id: int = Field(0, alias="company_id", title="Company", description="")
    default_lang_id: int = Field(0, alias="default_lang_id", title="Default Language", description="")
    user_id: int = Field(0, alias="user_id", title="Public User", description="")
    partner_id: Optional[int] = Field(None, alias="partner_id", title="Public Partner", description="Partner-related data of the user")
    menu_id: Optional[int] = Field(None, alias="menu_id", title="Main Menu", description="")
    theme_id: Optional[int] = Field(None, alias="theme_id", title="Theme", description="Installed theme")
    channel_id: Optional[int] = Field(None, alias="channel_id", title="Website Live Chat Channel", description="")
    language_ids: List[int] = Field([], alias="language_ids", title="Languages", description="")
    sequence: Optional[int] = Field(None, alias="sequence", title="Sequence", description="")
    domain: Optional[str] = Field(None, alias="domain", title="Website Domain", description="E.g. https://www.mydomain.com")
    language_count: Optional[int] = Field(None, alias="language_count", title="Number of languages", description="")
    auto_redirect_lang: Optional[bool] = Field(None, alias="auto_redirect_lang", title="Autoredirect Language", description="Should users be redirected to their browser's language")
    cookies_bar: Optional[bool] = Field(None, alias="cookies_bar", title="Cookies Bar", description="Display a customizable cookies bar on your website.")
    configurator_done: Optional[bool] = Field(None, alias="configurator_done", title="Configurator Done", description="True if configurator has been completed or ignored")
    logo: Optional[Any] = Field(None, alias="logo", title="Website Logo", description="Display this logo on the website.")
    social_twitter: Optional[str] = Field(None, alias="social_twitter", title="Twitter Account", description="")
    social_facebook: Optional[str] = Field(None, alias="social_facebook", title="Facebook Account", description="")
    social_github: Optional[str] = Field(None, alias="social_github", title="GitHub Account", description="")
    social_linkedin: Optional[str] = Field(None, alias="social_linkedin", title="LinkedIn Account", description="")
    social_youtube: Optional[str] = Field(None, alias="social_youtube", title="Youtube Account", description="")
    social_instagram: Optional[str] = Field(None, alias="social_instagram", title="Instagram Account", description="")
    social_tiktok: Optional[str] = Field(None, alias="social_tiktok", title="TikTok Account", description="")
    social_default_image: Optional[Any] = Field(None, alias="social_default_image", title="Default Social Share Image", description="If set, replaces the website logo as the default social share image.")
    has_social_default_image: Optional[bool] = Field(None, alias="has_social_default_image", title="Has Social Default Image", description="")
    google_analytics_key: Optional[str] = Field(None, alias="google_analytics_key", title="Google Analytics Key", description="")
    google_search_console: Optional[str] = Field(None, alias="google_search_console", title="Google Search Console", description="Google key, or Enable to access first reply")
    google_maps_api_key: Optional[str] = Field(None, alias="google_maps_api_key", title="Google Maps API Key", description="")
    plausible_shared_key: Optional[str] = Field(None, alias="plausible_shared_key", title="Plausible Shared Key", description="")
    plausible_site: Optional[str] = Field(None, alias="plausible_site", title="Plausible Site", description="")
    cdn_activated: Optional[bool] = Field(None, alias="cdn_activated", title="Content Delivery Network (CDN)", description="")
    cdn_url: Optional[str] = Field(None, alias="cdn_url", title="CDN Base URL", description="")
    cdn_filters: Optional[Any] = Field(None, alias="cdn_filters", title="CDN Filters", description="URL matching those filters will be rewritten using the CDN Base URL")
    homepage_url: Optional[str] = Field(None, alias="homepage_url", title="Homepage Url", description="E.g. /contactus or /shop")
    custom_code_head: Optional[Any] = Field(None, alias="custom_code_head", title="Custom <head> code", description="")
    custom_code_footer: Optional[Any] = Field(None, alias="custom_code_footer", title="Custom end of <body> code", description="")
    robots_txt: Optional[Any] = Field(None, alias="robots_txt", title="Robots.txt", description="")
    favicon: Optional[Any] = Field(None, alias="favicon", title="Website Favicon", description="This field holds the image used to display a favicon on the website.")
    specific_user_account: Optional[bool] = Field(None, alias="specific_user_account", title="Specific User Account", description="If True, new accounts will be associated to the current website")
    auth_signup_uninvited: Optional[Any] = Field(None, alias="auth_signup_uninvited", title="Customer Account", description="")
    display_name: Optional[str] = Field(None, alias="display_name", title="Display Name", description="")
    create_uid: Optional[int] = Field(None, alias="create_uid", title="Created by", description="")
    create_date: Optional[str] = Field(None, alias="create_date", title="Created on", description="")
    write_uid: Optional[int] = Field(None, alias="write_uid", title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, alias="write_date", title="Last Updated on", description="")

    class Config:
        from_attributes = True

    @classmethod
    def from_execute_kw(cls, data:List[dict], fields:List[str] = []) -> List['WebsiteModel']:
        transformed = []
        schema = WebsiteModel.model_json_schema()
        
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
