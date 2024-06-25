
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class SequenceDateRangeModel(BaseModel):
    id: Optional[int] = Field(None, title="ID", description="")
    date_from: str = Field("", title="From", description="")
    date_to: str = Field("", title="To", description="")
    number_next: int = Field(0, title="Next Number", description="Next number of this sequence")
    sequence_id: int = Field(0, title="Main Sequence", description="")
    number_next_actual: Optional[int] = Field(None, title="Actual Next Number", description="Next number that will be used. This number can be incremented frequently so the displayed value might already be obsolete")
    display_name: Optional[str] = Field(None, title="Display Name", description="")
    create_uid: Optional[int] = Field(None, title="Created by", description="")
    create_date: Optional[str] = Field(None, title="Created on", description="")
    write_uid: Optional[int] = Field(None, title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, title="Last Updated on", description="")

