
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class ProductCategoryModel(BaseModel):
    id: Optional[int] = Field(None, alias="id", title="ID", description="")
    name: str = Field("", alias="name", title="Name", description="")
    parent_id: Optional[int] = Field(None, alias="parent_id", title="Parent Category", description="")
    child_id: Optional[List[int]] = Field(None, alias="child_id", title="Child Categories", description="")
    complete_name: Optional[str] = Field(None, alias="complete_name", title="Complete Name", description="")
    parent_path: Optional[str] = Field(None, alias="parent_path", title="Parent Path", description="")
    product_count: Optional[int] = Field(None, alias="product_count", title="# Products", description="The number of products under this category (Does not consider the children categories)")
    product_properties_definition: Optional[Any] = Field(None, alias="product_properties_definition", title="Product Properties", description="")
    display_name: Optional[str] = Field(None, alias="display_name", title="Display Name", description="")
    create_uid: Optional[int] = Field(None, alias="create_uid", title="Created by", description="")
    create_date: Optional[str] = Field(None, alias="create_date", title="Created on", description="")
    write_uid: Optional[int] = Field(None, alias="write_uid", title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, alias="write_date", title="Last Updated on", description="")

    class Config:
        from_attributes = True

    @classmethod
    def from_execute_kw(cls, data:List[dict], fields:List[str] = []) -> List['ProductCategoryModel']:
        transformed = []
        schema = ProductCategoryModel.model_json_schema()
        
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

            transformed.append(cls(**filtered_item))
        return transformed