
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class ChoosethesheetlayouttoprintthelabelsModel(BaseModel):
    id: Optional[int] = Field(None, alias="id", title="ID", description="")
    print_format: Any = Field(None, alias="print_format", title="Format", description="")
    custom_quantity: int = Field(0, alias="custom_quantity", title="Quantity", description="")
    pricelist_id: Optional[int] = Field(None, alias="pricelist_id", title="Pricelist", description="")
    product_ids: Optional[List[int]] = Field(None, alias="product_ids", title="Product", description="")
    product_tmpl_ids: Optional[List[int]] = Field(None, alias="product_tmpl_ids", title="Product Tmpl", description="")
    extra_html: Optional[Any] = Field(None, alias="extra_html", title="Extra Content", description="")
    rows: Optional[int] = Field(None, alias="rows", title="Rows", description="")
    columns: Optional[int] = Field(None, alias="columns", title="Columns", description="")
    display_name: Optional[str] = Field(None, alias="display_name", title="Display Name", description="")
    create_uid: Optional[int] = Field(None, alias="create_uid", title="Created by", description="")
    create_date: Optional[str] = Field(None, alias="create_date", title="Created on", description="")
    write_uid: Optional[int] = Field(None, alias="write_uid", title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, alias="write_date", title="Last Updated on", description="")

    class ConfigDict:
        from_attributes = True

    @classmethod
    def from_execute_kw(cls, data:List[dict], fields:List[str] = []) -> List['ChoosethesheetlayouttoprintthelabelsModel']:
        transformed = []
        schema = ChoosethesheetlayouttoprintthelabelsModel.model_json_schema()
        
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
