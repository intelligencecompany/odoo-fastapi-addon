
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class ModelPageModel(BaseModel):
    id: Optional[int] = Field(None, title="ID", description="")
    page_name: str = Field("", title="Name", description="The name is used to generate the URL and is shown in the browser title bar")
    name: str = Field("", title="View Name", description="")
    priority: int = Field(0, title="Sequence", description="")
    mode: Any = Field(None, title="View inheritance mode", description="Only applies if this view inherits from an other one (inherit_id is not False/Null).\n\n* if extension (default), if this view is requested the closest primary view\nis looked up (via inherit_id), then all views inheriting from it with this\nview's model are applied\n* if primary, the closest primary view is fully resolved (even if it uses a\ndifferent model than this one), then this view's inheritance specs\n(<xpath/>) are applied, and the result is used as if it were this view's\nactual arch.")
    website_id: Optional[int] = Field(None, title="Website", description="Restrict publishing to this website.")
    view_id: int = Field(0, title="View", description="")
    inherit_id: Optional[int] = Field(None, title="Inherited View", description="")
    model_data_id: Optional[int] = Field(None, title="Model Data", description="")
    xml_id: Optional[str] = Field(None, title="External ID", description="ID of the view defined in xml file")
    groups_id: Optional[List[int]] = Field(None, title="Groups", description="If this field is empty, the view applies to all users. Otherwise, the view applies to the users of those groups only.")
    model_id: Optional[int] = Field(None, title="Model of the view", description="")
    first_page_id: Optional[int] = Field(None, title="Website Page", description="First page linked to this view")
    theme_template_id: Optional[int] = Field(None, title="Theme Template", description="")
    menu_ids: Optional[List[int]] = Field(None, title="Related Menus", description="")
    inherit_children_ids: Optional[List[int]] = Field(None, title="Views which inherit from this one", description="")
    page_ids: Optional[List[int]] = Field(None, title="Page", description="")
    controller_page_ids: Optional[List[int]] = Field(None, title="Controller Page", description="")
    website_published: Optional[bool] = Field(None, title="Visible on current website", description="")
    is_published: Optional[bool] = Field(None, title="Is Published", description="")
    can_publish: Optional[bool] = Field(None, title="Can Publish", description="")
    website_url: Optional[str] = Field(None, title="Website URL", description="The full URL to access the document through the website.")
    name_slugified: Optional[str] = Field(None, title="URL", description="The name of the page usable in a URL")
    page_type: Optional[Any] = Field(None, title="Page Type", description="The type of the page. If set, it indicates whether the page displays a list of records or a single record")
    record_domain: Optional[str] = Field(None, title="Domain", description="Domain to restrict records that can be viewed publicly")
    default_layout: Optional[Any] = Field(None, title="Default Layout", description="")
    display_name: Optional[str] = Field(None, title="Display Name", description="")
    create_uid: Optional[int] = Field(None, title="Created by", description="")
    create_date: Optional[str] = Field(None, title="Created on", description="")
    write_uid: Optional[int] = Field(None, title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, title="Last Updated on", description="")
    is_seo_optimized: Optional[bool] = Field(None, title="SEO optimized", description="")
    website_meta_title: Optional[str] = Field(None, title="Website meta title", description="")
    website_meta_description: Optional[Any] = Field(None, title="Website meta description", description="")
    website_meta_keywords: Optional[str] = Field(None, title="Website meta keywords", description="")
    website_meta_og_img: Optional[str] = Field(None, title="Website opengraph image", description="")
    seo_name: Optional[str] = Field(None, title="Seo name", description="")
    model: Optional[str] = Field(None, title="Model", description="")
    key: Optional[str] = Field(None, title="Key", description="")
    type: Optional[Any] = Field(None, title="View Type", description="")
    arch: Optional[Any] = Field(None, title="View Architecture", description="This field should be used when accessing view arch. It will use translation.\n                               Note that it will read `arch_db` or `arch_fs` if in dev-xml mode.")
    arch_base: Optional[Any] = Field(None, title="Base View Architecture", description="This field is the same as `arch` field without translations")
    arch_db: Optional[Any] = Field(None, title="Arch Blob", description="This field stores the view arch.")
    arch_fs: Optional[str] = Field(None, title="Arch Filename", description="File from where the view originates.\n                                                          Useful to (hard) reset broken views or to read arch from file in dev-xml mode.")
    arch_updated: Optional[bool] = Field(None, title="Modified Architecture", description="")
    arch_prev: Optional[Any] = Field(None, title="Previous View Architecture", description="This field will save the current `arch_db` before writing on it.\n                                                                         Useful to (soft) reset a broken view.")
    active: Optional[bool] = Field(None, title="Active", description="If this view is inherited,\n* if True, the view always extends its parent\n* if False, the view currently does not extend its parent but can be enabled")
    customize_show: Optional[bool] = Field(None, title="Show As Optional Inherit", description="")
    track: Optional[bool] = Field(None, title="Track", description="Allow to specify for one page of the website to be trackable or not")
    visibility: Optional[Any] = Field(None, title="Visibility", description="")
    visibility_password: Optional[str] = Field(None, title="Visibility Password", description="")
    visibility_password_display: Optional[str] = Field(None, title="Visibility Password Display", description="")

