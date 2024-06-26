
from pydantic import BaseModel, Field
from typing import Optional, List, Any, Dict

class AttributeValueModel(BaseModel):
    id: Optional[int] = Field(None, alias="id", title="ID", description="")
    name: str = Field("", alias="name", title="Value", description="")
    attribute_id: int = Field(0, alias="attribute_id", title="Attribute", description="The attribute cannot be changed once the value is used on at least one product.")
    pav_attribute_line_ids: Optional[List[int]] = Field(None, alias="pav_attribute_line_ids", title="Lines", description="")
    sequence: Optional[int] = Field(None, alias="sequence", title="Sequence", description="Determine the display order")
    is_used_on_products: Optional[bool] = Field(None, alias="is_used_on_products", title="Used on Products", description="")
    default_extra_price: Optional[Any] = Field(None, alias="default_extra_price", title="Default Extra Price", description="")
    is_custom: Optional[bool] = Field(None, alias="is_custom", title="Is custom value", description="Allow users to input custom values for this attribute value")
    html_color: Optional[str] = Field(None, alias="html_color", title="Color", description="Here you can set a specific HTML color index (e.g. #ff0000) to display the color if the attribute type is 'Color'.")
    display_type: Optional[Any] = Field(None, alias="display_type", title="Display Type", description="The display type used in the Product Configurator.")
    color: Optional[int] = Field(None, alias="color", title="Color Index", description="")
    image: Optional[Any] = Field(None, alias="image", title="Image", description="You can upload an image that will be used as the color of the attribute value.")
    display_name: Optional[str] = Field(None, alias="display_name", title="Display Name", description="")
    create_uid: Optional[int] = Field(None, alias="create_uid", title="Created by", description="")
    create_date: Optional[str] = Field(None, alias="create_date", title="Created on", description="")
    write_uid: Optional[int] = Field(None, alias="write_uid", title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, alias="write_date", title="Last Updated on", description="")

    class ConfigDict:
        from_attributes = True

    @classmethod
    def from_execute_kw(cls, item:Dict[str, Any]) -> 'AttributeValueModel':
        filtered_item = {}
        schema = AttributeValueModel.model_json_schema()

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
    def list_from_execute_kw(cls, data:List[dict], fields:List[str] = []) -> List['AttributeValueModel']:
        transformed = []
        schema = AttributeValueModel.model_json_schema()
        
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
