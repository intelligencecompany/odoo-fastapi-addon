
from pydantic import BaseModel, Field
from typing import Optional, List, Any, Dict

class BarcodeRuleModel(BaseModel):
    id: Optional[int] = Field(None, alias="id", title="ID", description="")
    name: str = Field("", alias="name", title="Rule Name", description="An internal identification for this barcode nomenclature rule")
    encoding: Any = Field(None, alias="encoding", title="Encoding", description="This rule will apply only if the barcode is encoded with the specified encoding")
    type: Any = Field(None, alias="type", title="Type", description="")
    pattern: str = Field("", alias="pattern", title="Barcode Pattern", description="The barcode matching pattern")
    alias: str = Field("", alias="alias", title="Alias", description="The matched pattern will alias to this barcode")
    barcode_nomenclature_id: Optional[int] = Field(None, alias="barcode_nomenclature_id", title="Barcode Nomenclature", description="")
    associated_uom_id: Optional[int] = Field(None, alias="associated_uom_id", title="Associated Uom", description="")
    sequence: Optional[int] = Field(None, alias="sequence", title="Sequence", description="Used to order rules such that rules with a smaller sequence match first")
    display_name: Optional[str] = Field(None, alias="display_name", title="Display Name", description="")
    create_uid: Optional[int] = Field(None, alias="create_uid", title="Created by", description="")
    create_date: Optional[str] = Field(None, alias="create_date", title="Created on", description="")
    write_uid: Optional[int] = Field(None, alias="write_uid", title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, alias="write_date", title="Last Updated on", description="")
    is_gs1_nomenclature: Optional[bool] = Field(None, alias="is_gs1_nomenclature", title="Is GS1 Nomenclature", description="This Nomenclature use the GS1 specification, only GS1-128 encoding rules is accepted is this kind of nomenclature.")
    gs1_content_type: Optional[Any] = Field(None, alias="gs1_content_type", title="GS1 Content Type", description="The GS1 content type defines what kind of data the rule will process the barcode as:        * Date: the barcode will be converted into a Odoo datetime;        * Measure: the barcode's value is related to a specific UoM;        * Numeric Identifier: fixed length barcode following a specific encoding;        * Alpha-Numeric Name: variable length barcode.")
    gs1_decimal_usage: Optional[bool] = Field(None, alias="gs1_decimal_usage", title="Decimal", description="If True, use the last digit of AI to determine where the first decimal is")

    class ConfigDict:
        from_attributes = True

    @classmethod
    def from_execute_kw(cls, item:Dict[str, Any]) -> 'BarcodeRuleModel':
        filtered_item = {}
        schema = BarcodeRuleModel.model_json_schema()

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
    def list_from_execute_kw(cls, data:List[dict], fields:List[str] = []) -> List['BarcodeRuleModel']:
        transformed = []
        schema = BarcodeRuleModel.model_json_schema()
        
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
