
from pydantic import BaseModel, Field
from typing import Optional, List, Any, Dict

class ProductUnitofMeasureModel(BaseModel):
    id: Optional[int] = Field(None, alias="id", title="ID", description="")
    name: str = Field("", alias="name", title="Unit of Measure", description="")
    factor: Any = Field(None, alias="factor", title="Ratio", description="How much bigger or smaller this unit is compared to the reference Unit of Measure for this category: 1 * (reference unit) = ratio * (this unit)")
    factor_inv: Any = Field(None, alias="factor_inv", title="Bigger Ratio", description="How many times this Unit of Measure is bigger than the reference Unit of Measure in this category: 1 * (this unit) = ratio * (reference unit)")
    rounding: Any = Field(None, alias="rounding", title="Rounding Precision", description="The computed quantity will be a multiple of this value. Use 1.0 for a Unit of Measure that cannot be further split, such as a piece.")
    uom_type: Any = Field(None, alias="uom_type", title="Type", description="")
    category_id: int = Field(0, alias="category_id", title="Category", description="Conversion between Units of Measure can only occur if they belong to the same category. The conversion will be made based on the ratios.")
    active: Optional[bool] = Field(None, alias="active", title="Active", description="Uncheck the active field to disable a unit of measure without deleting it.")
    ratio: Optional[Any] = Field(None, alias="ratio", title="Combined Ratio", description="")
    color: Optional[int] = Field(None, alias="color", title="Color", description="")
    display_name: Optional[str] = Field(None, alias="display_name", title="Display Name", description="")
    create_uid: Optional[int] = Field(None, alias="create_uid", title="Created by", description="")
    create_date: Optional[str] = Field(None, alias="create_date", title="Created on", description="")
    write_uid: Optional[int] = Field(None, alias="write_uid", title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, alias="write_date", title="Last Updated on", description="")

    class ConfigDict:
        from_attributes = True

    @classmethod
    def from_execute_kw(cls, item:Dict[str, Any]) -> 'ProductUnitofMeasureModel':
        filtered_item = {}
        schema = ProductUnitofMeasureModel.model_json_schema()

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
    def list_from_execute_kw(cls, data:List[dict], fields:List[str] = []) -> List['ProductUnitofMeasureModel']:
        transformed = []
        schema = ProductUnitofMeasureModel.model_json_schema()
        
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
