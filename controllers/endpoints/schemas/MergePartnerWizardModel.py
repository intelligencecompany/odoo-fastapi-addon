
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class MergePartnerWizardModel(BaseModel):
    id: Optional[int] = Field(None, alias="id", title="ID", description="")
    state: Any = Field(None, alias="state", title="State", description="")
    group_by_parent_id: Optional[bool] = Field(None, alias="group_by_parent_id", title="Parent Company", description="")
    current_line_id: Optional[int] = Field(None, alias="current_line_id", title="Current Line", description="")
    dst_partner_id: Optional[int] = Field(None, alias="dst_partner_id", title="Destination Contact", description="")
    line_ids: Optional[List[int]] = Field(None, alias="line_ids", title="Lines", description="")
    partner_ids: Optional[List[int]] = Field(None, alias="partner_ids", title="Contacts", description="")
    group_by_email: Optional[bool] = Field(None, alias="group_by_email", title="Email", description="")
    group_by_name: Optional[bool] = Field(None, alias="group_by_name", title="Name", description="")
    group_by_is_company: Optional[bool] = Field(None, alias="group_by_is_company", title="Is Company", description="")
    group_by_vat: Optional[bool] = Field(None, alias="group_by_vat", title="VAT", description="")
    number_group: Optional[int] = Field(None, alias="number_group", title="Group of Contacts", description="")
    exclude_contact: Optional[bool] = Field(None, alias="exclude_contact", title="A user associated to the contact", description="")
    exclude_journal_item: Optional[bool] = Field(None, alias="exclude_journal_item", title="Journal Items associated to the contact", description="")
    maximum_group: Optional[int] = Field(None, alias="maximum_group", title="Maximum of Group of Contacts", description="")
    display_name: Optional[str] = Field(None, alias="display_name", title="Display Name", description="")
    create_uid: Optional[int] = Field(None, alias="create_uid", title="Created by", description="")
    create_date: Optional[str] = Field(None, alias="create_date", title="Created on", description="")
    write_uid: Optional[int] = Field(None, alias="write_uid", title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, alias="write_date", title="Last Updated on", description="")

    class ConfigDict:
        from_attributes = True

    @classmethod
    def from_execute_kw(cls, item:dict[str, any]) -> 'MergePartnerWizardModel':
        filtered_item = {}
        schema = MergePartnerWizardModel.model_json_schema()

        for key in item:
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
    def list_from_execute_kw(cls, data:List[dict], fields:List[str] = []) -> List['MergePartnerWizardModel']:
        transformed = []
        schema = MergePartnerWizardModel.model_json_schema()
        
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
