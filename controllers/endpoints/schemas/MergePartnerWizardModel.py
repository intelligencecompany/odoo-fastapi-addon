
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class MergePartnerWizardModel(BaseModel):
    id: Optional[int] = Field(None, title="ID", description="")
    state: Any = Field(None, title="State", description="")
    group_by_parent_id: Optional[bool] = Field(None, title="Parent Company", description="")
    current_line_id: Optional[int] = Field(None, title="Current Line", description="")
    dst_partner_id: Optional[int] = Field(None, title="Destination Contact", description="")
    line_ids: Optional[List[int]] = Field(None, title="Lines", description="")
    partner_ids: Optional[List[int]] = Field(None, title="Contacts", description="")
    group_by_email: Optional[bool] = Field(None, title="Email", description="")
    group_by_name: Optional[bool] = Field(None, title="Name", description="")
    group_by_is_company: Optional[bool] = Field(None, title="Is Company", description="")
    group_by_vat: Optional[bool] = Field(None, title="VAT", description="")
    number_group: Optional[int] = Field(None, title="Group of Contacts", description="")
    exclude_contact: Optional[bool] = Field(None, title="A user associated to the contact", description="")
    exclude_journal_item: Optional[bool] = Field(None, title="Journal Items associated to the contact", description="")
    maximum_group: Optional[int] = Field(None, title="Maximum of Group of Contacts", description="")
    display_name: Optional[str] = Field(None, title="Display Name", description="")
    create_uid: Optional[int] = Field(None, title="Created by", description="")
    create_date: Optional[str] = Field(None, title="Created on", description="")
    write_uid: Optional[int] = Field(None, title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, title="Last Updated on", description="")

