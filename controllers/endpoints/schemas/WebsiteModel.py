
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class WebsiteModel(BaseModel):
    id: Optional[int] = Field(None, title="ID", description="")
    name: str = Field("", title="Website Name", description="")
    company_id: int = Field(0, title="Company", description="")
    default_lang_id: int = Field(0, title="Default Language", description="")
    user_id: int = Field(0, title="Public User", description="")
    partner_id: Optional[int] = Field(None, title="Public Partner", description="Partner-related data of the user")
    menu_id: Optional[int] = Field(None, title="Main Menu", description="")
    theme_id: Optional[int] = Field(None, title="Theme", description="Installed theme")
    channel_id: Optional[int] = Field(None, title="Website Live Chat Channel", description="")
    language_ids: List[int] = Field([], title="Languages", description="")
    sequence: Optional[int] = Field(None, title="Sequence", description="")
    domain: Optional[str] = Field(None, title="Website Domain", description="E.g. https://www.mydomain.com")
    language_count: Optional[int] = Field(None, title="Number of languages", description="")
    auto_redirect_lang: Optional[bool] = Field(None, title="Autoredirect Language", description="Should users be redirected to their browser's language")
    cookies_bar: Optional[bool] = Field(None, title="Cookies Bar", description="Display a customizable cookies bar on your website.")
    configurator_done: Optional[bool] = Field(None, title="Configurator Done", description="True if configurator has been completed or ignored")
    logo: Optional[Any] = Field(None, title="Website Logo", description="Display this logo on the website.")
    social_twitter: Optional[str] = Field(None, title="Twitter Account", description="")
    social_facebook: Optional[str] = Field(None, title="Facebook Account", description="")
    social_github: Optional[str] = Field(None, title="GitHub Account", description="")
    social_linkedin: Optional[str] = Field(None, title="LinkedIn Account", description="")
    social_youtube: Optional[str] = Field(None, title="Youtube Account", description="")
    social_instagram: Optional[str] = Field(None, title="Instagram Account", description="")
    social_tiktok: Optional[str] = Field(None, title="TikTok Account", description="")
    social_default_image: Optional[Any] = Field(None, title="Default Social Share Image", description="If set, replaces the website logo as the default social share image.")
    has_social_default_image: Optional[bool] = Field(None, title="Has Social Default Image", description="")
    google_analytics_key: Optional[str] = Field(None, title="Google Analytics Key", description="")
    google_search_console: Optional[str] = Field(None, title="Google Search Console", description="Google key, or Enable to access first reply")
    google_maps_api_key: Optional[str] = Field(None, title="Google Maps API Key", description="")
    plausible_shared_key: Optional[str] = Field(None, title="Plausible Shared Key", description="")
    plausible_site: Optional[str] = Field(None, title="Plausible Site", description="")
    cdn_activated: Optional[bool] = Field(None, title="Content Delivery Network (CDN)", description="")
    cdn_url: Optional[str] = Field(None, title="CDN Base URL", description="")
    cdn_filters: Optional[Any] = Field(None, title="CDN Filters", description="URL matching those filters will be rewritten using the CDN Base URL")
    homepage_url: Optional[str] = Field(None, title="Homepage Url", description="E.g. /contactus or /shop")
    custom_code_head: Optional[Any] = Field(None, title="Custom <head> code", description="")
    custom_code_footer: Optional[Any] = Field(None, title="Custom end of <body> code", description="")
    robots_txt: Optional[Any] = Field(None, title="Robots.txt", description="")
    favicon: Optional[Any] = Field(None, title="Website Favicon", description="This field holds the image used to display a favicon on the website.")
    specific_user_account: Optional[bool] = Field(None, title="Specific User Account", description="If True, new accounts will be associated to the current website")
    auth_signup_uninvited: Optional[Any] = Field(None, title="Customer Account", description="")
    display_name: Optional[str] = Field(None, title="Display Name", description="")
    create_uid: Optional[int] = Field(None, title="Created by", description="")
    create_date: Optional[str] = Field(None, title="Created on", description="")
    write_uid: Optional[int] = Field(None, title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, title="Last Updated on", description="")

