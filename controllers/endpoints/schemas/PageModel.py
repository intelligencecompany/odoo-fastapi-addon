
from pydantic import BaseModel, Field
from typing import Optional, List, Any, Dict

class PageModel(BaseModel):
    id: Optional[int] = Field(None, alias="id", title="ID", description="")
    url: str = Field("", alias="url", title="Page URL", description="")
    name: str = Field("", alias="name", title="View Name", description="")
    priority: int = Field(0, alias="priority", title="Sequence", description="")
    mode: Any = Field(None, alias="mode", title="View inheritance mode", description="Only applies if this view inherits from an other one (inherit_id is not False/Null).\n\n* if extension (default), if this view is requested the closest primary view\nis looked up (via inherit_id), then all views inheriting from it with this\nview's model are applied\n* if primary, the closest primary view is fully resolved (even if it uses a\ndifferent model than this one), then this view's inheritance specs\n(<xpath/>) are applied, and the result is used as if it were this view's\nactual arch.")
    website_id: Optional[int] = Field(None, alias="website_id", title="Website", description="Restrict publishing to this website.")
    view_id: int = Field(0, alias="view_id", title="View", description="")
    theme_template_id: Optional[int] = Field(None, alias="theme_template_id", title="Theme Template", description="")
    inherit_id: Optional[int] = Field(None, alias="inherit_id", title="Inherited View", description="")
    x_model_data_id: Optional[int] = Field(None, alias="x_model_data_id", title="Model Data", description="")
    xml_id: Optional[str] = Field(None, alias="xml_id", title="External ID", description="ID of the view defined in xml file")
    groups_id: Optional[List[int]] = Field(None, alias="groups_id", title="Groups", description="If this field is empty, the view applies to all users. Otherwise, the view applies to the users of those groups only.")
    x_model_id: Optional[int] = Field(None, alias="x_model_id", title="Model of the view", description="")
    first_page_id: Optional[int] = Field(None, alias="first_page_id", title="Website Page", description="First page linked to this view")
    menu_ids: Optional[List[int]] = Field(None, alias="menu_ids", title="Related Menus", description="")
    inherit_children_ids: Optional[List[int]] = Field(None, alias="inherit_children_ids", title="Views which inherit from this one", description="")
    page_ids: Optional[List[int]] = Field(None, alias="page_ids", title="Page", description="")
    controller_page_ids: Optional[List[int]] = Field(None, alias="controller_page_ids", title="Controller Page", description="")
    website_published: Optional[bool] = Field(None, alias="website_published", title="Visible on current website", description="")
    is_published: Optional[bool] = Field(None, alias="is_published", title="Is Published", description="")
    can_publish: Optional[bool] = Field(None, alias="can_publish", title="Can Publish", description="")
    website_url: Optional[str] = Field(None, alias="website_url", title="Website URL", description="The full URL to access the document through the website.")
    website_indexed: Optional[bool] = Field(None, alias="website_indexed", title="Is Indexed", description="")
    date_publish: Optional[str] = Field(None, alias="date_publish", title="Publishing Date", description="")
    is_in_menu: Optional[bool] = Field(None, alias="is_in_menu", title="Is In Menu", description="")
    is_homepage: Optional[bool] = Field(None, alias="is_homepage", title="Homepage", description="")
    is_visible: Optional[bool] = Field(None, alias="is_visible", title="Is Visible", description="")
    header_overlay: Optional[bool] = Field(None, alias="header_overlay", title="Header Overlay", description="")
    header_color: Optional[str] = Field(None, alias="header_color", title="Header Color", description="")
    header_text_color: Optional[str] = Field(None, alias="header_text_color", title="Header Text Color", description="")
    header_visible: Optional[bool] = Field(None, alias="header_visible", title="Header Visible", description="")
    footer_visible: Optional[bool] = Field(None, alias="footer_visible", title="Footer Visible", description="")
    arch: Optional[Any] = Field(None, alias="arch", title="View Architecture", description="This field should be used when accessing view arch. It will use translation.\n                               Note that it will read `arch_db` or `arch_fs` if in dev-xml mode.")
    display_name: Optional[str] = Field(None, alias="display_name", title="Display Name", description="")
    create_uid: Optional[int] = Field(None, alias="create_uid", title="Created by", description="")
    create_date: Optional[str] = Field(None, alias="create_date", title="Created on", description="")
    write_uid: Optional[int] = Field(None, alias="write_uid", title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, alias="write_date", title="Last Updated on", description="")
    is_seo_optimized: Optional[bool] = Field(None, alias="is_seo_optimized", title="SEO optimized", description="")
    website_meta_title: Optional[str] = Field(None, alias="website_meta_title", title="Website meta title", description="")
    website_meta_description: Optional[Any] = Field(None, alias="website_meta_description", title="Website meta description", description="")
    website_meta_keywords: Optional[str] = Field(None, alias="website_meta_keywords", title="Website meta keywords", description="")
    website_meta_og_img: Optional[str] = Field(None, alias="website_meta_og_img", title="Website opengraph image", description="")
    seo_name: Optional[str] = Field(None, alias="seo_name", title="Seo name", description="")
    model: Optional[str] = Field(None, alias="model", title="Model", description="")
    key: Optional[str] = Field(None, alias="key", title="Key", description="")
    type: Optional[Any] = Field(None, alias="type", title="View Type", description="")
    arch_base: Optional[Any] = Field(None, alias="arch_base", title="Base View Architecture", description="This field is the same as `arch` field without translations")
    arch_db: Optional[Any] = Field(None, alias="arch_db", title="Arch Blob", description="This field stores the view arch.")
    arch_fs: Optional[str] = Field(None, alias="arch_fs", title="Arch Filename", description="File from where the view originates.\n                                                          Useful to (hard) reset broken views or to read arch from file in dev-xml mode.")
    arch_updated: Optional[bool] = Field(None, alias="arch_updated", title="Modified Architecture", description="")
    arch_prev: Optional[Any] = Field(None, alias="arch_prev", title="Previous View Architecture", description="This field will save the current `arch_db` before writing on it.\n                                                                         Useful to (soft) reset a broken view.")
    active: Optional[bool] = Field(None, alias="active", title="Active", description="If this view is inherited,\n* if True, the view always extends its parent\n* if False, the view currently does not extend its parent but can be enabled")
    customize_show: Optional[bool] = Field(None, alias="customize_show", title="Show As Optional Inherit", description="")
    track: Optional[bool] = Field(None, alias="track", title="Track", description="Allow to specify for one page of the website to be trackable or not")
    visibility: Optional[Any] = Field(None, alias="visibility", title="Visibility", description="")
    visibility_password: Optional[str] = Field(None, alias="visibility_password", title="Visibility Password", description="")
    visibility_password_display: Optional[str] = Field(None, alias="visibility_password_display", title="Visibility Password Display", description="")

    class ConfigDict:
        from_attributes = True

    @classmethod
    def from_execute_kw(cls, item:Dict[str, Any]) -> 'PageModel':
        filtered_item = {}
        schema = PageModel.model_json_schema()

        for key in item:
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

        return cls(**filtered_item).model_dump(by_alias=True)

    @classmethod
    def list_from_execute_kw(cls, data:List[dict], fields:List[str] = []) -> List['PageModel']:
        transformed = []
        schema = PageModel.model_json_schema()
        
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
