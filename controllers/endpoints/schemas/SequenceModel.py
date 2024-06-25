
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class SequenceModel(BaseModel):
    id: Optional[int] = Field(None, title="ID", description="")
    name: str = Field("", title="Name", description="")
    implementation: Any = Field(None, title="Implementation", description="While assigning a sequence number to a record, the 'no gap' sequence implementation ensures that each previous sequence number has been assigned already. While this sequence implementation will not skip any sequence number upon assignment, there can still be gaps in the sequence if records are deleted. The 'no gap' implementation is slower than the standard one.")
    number_next: int = Field(0, title="Next Number", description="Next number of this sequence")
    number_increment: int = Field(0, title="Step", description="The next number of the sequence will be incremented by this number")
    padding: int = Field(0, title="Sequence Size", description="Odoo will automatically adds some '0' on the left of the 'Next Number' to get the required padding size.")
    company_id: Optional[int] = Field(None, title="Company", description="")
    date_range_ids: Optional[List[int]] = Field(None, title="Subsequences", description="")
    code: Optional[str] = Field(None, title="Sequence Code", description="")
    active: Optional[bool] = Field(None, title="Active", description="")
    prefix: Optional[str] = Field(None, title="Prefix", description="Prefix value of the record for the sequence")
    suffix: Optional[str] = Field(None, title="Suffix", description="Suffix value of the record for the sequence")
    number_next_actual: Optional[int] = Field(None, title="Actual Next Number", description="Next number that will be used. This number can be incremented frequently so the displayed value might already be obsolete")
    use_date_range: Optional[bool] = Field(None, title="Use subsequences per date_range", description="")
    display_name: Optional[str] = Field(None, title="Display Name", description="")
    create_uid: Optional[int] = Field(None, title="Created by", description="")
    create_date: Optional[str] = Field(None, title="Created on", description="")
    write_uid: Optional[int] = Field(None, title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, title="Last Updated on", description="")

