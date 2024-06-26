
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class SequenceModel(BaseModel):
    id: Optional[int] = Field(None, alias="id", title="ID", description="")
    name: str = Field("", alias="name", title="Name", description="")
    implementation: Any = Field(None, alias="implementation", title="Implementation", description="While assigning a sequence number to a record, the 'no gap' sequence implementation ensures that each previous sequence number has been assigned already. While this sequence implementation will not skip any sequence number upon assignment, there can still be gaps in the sequence if records are deleted. The 'no gap' implementation is slower than the standard one.")
    number_next: int = Field(0, alias="number_next", title="Next Number", description="Next number of this sequence")
    number_increment: int = Field(0, alias="number_increment", title="Step", description="The next number of the sequence will be incremented by this number")
    padding: int = Field(0, alias="padding", title="Sequence Size", description="Odoo will automatically adds some '0' on the left of the 'Next Number' to get the required padding size.")
    company_id: Optional[int] = Field(None, alias="company_id", title="Company", description="")
    date_range_ids: Optional[List[int]] = Field(None, alias="date_range_ids", title="Subsequences", description="")
    code: Optional[str] = Field(None, alias="code", title="Sequence Code", description="")
    active: Optional[bool] = Field(None, alias="active", title="Active", description="")
    prefix: Optional[str] = Field(None, alias="prefix", title="Prefix", description="Prefix value of the record for the sequence")
    suffix: Optional[str] = Field(None, alias="suffix", title="Suffix", description="Suffix value of the record for the sequence")
    number_next_actual: Optional[int] = Field(None, alias="number_next_actual", title="Actual Next Number", description="Next number that will be used. This number can be incremented frequently so the displayed value might already be obsolete")
    use_date_range: Optional[bool] = Field(None, alias="use_date_range", title="Use subsequences per date_range", description="")
    display_name: Optional[str] = Field(None, alias="display_name", title="Display Name", description="")
    create_uid: Optional[int] = Field(None, alias="create_uid", title="Created by", description="")
    create_date: Optional[str] = Field(None, alias="create_date", title="Created on", description="")
    write_uid: Optional[int] = Field(None, alias="write_uid", title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, alias="write_date", title="Last Updated on", description="")

    class Config:
        from_attributes = True

    @classmethod
    def from_execute_kw(cls, data:List[dict], fields:List[str] = []) -> List['SequenceModel']:
        transformed = []
        schema = SequenceModel.model_json_schema()
        
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
