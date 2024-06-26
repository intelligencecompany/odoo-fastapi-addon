
from pydantic import BaseModel, Field
from typing import Optional, List, Any, Dict

class UserModel(BaseModel):
    id: Optional[int] = Field(None, alias="id", title="ID", description="")
    login: str = Field("", alias="login", title="Login", description="Used to log into the system")
    notification_type: Any = Field(None, alias="notification_type", title="Notification", description="Policy on how to handle Chatter notifications:\n- Handle by Emails: notifications are sent to your email address\n- Handle in Odoo: notifications appear in your Odoo Inbox")
    partner_id: int = Field(0, alias="partner_id", title="Related Partner", description="Partner-related data of the user")
    action_id: Optional[int] = Field(None, alias="action_id", title="Home Action", description="If specified, this action will be opened at log on for this user, in addition to the standard menu.")
    groups_id: Optional[List[int]] = Field(None, alias="groups_id", title="Groups", description="")
    res_users_settings_id: Optional[int] = Field(None, alias="res_users_settings_id", title="Settings", description="")
    company_id: int = Field(0, alias="company_id", title="Company", description="The default company for this user.")
    resource_calendar_id: Optional[int] = Field(None, alias="resource_calendar_id", title="Default Working Hours", description="")
    website_id: Optional[int] = Field(None, alias="website_id", title="Website", description="Restrict publishing to this website.")
    activity_user_id: Optional[int] = Field(None, alias="activity_user_id", title="Responsible User", description="")
    activity_type_id: Optional[int] = Field(None, alias="activity_type_id", title="Next Activity Type", description="")
    activity_calendar_event_id: Optional[int] = Field(None, alias="activity_calendar_event_id", title="Next Activity Calendar Event", description="")
    parent_id: Optional[int] = Field(None, alias="parent_id", title="Related Company", description="")
    user_id: Optional[int] = Field(None, alias="user_id", title="Salesperson", description="The internal user in charge of this contact.")
    same_vat_partner_id: Optional[int] = Field(None, alias="same_vat_partner_id", title="Partner with same Tax ID", description="")
    same_company_registry_partner_id: Optional[int] = Field(None, alias="same_company_registry_partner_id", title="Partner with same Company Registry", description="")
    category_id: Optional[List[int]] = Field(None, alias="category_id", title="Tags", description="")
    state_id: Optional[int] = Field(None, alias="state_id", title="State", description="")
    country_id: Optional[int] = Field(None, alias="country_id", title="Country", description="")
    industry_id: Optional[int] = Field(None, alias="industry_id", title="Industry", description="")
    commercial_partner_id: Optional[int] = Field(None, alias="commercial_partner_id", title="Commercial Entity", description="")
    log_ids: Optional[List[int]] = Field(None, alias="log_ids", title="User log entries", description="")
    res_users_settings_ids: Optional[List[int]] = Field(None, alias="res_users_settings_ids", title="Res Users Settings", description="")
    company_ids: Optional[List[int]] = Field(None, alias="company_ids", title="Companies", description="")
    api_key_ids: Optional[List[int]] = Field(None, alias="api_key_ids", title="API Keys", description="")
    totp_trusted_device_ids: Optional[List[int]] = Field(None, alias="totp_trusted_device_ids", title="Trusted Devices", description="")
    resource_ids: Optional[List[int]] = Field(None, alias="resource_ids", title="Resources", description="")
    livechat_lang_ids: Optional[List[int]] = Field(None, alias="livechat_lang_ids", title="Livechat Languages", description="")
    message_follower_ids: Optional[List[int]] = Field(None, alias="message_follower_ids", title="Followers", description="")
    message_partner_ids: Optional[List[int]] = Field(None, alias="message_partner_ids", title="Followers (Partners)", description="")
    message_ids: Optional[List[int]] = Field(None, alias="message_ids", title="Messages", description="")
    rating_ids: Optional[List[int]] = Field(None, alias="rating_ids", title="Ratings", description="")
    website_message_ids: Optional[List[int]] = Field(None, alias="website_message_ids", title="Website Messages", description="Website communication history")
    activity_ids: Optional[List[int]] = Field(None, alias="activity_ids", title="Activities", description="")
    child_ids: Optional[List[int]] = Field(None, alias="child_ids", title="Contact", description="")
    bank_ids: Optional[List[int]] = Field(None, alias="bank_ids", title="Banks", description="")
    user_ids: Optional[List[int]] = Field(None, alias="user_ids", title="Users", description="")
    channel_ids: Optional[List[int]] = Field(None, alias="channel_ids", title="Channels", description="")
    starred_message_ids: Optional[List[int]] = Field(None, alias="starred_message_ids", title="Starred Message", description="")
    meeting_ids: Optional[List[int]] = Field(None, alias="meeting_ids", title="Meetings", description="")
    payment_token_ids: Optional[List[int]] = Field(None, alias="payment_token_ids", title="Payment Tokens", description="")
    visitor_ids: Optional[List[int]] = Field(None, alias="visitor_ids", title="Visitors", description="")
    password: Optional[str] = Field(None, alias="password", title="Password", description="Keep empty if you don't want the user to be able to connect on the system.")
    new_password: Optional[str] = Field(None, alias="new_password", title="Set Password", description="Specify a value only when creating a user or if you're changing the user's password, otherwise leave empty. After a change of password, the user has to login again.")
    signature: Optional[Any] = Field(None, alias="signature", title="Email Signature", description="")
    active: Optional[bool] = Field(None, alias="active", title="Active", description="")
    active_partner: Optional[bool] = Field(None, alias="active_partner", title="Partner is Active", description="")
    login_date: Optional[str] = Field(None, alias="login_date", title="Latest authentication", description="")
    share: Optional[bool] = Field(None, alias="share", title="Share User", description="External user with limited access, created only for the purpose of sharing data.")
    companies_count: Optional[int] = Field(None, alias="companies_count", title="Number of Companies", description="")
    tz_offset: Optional[str] = Field(None, alias="tz_offset", title="Timezone offset", description="")
    name: Optional[str] = Field(None, alias="name", title="Name", description="")
    email: Optional[str] = Field(None, alias="email", title="Email", description="")
    accesses_count: Optional[int] = Field(None, alias="accesses_count", title="# Access Rights", description="Number of access rights that apply to the current user")
    rules_count: Optional[int] = Field(None, alias="rules_count", title="# Record Rules", description="Number of record rules that apply to the current user")
    groups_count: Optional[int] = Field(None, alias="groups_count", title="# Groups", description="Number of groups that apply to the current user")
    display_name: Optional[str] = Field(None, alias="display_name", title="Display Name", description="")
    create_uid: Optional[int] = Field(None, alias="create_uid", title="Created by", description="")
    create_date: Optional[str] = Field(None, alias="create_date", title="Created on", description="")
    write_uid: Optional[int] = Field(None, alias="write_uid", title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, alias="write_date", title="Last Updated on", description="")
    user_group_warning: Optional[Any] = Field(None, alias="user_group_warning", title="User Group Warning", description="")
    totp_enabled: Optional[bool] = Field(None, alias="totp_enabled", title="Two-factor authentication", description="")
    im_status: Optional[str] = Field(None, alias="im_status", title="IM Status", description="")
    state: Optional[Any] = Field(None, alias="state", title="Status", description="")
    odoobot_state: Optional[Any] = Field(None, alias="odoobot_state", title="OdooBot Status", description="")
    odoobot_failed: Optional[bool] = Field(None, alias="odoobot_failed", title="Odoobot Failed", description="")
    livechat_username: Optional[str] = Field(None, alias="livechat_username", title="Livechat Username", description="")
    has_access_livechat: Optional[bool] = Field(None, alias="has_access_livechat", title="Has access to Livechat", description="")
    is_seo_optimized: Optional[bool] = Field(None, alias="is_seo_optimized", title="SEO optimized", description="")
    website_meta_title: Optional[str] = Field(None, alias="website_meta_title", title="Website meta title", description="")
    website_meta_description: Optional[Any] = Field(None, alias="website_meta_description", title="Website meta description", description="")
    website_meta_keywords: Optional[str] = Field(None, alias="website_meta_keywords", title="Website meta keywords", description="")
    website_meta_og_img: Optional[str] = Field(None, alias="website_meta_og_img", title="Website opengraph image", description="")
    seo_name: Optional[str] = Field(None, alias="seo_name", title="Seo name", description="")
    website_published: Optional[bool] = Field(None, alias="website_published", title="Visible on current website", description="")
    is_published: Optional[bool] = Field(None, alias="is_published", title="Is Published", description="")
    can_publish: Optional[bool] = Field(None, alias="can_publish", title="Can Publish", description="")
    website_url: Optional[str] = Field(None, alias="website_url", title="Website URL", description="The full URL to access the document through the website.")
    message_is_follower: Optional[bool] = Field(None, alias="message_is_follower", title="Is Follower", description="")
    has_message: Optional[bool] = Field(None, alias="has_message", title="Has Message", description="")
    message_needaction: Optional[bool] = Field(None, alias="message_needaction", title="Action Needed", description="If checked, new messages require your attention.")
    message_needaction_counter: Optional[int] = Field(None, alias="message_needaction_counter", title="Number of Actions", description="Number of messages requiring action")
    message_has_error: Optional[bool] = Field(None, alias="message_has_error", title="Message Delivery error", description="If checked, some messages have a delivery error.")
    message_has_error_counter: Optional[int] = Field(None, alias="message_has_error_counter", title="Number of errors", description="Number of messages with delivery error")
    message_attachment_count: Optional[int] = Field(None, alias="message_attachment_count", title="Attachment Count", description="")
    message_has_sms_error: Optional[bool] = Field(None, alias="message_has_sms_error", title="SMS Delivery error", description="If checked, some messages have a delivery error.")
    email_normalized: Optional[str] = Field(None, alias="email_normalized", title="Normalized Email", description="This field is used to search on email address as the primary email field can contain more than strictly an email address.")
    is_blacklisted: Optional[bool] = Field(None, alias="is_blacklisted", title="Blacklist", description="If the email address is on the blacklist, the contact won't receive mass mailing anymore, from any list")
    message_bounce: Optional[int] = Field(None, alias="message_bounce", title="Bounce", description="Counter of the number of bounced emails for this contact")
    activity_state: Optional[Any] = Field(None, alias="activity_state", title="Activity State", description="Status based on activities\nOverdue: Due date is already passed\nToday: Activity date is today\nPlanned: Future activities.")
    activity_type_icon: Optional[str] = Field(None, alias="activity_type_icon", title="Activity Type Icon", description="Font awesome icon e.g. fa-tasks")
    activity_date_deadline: Optional[str] = Field(None, alias="activity_date_deadline", title="Next Activity Deadline", description="")
    my_activity_date_deadline: Optional[str] = Field(None, alias="my_activity_date_deadline", title="My Activity Deadline", description="")
    activity_summary: Optional[str] = Field(None, alias="activity_summary", title="Next Activity Summary", description="")
    activity_exception_decoration: Optional[Any] = Field(None, alias="activity_exception_decoration", title="Activity Exception Decoration", description="Type of the exception activity on record.")
    activity_exception_icon: Optional[str] = Field(None, alias="activity_exception_icon", title="Icon", description="Icon to indicate an exception activity.")
    image_1920: Optional[Any] = Field(None, alias="image_1920", title="Image", description="")
    image_1024: Optional[Any] = Field(None, alias="image_1024", title="Image 1024", description="")
    image_512: Optional[Any] = Field(None, alias="image_512", title="Image 512", description="")
    image_256: Optional[Any] = Field(None, alias="image_256", title="Image 256", description="")
    image_128: Optional[Any] = Field(None, alias="image_128", title="Image 128", description="")
    avatar_1920: Optional[Any] = Field(None, alias="avatar_1920", title="Avatar", description="")
    avatar_1024: Optional[Any] = Field(None, alias="avatar_1024", title="Avatar 1024", description="")
    avatar_512: Optional[Any] = Field(None, alias="avatar_512", title="Avatar 512", description="")
    avatar_256: Optional[Any] = Field(None, alias="avatar_256", title="Avatar 256", description="")
    avatar_128: Optional[Any] = Field(None, alias="avatar_128", title="Avatar 128", description="")
    complete_name: Optional[str] = Field(None, alias="complete_name", title="Complete Name", description="")
    date: Optional[str] = Field(None, alias="date", title="Date", description="")
    title: Optional[int] = Field(None, alias="title", title="Title", description="")
    parent_name: Optional[str] = Field(None, alias="parent_name", title="Parent name", description="")
    ref: Optional[str] = Field(None, alias="ref", title="Reference", description="")
    lang: Optional[Any] = Field(None, alias="lang", title="Language", description="All the emails and documents sent to this contact will be translated in this language.")
    active_lang_count: Optional[int] = Field(None, alias="active_lang_count", title="Active Lang Count", description="")
    tz: Optional[Any] = Field(None, alias="tz", title="Timezone", description="When printing documents and exporting/importing data, time values are computed according to this timezone.\nIf the timezone is not set, UTC (Coordinated Universal Time) is used.\nAnywhere else, time values are computed according to the time offset of your web client.")
    vat: Optional[str] = Field(None, alias="vat", title="Tax ID", description="The Tax Identification Number. Values here will be validated based on the country format. You can use '/' to indicate that the partner is not subject to tax.")
    company_registry: Optional[str] = Field(None, alias="company_registry", title="Company ID", description="The registry number of the company. Use it if it is different from the Tax ID. It must be unique across all partners of a same country")
    website: Optional[str] = Field(None, alias="website", title="Website Link", description="")
    comment: Optional[Any] = Field(None, alias="comment", title="Notes", description="")
    employee: Optional[bool] = Field(None, alias="employee", title="Employee", description="Check this box if this contact is an Employee.")
    function: Optional[str] = Field(None, alias="function", title="Job Position", description="")
    type: Optional[Any] = Field(None, alias="type", title="Address Type", description="- Contact: Use this to organize the contact details of employees of a given company (e.g. CEO, CFO, ...).\n- Invoice Address: Preferred address for all invoices. Selected by default when you invoice an order that belongs to this company.\n- Delivery Address: Preferred address for all deliveries. Selected by default when you deliver an order that belongs to this company.\n- Other: Other address for the company (e.g. subsidiary, ...)")
    street: Optional[str] = Field(None, alias="street", title="Street", description="")
    street2: Optional[str] = Field(None, alias="street2", title="Street2", description="")
    zip: Optional[str] = Field(None, alias="zip", title="Zip", description="")
    city: Optional[str] = Field(None, alias="city", title="City", description="")
    country_code: Optional[str] = Field(None, alias="country_code", title="Country Code", description="The ISO country code in two chars. \nYou can use this field for quick search.")
    partner_latitude: Optional[Any] = Field(None, alias="partner_latitude", title="Geo Latitude", description="")
    partner_longitude: Optional[Any] = Field(None, alias="partner_longitude", title="Geo Longitude", description="")
    email_formatted: Optional[str] = Field(None, alias="email_formatted", title="Formatted Email", description="Format email address \"Name <email@domain>\"")
    phone: Optional[str] = Field(None, alias="phone", title="Phone", description="")
    mobile: Optional[str] = Field(None, alias="mobile", title="Mobile", description="")
    is_company: Optional[bool] = Field(None, alias="is_company", title="Is a Company", description="Check if the contact is a company, otherwise it is a person")
    is_public: Optional[bool] = Field(None, alias="is_public", title="Is Public", description="")
    company_type: Optional[Any] = Field(None, alias="company_type", title="Company Type", description="")
    color: Optional[int] = Field(None, alias="color", title="Color Index", description="")
    partner_share: Optional[bool] = Field(None, alias="partner_share", title="Share Partner", description="Either customer (not a user), either shared user. Indicated the current partner is a customer without access or with a limited access created for sharing data.")
    contact_address: Optional[str] = Field(None, alias="contact_address", title="Complete Address", description="")
    commercial_company_name: Optional[str] = Field(None, alias="commercial_company_name", title="Company Name Entity", description="")
    company_name: Optional[str] = Field(None, alias="company_name", title="Company Name", description="")
    barcode: Optional[str] = Field(None, alias="barcode", title="Barcode", description="Use a barcode to identify this contact.")
    self: Optional[int] = Field(None, alias="self", title="Self", description="")
    date_localization: Optional[str] = Field(None, alias="date_localization", title="Geolocation Date", description="")
    contact_address_inline: Optional[str] = Field(None, alias="contact_address_inline", title="Inlined Complete Address", description="")
    signup_token: Optional[str] = Field(None, alias="signup_token", title="Signup Token", description="")
    signup_type: Optional[str] = Field(None, alias="signup_type", title="Signup Token Type", description="")
    signup_expiration: Optional[str] = Field(None, alias="signup_expiration", title="Signup Expiration", description="")
    signup_valid: Optional[bool] = Field(None, alias="signup_valid", title="Signup Token is Valid", description="")
    signup_url: Optional[str] = Field(None, alias="signup_url", title="Signup URL", description="")
    meeting_count: Optional[int] = Field(None, alias="meeting_count", title="# Meetings", description="")
    calendar_last_notif_ack: Optional[str] = Field(None, alias="calendar_last_notif_ack", title="Last notification marked as read from base Calendar", description="")
    property_product_pricelist: Optional[int] = Field(None, alias="property_product_pricelist", title="Pricelist", description="This pricelist will be used, instead of the default one, for sales to the current partner")
    partner_gid: Optional[int] = Field(None, alias="partner_gid", title="Company database ID", description="")
    additional_info: Optional[str] = Field(None, alias="additional_info", title="Additional info", description="")
    phone_sanitized: Optional[str] = Field(None, alias="phone_sanitized", title="Sanitized Number", description="Field used to store sanitized phone number. Helps speeding up searches and comparisons.")
    phone_sanitized_blacklisted: Optional[bool] = Field(None, alias="phone_sanitized_blacklisted", title="Phone Blacklisted", description="If the sanitized phone number is on the blacklist, the contact won't receive mass mailing sms anymore, from any list")
    phone_blacklisted: Optional[bool] = Field(None, alias="phone_blacklisted", title="Blacklisted Phone is Phone", description="Indicates if a blacklisted sanitized phone number is a phone number. Helps distinguish which number is blacklisted             when there is both a mobile and phone field in a model.")
    mobile_blacklisted: Optional[bool] = Field(None, alias="mobile_blacklisted", title="Blacklisted Phone Is Mobile", description="Indicates if a blacklisted sanitized phone number is a mobile number. Helps distinguish which number is blacklisted             when there is both a mobile and phone field in a model.")
    phone_mobile_search: Optional[str] = Field(None, alias="phone_mobile_search", title="Phone/Mobile", description="")
    payment_token_count: Optional[int] = Field(None, alias="payment_token_count", title="Payment Token Count", description="")
    user_livechat_username: Optional[str] = Field(None, alias="user_livechat_username", title="User Livechat Username", description="")
    website_description: Optional[Any] = Field(None, alias="website_description", title="Website Partner Full Description", description="")
    website_short_description: Optional[Any] = Field(None, alias="website_short_description", title="Website Partner Short Description", description="")
    sel_groups_2_4: Optional[Any] = Field(None, alias="sel_groups_2_4", title="Administration", description="")
    sel_groups_59_60: Optional[Any] = Field(None, alias="sel_groups_59_60", title="Live Chat", description="User: The user will be able to join support channels.\nAdministrator: The user will be able to delete support channels.")
    sel_groups_1_10_11: Optional[Any] = Field(None, alias="sel_groups_1_10_11", title="User types", description="Helps you manage users.\n\nPortal: Portal members have specific access rights (such as record rules and restricted menus).\n                They usually do not belong to the usual Odoo groups.\nPublic: Public users have specific access rights (such as record rules and restricted menus).\n                They usually do not belong to the usual Odoo groups.")
    sel_groups_14_15: Optional[Any] = Field(None, alias="sel_groups_14_15", title="Website", description="")
    sel_groups_35: Optional[Any] = Field(None, alias="sel_groups_35", title="Dashboard", description="User access level for Dashboard module")
    in_group_8: Optional[bool] = Field(None, alias="in_group_8", title="Access to export feature", description="")
    in_group_21: Optional[bool] = Field(None, alias="in_group_21", title="Advanced Pricelists", description="")
    in_group_19: Optional[bool] = Field(None, alias="in_group_19", title="Analytic Accounting", description="")
    in_group_20: Optional[bool] = Field(None, alias="in_group_20", title="Basic Pricelists", description="")
    in_group_24: Optional[bool] = Field(None, alias="in_group_24", title="Discount on lines", description="")
    in_group_12: Optional[bool] = Field(None, alias="in_group_12", title="Mail Template Editor", description="")
    in_group_18: Optional[bool] = Field(None, alias="in_group_18", title="Manage Multiple Units of Measure", description="")
    in_group_22: Optional[bool] = Field(None, alias="in_group_22", title="Manage Product Packaging", description="")
    in_group_23: Optional[bool] = Field(None, alias="in_group_23", title="Manage Product Variants", description="")
    in_group_17: Optional[bool] = Field(None, alias="in_group_17", title="Multi-website", description="")
    in_group_16: Optional[bool] = Field(None, alias="in_group_16", title="Public access to arbitrary exposed model", description="")
    in_group_13: Optional[bool] = Field(None, alias="in_group_13", title="Receive notifications in Odoo", description="")
    in_group_9: Optional[bool] = Field(None, alias="in_group_9", title="Contact Creation", description="")
    in_group_5: Optional[bool] = Field(None, alias="in_group_5", title="Multi Companies", description="")
    in_group_6: Optional[bool] = Field(None, alias="in_group_6", title="Multi Currencies", description="")
    in_group_7: Optional[bool] = Field(None, alias="in_group_7", title="Technical Features", description="")
    in_group_3: Optional[bool] = Field(None, alias="in_group_3", title="Bypass HTML Field Sanitize", description="")

    class ConfigDict:
        from_attributes = True

    @classmethod
    def from_execute_kw(cls, item:dict) -> 'UserModel':
        filtered_item = {}
        schema = UserModel.model_json_schema()

        for key in item.keys():
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
    def list_from_execute_kw(cls, data:List[dict], fields:List[str] = []) -> List['UserModel']:
        transformed = []
        schema = UserModel.model_json_schema()
        
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
