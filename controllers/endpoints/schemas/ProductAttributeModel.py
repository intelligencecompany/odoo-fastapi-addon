
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class ProductAttributeModel(BaseModel):
    id: Optional[int] = Field(None, alias="id", title="ID", description="")
    name: str = Field("", alias="name", title="Attribute", description="")
    create_variant: Any = Field(None, alias="create_variant", title="Variants Creation Mode", description="- Instantly: All possible variants are created as soon as the attribute and its values are added to a product.\n        - Dynamically: Each variant is created only when its corresponding attributes and values are added to a sales order.\n        - Never: Variants are never created for the attribute.\n        Note: the variants creation mode cannot be changed once the attribute is used on at least one product.")
    display_type: Any = Field(None, alias="display_type", title="Display Type", description="The display type used in the Product Configurator.")
    value_ids: Optional[List[int]] = Field(None, alias="value_ids", title="Values", description="")
    attribute_line_ids: Optional[List[int]] = Field(None, alias="attribute_line_ids", title="Lines", description="")
    product_tmpl_ids: Optional[List[int]] = Field(None, alias="product_tmpl_ids", title="Related Products", description="")
    sequence: Optional[int] = Field(None, alias="sequence", title="Sequence", description="Determine the display order")
    number_related_products: Optional[int] = Field(None, alias="number_related_products", title="Number Related Products", description="")
    display_name: Optional[str] = Field(None, alias="display_name", title="Display Name", description="")
    create_uid: Optional[int] = Field(None, alias="create_uid", title="Created by", description="")
    create_date: Optional[str] = Field(None, alias="create_date", title="Created on", description="")
    write_uid: Optional[int] = Field(None, alias="write_uid", title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, alias="write_date", title="Last Updated on", description="")

    class ConfigDict:
        from_attributes = True

    @classmethod
    def from_execute_kw(cls, item:dict[str, any]) -> 'ProductAttributeModel':
        filtered_item = {}
        schema = ProductAttributeModel.model_json_schema()

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
    def list_from_execute_kw(cls, data:List[dict], fields:List[str] = []) -> List['ProductAttributeModel']:
        transformed = []
        schema = ProductAttributeModel.model_json_schema()
        
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
