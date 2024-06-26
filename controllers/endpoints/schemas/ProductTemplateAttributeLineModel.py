
from pydantic import BaseModel, Field
from typing import Optional, List, Any, Dict

class ProductTemplateAttributeLineModel(BaseModel):
    id: Optional[int] = Field(None, alias="id", title="ID", description="")
    product_tmpl_id: int = Field(0, alias="product_tmpl_id", title="Product Template", description="")
    attribute_id: int = Field(0, alias="attribute_id", title="Attribute", description="")
    value_ids: Optional[List[int]] = Field(None, alias="value_ids", title="Values", description="")
    product_template_value_ids: Optional[List[int]] = Field(None, alias="product_template_value_ids", title="Product Attribute Values", description="")
    active: Optional[bool] = Field(None, alias="active", title="Active", description="")
    sequence: Optional[int] = Field(None, alias="sequence", title="Sequence", description="")
    value_count: Optional[int] = Field(None, alias="value_count", title="Value Count", description="")
    display_name: Optional[str] = Field(None, alias="display_name", title="Display Name", description="")
    create_uid: Optional[int] = Field(None, alias="create_uid", title="Created by", description="")
    create_date: Optional[str] = Field(None, alias="create_date", title="Created on", description="")
    write_uid: Optional[int] = Field(None, alias="write_uid", title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, alias="write_date", title="Last Updated on", description="")

    class ConfigDict:
        from_attributes = True

    @classmethod
    def from_execute_kw(cls, item:Dict[str, Any]) -> 'ProductTemplateAttributeLineModel':
        filtered_item = {}
        schema = ProductTemplateAttributeLineModel.model_json_schema()

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
    def list_from_execute_kw(cls, data:List[dict], fields:List[str] = []) -> List['ProductTemplateAttributeLineModel']:
        transformed = []
        schema = ProductTemplateAttributeLineModel.model_json_schema()
        
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
