
from pydantic import BaseModel, Field
from typing import Optional, List, Any, Dict

class ProductVariantModel(BaseModel):
    id: Optional[int] = Field(None, alias="id", title="ID", description="")
    name: str = Field("", alias="name", title="Name", description="")
    detailed_type: Any = Field(None, alias="detailed_type", title="Product Type", description="A storable product is a product for which you manage stock. The Inventory app has to be installed.\nA consumable product is a product for which stock is not managed.\nA service is a non-material product you provide.")
    activity_user_id: Optional[int] = Field(None, alias="activity_user_id", title="Responsible User", description="")
    activity_type_id: Optional[int] = Field(None, alias="activity_type_id", title="Next Activity Type", description="")
    product_tmpl_id: int = Field(0, alias="product_tmpl_id", title="Product Template", description="")
    categ_id: int = Field(0, alias="categ_id", title="Product Category", description="")
    currency_id: Optional[int] = Field(None, alias="currency_id", title="Currency", description="")
    cost_currency_id: Optional[int] = Field(None, alias="cost_currency_id", title="Cost Currency", description="")
    uom_id: int = Field(0, alias="uom_id", title="Unit of Measure", description="Default unit of measure used for all stock operations.")
    uom_po_id: int = Field(0, alias="uom_po_id", title="Purchase UoM", description="Default unit of measure used for purchase orders. It must be in the same category as the default unit of measure.")
    company_id: Optional[int] = Field(None, alias="company_id", title="Company", description="")
    product_variant_id: Optional[int] = Field(None, alias="product_variant_id", title="Product", description="")
    activity_ids: Optional[List[int]] = Field(None, alias="activity_ids", title="Activities", description="")
    message_follower_ids: Optional[List[int]] = Field(None, alias="message_follower_ids", title="Followers", description="")
    message_partner_ids: Optional[List[int]] = Field(None, alias="message_partner_ids", title="Followers (Partners)", description="")
    message_ids: Optional[List[int]] = Field(None, alias="message_ids", title="Messages", description="")
    rating_ids: Optional[List[int]] = Field(None, alias="rating_ids", title="Ratings", description="")
    website_message_ids: Optional[List[int]] = Field(None, alias="website_message_ids", title="Website Messages", description="Website communication history")
    product_template_attribute_value_ids: Optional[List[int]] = Field(None, alias="product_template_attribute_value_ids", title="Attribute Values", description="")
    product_template_variant_value_ids: Optional[List[int]] = Field(None, alias="product_template_variant_value_ids", title="Variant Values", description="")
    product_document_ids: Optional[List[int]] = Field(None, alias="product_document_ids", title="Documents", description="")
    packaging_ids: Optional[List[int]] = Field(None, alias="packaging_ids", title="Product Packages", description="Gives the different ways to package the same product.")
    additional_product_tag_ids: Optional[List[int]] = Field(None, alias="additional_product_tag_ids", title="Additional Product Tags", description="")
    all_product_tag_ids: Optional[List[int]] = Field(None, alias="all_product_tag_ids", title="All Product Tag", description="")
    seller_ids: Optional[List[int]] = Field(None, alias="seller_ids", title="Vendors", description="")
    variant_seller_ids: Optional[List[int]] = Field(None, alias="variant_seller_ids", title="Variant Seller", description="")
    attribute_line_ids: Optional[List[int]] = Field(None, alias="attribute_line_ids", title="Product Attributes", description="")
    valid_product_template_attribute_line_ids: Optional[List[int]] = Field(None, alias="valid_product_template_attribute_line_ids", title="Valid Product Attribute Lines", description="")
    product_variant_ids: List[int] = Field([], alias="product_variant_ids", title="Products", description="")
    product_tag_ids: Optional[List[int]] = Field(None, alias="product_tag_ids", title="Product Template Tags", description="")
    activity_state: Optional[Any] = Field(None, alias="activity_state", title="Activity State", description="Status based on activities\nOverdue: Due date is already passed\nToday: Activity date is today\nPlanned: Future activities.")
    activity_type_icon: Optional[str] = Field(None, alias="activity_type_icon", title="Activity Type Icon", description="Font awesome icon e.g. fa-tasks")
    activity_date_deadline: Optional[str] = Field(None, alias="activity_date_deadline", title="Next Activity Deadline", description="")
    my_activity_date_deadline: Optional[str] = Field(None, alias="my_activity_date_deadline", title="My Activity Deadline", description="")
    activity_summary: Optional[str] = Field(None, alias="activity_summary", title="Next Activity Summary", description="")
    activity_exception_decoration: Optional[Any] = Field(None, alias="activity_exception_decoration", title="Activity Exception Decoration", description="Type of the exception activity on record.")
    activity_exception_icon: Optional[str] = Field(None, alias="activity_exception_icon", title="Icon", description="Icon to indicate an exception activity.")
    message_is_follower: Optional[bool] = Field(None, alias="message_is_follower", title="Is Follower", description="")
    has_message: Optional[bool] = Field(None, alias="has_message", title="Has Message", description="")
    message_needaction: Optional[bool] = Field(None, alias="message_needaction", title="Action Needed", description="If checked, new messages require your attention.")
    message_needaction_counter: Optional[int] = Field(None, alias="message_needaction_counter", title="Number of Actions", description="Number of messages requiring action")
    message_has_error: Optional[bool] = Field(None, alias="message_has_error", title="Message Delivery error", description="If checked, some messages have a delivery error.")
    message_has_error_counter: Optional[int] = Field(None, alias="message_has_error_counter", title="Number of errors", description="Number of messages with delivery error")
    message_attachment_count: Optional[int] = Field(None, alias="message_attachment_count", title="Attachment Count", description="")
    message_has_sms_error: Optional[bool] = Field(None, alias="message_has_sms_error", title="SMS Delivery error", description="If checked, some messages have a delivery error.")
    price_extra: Optional[Any] = Field(None, alias="price_extra", title="Variant Price Extra", description="This is the sum of the extra price of all attributes")
    lst_price: Optional[Any] = Field(None, alias="lst_price", title="Sales Price", description="The sale price is managed from the product template. Click on the 'Configure Variants' button to set the extra attribute prices.")
    default_code: Optional[str] = Field(None, alias="default_code", title="Internal Reference", description="")
    code: Optional[str] = Field(None, alias="code", title="Reference", description="")
    partner_ref: Optional[str] = Field(None, alias="partner_ref", title="Customer Ref", description="")
    active: Optional[bool] = Field(None, alias="active", title="Active", description="If unchecked, it will allow you to hide the product without removing it.")
    barcode: Optional[str] = Field(None, alias="barcode", title="Barcode", description="International Article Number used for product identification.")
    combination_indices: Optional[str] = Field(None, alias="combination_indices", title="Combination Indices", description="")
    is_product_variant: Optional[bool] = Field(None, alias="is_product_variant", title="Is Product Variant", description="")
    standard_price: Optional[Any] = Field(None, alias="standard_price", title="Cost", description="Value of the product (automatically computed in AVCO).\n        Used to value the product when the purchase cost is not known (e.g. inventory adjustment).\n        Used to compute margins on sale orders.")
    volume: Optional[Any] = Field(None, alias="volume", title="Volume", description="")
    weight: Optional[Any] = Field(None, alias="weight", title="Weight", description="")
    pricelist_item_count: Optional[int] = Field(None, alias="pricelist_item_count", title="Number of price rules", description="")
    product_document_count: Optional[int] = Field(None, alias="product_document_count", title="Documents Count", description="")
    image_variant_1920: Optional[Any] = Field(None, alias="image_variant_1920", title="Variant Image", description="")
    image_variant_1024: Optional[Any] = Field(None, alias="image_variant_1024", title="Variant Image 1024", description="")
    image_variant_512: Optional[Any] = Field(None, alias="image_variant_512", title="Variant Image 512", description="")
    image_variant_256: Optional[Any] = Field(None, alias="image_variant_256", title="Variant Image 256", description="")
    image_variant_128: Optional[Any] = Field(None, alias="image_variant_128", title="Variant Image 128", description="")
    can_image_variant_1024_be_zoomed: Optional[bool] = Field(None, alias="can_image_variant_1024_be_zoomed", title="Can Variant Image 1024 be zoomed", description="")
    image_1920: Optional[Any] = Field(None, alias="image_1920", title="Image", description="")
    image_1024: Optional[Any] = Field(None, alias="image_1024", title="Image 1024", description="")
    image_512: Optional[Any] = Field(None, alias="image_512", title="Image 512", description="")
    image_256: Optional[Any] = Field(None, alias="image_256", title="Image 256", description="")
    image_128: Optional[Any] = Field(None, alias="image_128", title="Image 128", description="")
    can_image_1024_be_zoomed: Optional[bool] = Field(None, alias="can_image_1024_be_zoomed", title="Can Image 1024 be zoomed", description="")
    write_date: Optional[str] = Field(None, alias="write_date", title="Write Date", description="")
    display_name: Optional[str] = Field(None, alias="display_name", title="Display Name", description="")
    create_uid: Optional[int] = Field(None, alias="create_uid", title="Created by", description="")
    create_date: Optional[str] = Field(None, alias="create_date", title="Created on", description="")
    write_uid: Optional[int] = Field(None, alias="write_uid", title="Last Updated by", description="")
    sequence: Optional[int] = Field(None, alias="sequence", title="Sequence", description="Gives the sequence order when displaying a product list")
    description: Optional[Any] = Field(None, alias="description", title="Description", description="")
    description_purchase: Optional[Any] = Field(None, alias="description_purchase", title="Purchase Description", description="")
    description_sale: Optional[Any] = Field(None, alias="description_sale", title="Sales Description", description="A description of the Product that you want to communicate to your customers. This description will be copied to every Sales Order, Delivery Order and Customer Invoice/Credit Note")
    type: Optional[Any] = Field(None, alias="type", title="Type", description="")
    list_price: Optional[Any] = Field(None, alias="list_price", title="Sales Price", description="Price at which the product is sold to customers.")
    volume_uom_name: Optional[str] = Field(None, alias="volume_uom_name", title="Volume unit of measure label", description="")
    weight_uom_name: Optional[str] = Field(None, alias="weight_uom_name", title="Weight unit of measure label", description="")
    sale_ok: Optional[bool] = Field(None, alias="sale_ok", title="Can be Sold", description="")
    purchase_ok: Optional[bool] = Field(None, alias="purchase_ok", title="Can be Purchased", description="")
    uom_name: Optional[str] = Field(None, alias="uom_name", title="Unit of Measure Name", description="")
    color: Optional[int] = Field(None, alias="color", title="Color Index", description="")
    product_variant_count: Optional[int] = Field(None, alias="product_variant_count", title="# Product Variants", description="")
    has_configurable_attributes: Optional[bool] = Field(None, alias="has_configurable_attributes", title="Is a configurable product", description="")
    product_tooltip: Optional[str] = Field(None, alias="product_tooltip", title="Product Tooltip", description="")
    priority: Optional[Any] = Field(None, alias="priority", title="Favorite", description="")
    product_properties: Optional[Any] = Field(None, alias="product_properties", title="Properties", description="")

    class ConfigDict:
        from_attributes = True

    @classmethod
    def from_execute_kw(cls, item:dict) -> 'ProductVariantModel':
        filtered_item = {}
        schema = ProductVariantModel.model_json_schema()

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
    def list_from_execute_kw(cls, data:List[dict], fields:List[str] = []) -> List['ProductVariantModel']:
        transformed = []
        schema = ProductVariantModel.model_json_schema()
        
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
