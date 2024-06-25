
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class BarcodeNomenclatureModel(BaseModel):
    id: Optional[int] = Field(None, title="ID", description="")
    name: str = Field("", title="Barcode Nomenclature", description="An internal identification of the barcode nomenclature")
    upc_ean_conv: Any = Field(None, title="UPC/EAN Conversion", description="UPC Codes can be converted to EAN by prefixing them with a zero. This setting determines if a UPC/EAN barcode should be automatically converted in one way or another when trying to match a rule with the other encoding.")
    rule_ids: Optional[List[int]] = Field(None, title="Rules", description="The list of barcode rules")
    display_name: Optional[str] = Field(None, title="Display Name", description="")
    create_uid: Optional[int] = Field(None, title="Created by", description="")
    create_date: Optional[str] = Field(None, title="Created on", description="")
    write_uid: Optional[int] = Field(None, title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, title="Last Updated on", description="")
    is_gs1_nomenclature: Optional[bool] = Field(None, title="Is GS1 Nomenclature", description="This Nomenclature use the GS1 specification, only GS1-128 encoding rules is accepted is this kind of nomenclature.")
    gs1_separator_fnc1: Optional[str] = Field(None, title="FNC1 Separator", description="Alternative regex delimiter for the FNC1. The separator must not match the begin/end of any related rules pattern.")

