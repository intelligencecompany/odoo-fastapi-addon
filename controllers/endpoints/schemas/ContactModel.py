
from pydantic import BaseModel, Field
from typing import Optional, List, Any, Dict

class ContactModel(BaseModel):
    id: Optional[int] = Field(None, alias="id", title="ID", description="")
    website_id: Optional[int] = Field(None, alias="website_id", title="Website", description="Restrict publishing to this website.")
    activity_user_id: Optional[int] = Field(None, alias="activity_user_id", title="Responsible User", description="")
    activity_type_id: Optional[int] = Field(None, alias="activity_type_id", title="Next Activity Type", description="")
    parent_id: Optional[int] = Field(None, alias="parent_id", title="Related Company", description="")
    user_id: Optional[int] = Field(None, alias="user_id", title="Salesperson", description="The internal user in charge of this contact.")
    same_vat_partner_id: Optional[int] = Field(None, alias="same_vat_partner_id", title="Partner with same Tax ID", description="")
    same_company_registry_partner_id: Optional[int] = Field(None, alias="same_company_registry_partner_id", title="Partner with same Company Registry", description="")
    category_id: Optional[List[int]] = Field(None, alias="category_id", title="Tags", description="")
    state_id: Optional[int] = Field(None, alias="state_id", title="State", description="")
    country_id: Optional[int] = Field(None, alias="country_id", title="Country", description="")
    industry_id: Optional[int] = Field(None, alias="industry_id", title="Industry", description="")
    company_id: Optional[int] = Field(None, alias="company_id", title="Company", description="")
    commercial_partner_id: Optional[int] = Field(None, alias="commercial_partner_id", title="Commercial Entity", description="")
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
    payment_token_ids: Optional[List[int]] = Field(None, alias="payment_token_ids", title="Payment Tokens", description="")
    visitor_ids: Optional[List[int]] = Field(None, alias="visitor_ids", title="Visitors", description="")
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
    name: Optional[str] = Field(None, alias="name", title="Name", description="")
    complete_name: Optional[str] = Field(None, alias="complete_name", title="Complete Name", description="")
    date: Optional[str] = Field(None, alias="date", title="Date", description="")
    title: Optional[int] = Field(None, alias="title", title="Title", description="")
    parent_name: Optional[str] = Field(None, alias="parent_name", title="Parent name", description="")
    ref: Optional[str] = Field(None, alias="ref", title="Reference", description="")
    lang: Optional[Any] = Field(None, alias="lang", title="Language", description="All the emails and documents sent to this contact will be translated in this language.")
    active_lang_count: Optional[int] = Field(None, alias="active_lang_count", title="Active Lang Count", description="")
    tz: Optional[Any] = Field(None, alias="tz", title="Timezone", description="When printing documents and exporting/importing data, time values are computed according to this timezone.\nIf the timezone is not set, UTC (Coordinated Universal Time) is used.\nAnywhere else, time values are computed according to the time offset of your web client.")
    tz_offset: Optional[str] = Field(None, alias="tz_offset", title="Timezone offset", description="")
    vat: Optional[str] = Field(None, alias="vat", title="Tax ID", description="The Tax Identification Number. Values here will be validated based on the country format. You can use '/' to indicate that the partner is not subject to tax.")
    company_registry: Optional[str] = Field(None, alias="company_registry", title="Company ID", description="The registry number of the company. Use it if it is different from the Tax ID. It must be unique across all partners of a same country")
    website: Optional[str] = Field(None, alias="website", title="Website Link", description="")
    comment: Optional[Any] = Field(None, alias="comment", title="Notes", description="")
    active: Optional[bool] = Field(None, alias="active", title="Active", description="")
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
    email: Optional[str] = Field(None, alias="email", title="Email", description="")
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
    display_name: Optional[str] = Field(None, alias="display_name", title="Display Name", description="")
    create_uid: Optional[int] = Field(None, alias="create_uid", title="Created by", description="")
    create_date: Optional[str] = Field(None, alias="create_date", title="Created on", description="")
    write_uid: Optional[int] = Field(None, alias="write_uid", title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, alias="write_date", title="Last Updated on", description="")
    im_status: Optional[str] = Field(None, alias="im_status", title="IM Status", description="")
    date_localization: Optional[str] = Field(None, alias="date_localization", title="Geolocation Date", description="")
    contact_address_inline: Optional[str] = Field(None, alias="contact_address_inline", title="Inlined Complete Address", description="")
    signup_token: Optional[str] = Field(None, alias="signup_token", title="Signup Token", description="")
    signup_type: Optional[str] = Field(None, alias="signup_type", title="Signup Token Type", description="")
    signup_expiration: Optional[str] = Field(None, alias="signup_expiration", title="Signup Expiration", description="")
    signup_valid: Optional[bool] = Field(None, alias="signup_valid", title="Signup Token is Valid", description="")
    signup_url: Optional[str] = Field(None, alias="signup_url", title="Signup URL", description="")
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

    class ConfigDict:
        from_attributes = True

    @classmethod
    def from_execute_kw(cls, item:dict) -> 'ContactModel':
        filtered_item = {}
        schema = ContactModel.model_json_schema()

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
    def list_from_execute_kw(cls, data:List[dict], fields:List[str] = []) -> List['ContactModel']:
        transformed = []
        schema = ContactModel.model_json_schema()
        
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
