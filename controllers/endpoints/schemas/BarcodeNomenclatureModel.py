
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class BarcodeNomenclatureModel(BaseModel):
    id: Optional[int] = Field(None, alias="id", title="ID", description="")
    name: str = Field("", alias="name", title="Barcode Nomenclature", description="An internal identification of the barcode nomenclature")
    upc_ean_conv: Any = Field(None, alias="upc_ean_conv", title="UPC/EAN Conversion", description="UPC Codes can be converted to EAN by prefixing them with a zero. This setting determines if a UPC/EAN barcode should be automatically converted in one way or another when trying to match a rule with the other encoding.")
    rule_ids: Optional[List[int]] = Field(None, alias="rule_ids", title="Rules", description="The list of barcode rules")
    display_name: Optional[str] = Field(None, alias="display_name", title="Display Name", description="")
    create_uid: Optional[int] = Field(None, alias="create_uid", title="Created by", description="")
    create_date: Optional[str] = Field(None, alias="create_date", title="Created on", description="")
    write_uid: Optional[int] = Field(None, alias="write_uid", title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, alias="write_date", title="Last Updated on", description="")
    is_gs1_nomenclature: Optional[bool] = Field(None, alias="is_gs1_nomenclature", title="Is GS1 Nomenclature", description="This Nomenclature use the GS1 specification, only GS1-128 encoding rules is accepted is this kind of nomenclature.")
    gs1_separator_fnc1: Optional[str] = Field(None, alias="gs1_separator_fnc1", title="FNC1 Separator", description="Alternative regex delimiter for the FNC1. The separator must not match the begin/end of any related rules pattern.")

    class ConfigDict:
        from_attributes = True

    @classmethod
    def from_execute_kw(cls, item:dict) -> 'BarcodeNomenclatureModel':
        filtered_item = {}
        schema = BarcodeNomenclatureModel.model_json_schema()

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
    def list_from_execute_kw(cls, data:List[dict], fields:List[str] = []) -> List['BarcodeNomenclatureModel']:
        transformed = []
        schema = BarcodeNomenclatureModel.model_json_schema()
        
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
