
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class ProductTemplateAttributeValueModel(BaseModel):
    id: Optional[int] = Field(None, alias="id", title="ID", description="")
    product_attribute_value_id: int = Field(0, alias="product_attribute_value_id", title="Attribute Value", description="")
    attribute_line_id: int = Field(0, alias="attribute_line_id", title="Attribute Line", description="")
    currency_id: Optional[int] = Field(None, alias="currency_id", title="Currency", description="")
    product_tmpl_id: Optional[int] = Field(None, alias="product_tmpl_id", title="Product Template", description="")
    attribute_id: Optional[int] = Field(None, alias="attribute_id", title="Attribute", description="")
    ptav_product_variant_ids: Optional[List[int]] = Field(None, alias="ptav_product_variant_ids", title="Related Variants", description="")
    ptav_active: Optional[bool] = Field(None, alias="ptav_active", title="Active", description="")
    name: Optional[str] = Field(None, alias="name", title="Value", description="")
    price_extra: Optional[Any] = Field(None, alias="price_extra", title="Value Price Extra", description="Extra price for the variant with this attribute value on sale price. eg. 200 price extra, 1000 + 200 = 1200.")
    exclude_for: Optional[List[int]] = Field(None, alias="exclude_for", title="Exclude for", description="Make this attribute value not compatible with other values of the product or some attribute values of optional and accessory products.")
    html_color: Optional[str] = Field(None, alias="html_color", title="HTML Color Index", description="Here you can set a specific HTML color index (e.g. #ff0000) to display the color if the attribute type is 'Color'.")
    is_custom: Optional[bool] = Field(None, alias="is_custom", title="Is custom value", description="Allow users to input custom values for this attribute value")
    display_type: Optional[Any] = Field(None, alias="display_type", title="Display Type", description="The display type used in the Product Configurator.")
    color: Optional[int] = Field(None, alias="color", title="Color", description="")
    image: Optional[Any] = Field(None, alias="image", title="Image", description="You can upload an image that will be used as the color of the attribute value.")
    display_name: Optional[str] = Field(None, alias="display_name", title="Display Name", description="")
    create_uid: Optional[int] = Field(None, alias="create_uid", title="Created by", description="")
    create_date: Optional[str] = Field(None, alias="create_date", title="Created on", description="")
    write_uid: Optional[int] = Field(None, alias="write_uid", title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, alias="write_date", title="Last Updated on", description="")

    class ConfigDict:
        from_attributes = True

    @classmethod
    def from_execute_kw(cls, item:dict) -> 'ProductTemplateAttributeValueModel':
        filtered_item = {}
        schema = ProductTemplateAttributeValueModel.model_json_schema()

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
    def list_from_execute_kw(cls, data:List[dict], fields:List[str] = []) -> List['ProductTemplateAttributeValueModel']:
        transformed = []
        schema = ProductTemplateAttributeValueModel.model_json_schema()
        
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
