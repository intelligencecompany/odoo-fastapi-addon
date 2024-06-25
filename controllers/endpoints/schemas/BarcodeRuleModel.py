
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class BarcodeRuleModel(BaseModel):
    id: Optional[int] = Field(None, title="ID", description="")
    name: str = Field("", title="Rule Name", description="An internal identification for this barcode nomenclature rule")
    encoding: Any = Field(None, title="Encoding", description="This rule will apply only if the barcode is encoded with the specified encoding")
    type: Any = Field(None, title="Type", description="")
    pattern: str = Field("", title="Barcode Pattern", description="The barcode matching pattern")
    alias: str = Field("", title="Alias", description="The matched pattern will alias to this barcode")
    barcode_nomenclature_id: Optional[int] = Field(None, title="Barcode Nomenclature", description="")
    associated_uom_id: Optional[int] = Field(None, title="Associated Uom", description="")
    sequence: Optional[int] = Field(None, title="Sequence", description="Used to order rules such that rules with a smaller sequence match first")
    display_name: Optional[str] = Field(None, title="Display Name", description="")
    create_uid: Optional[int] = Field(None, title="Created by", description="")
    create_date: Optional[str] = Field(None, title="Created on", description="")
    write_uid: Optional[int] = Field(None, title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, title="Last Updated on", description="")
    is_gs1_nomenclature: Optional[bool] = Field(None, title="Is GS1 Nomenclature", description="This Nomenclature use the GS1 specification, only GS1-128 encoding rules is accepted is this kind of nomenclature.")
    gs1_content_type: Optional[Any] = Field(None, title="GS1 Content Type", description="The GS1 content type defines what kind of data the rule will process the barcode as:        * Date: the barcode will be converted into a Odoo datetime;        * Measure: the barcode's value is related to a specific UoM;        * Numeric Identifier: fixed length barcode following a specific encoding;        * Alpha-Numeric Name: variable length barcode.")
    gs1_decimal_usage: Optional[bool] = Field(None, title="Decimal", description="If True, use the last digit of AI to determine where the first decimal is")

