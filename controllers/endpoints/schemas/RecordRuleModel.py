
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class RecordRuleModel(BaseModel):
    id: Optional[int] = Field(None, alias="id", title="ID", description="")
    x_model_id: int = Field(0, alias="x_model_id", title="Model", description="")
    name: Optional[str] = Field(None, alias="name", title="Name", description="")
    active: Optional[bool] = Field(None, alias="active", title="Active", description="If you uncheck the active field, it will disable the record rule without deleting it (if you delete a native record rule, it may be re-created when you reload the module).")
    groups: Optional[List[int]] = Field(None, alias="groups", title="Groups", description="")
    domain_force: Optional[Any] = Field(None, alias="domain_force", title="Domain", description="")
    perm_read: Optional[bool] = Field(None, alias="perm_read", title="Read", description="")
    perm_write: Optional[bool] = Field(None, alias="perm_write", title="Write", description="")
    perm_create: Optional[bool] = Field(None, alias="perm_create", title="Create", description="")
    perm_unlink: Optional[bool] = Field(None, alias="perm_unlink", title="Delete", description="")
    display_name: Optional[str] = Field(None, alias="display_name", title="Display Name", description="")
    create_uid: Optional[int] = Field(None, alias="create_uid", title="Created by", description="")
    create_date: Optional[str] = Field(None, alias="create_date", title="Created on", description="")
    write_uid: Optional[int] = Field(None, alias="write_uid", title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, alias="write_date", title="Last Updated on", description="")

    class ConfigDict:
        from_attributes = True

    @classmethod
    def from_execute_kw(cls, data:List[dict], fields:List[str] = []) -> List['RecordRuleModel']:
        transformed = []
        schema = RecordRuleModel.model_json_schema()
        
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
