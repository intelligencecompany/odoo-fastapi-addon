
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class DocumentFollowersModel(BaseModel):
    id: Optional[int] = Field(None, alias="id", title="ID", description="")
    res_model: str = Field("", alias="res_model", title="Related Document Model Name", description="")
    res_id: Optional[Any] = Field(None, alias="res_id", title="Related Document ID", description="Id of the followed resource")
    partner_id: int = Field(0, alias="partner_id", title="Related Partner", description="")
    subtype_ids: Optional[List[int]] = Field(None, alias="subtype_ids", title="Subtype", description="Message subtypes followed, meaning subtypes that will be pushed onto the user's Wall.")
    name: Optional[str] = Field(None, alias="name", title="Name", description="")
    email: Optional[str] = Field(None, alias="email", title="Email", description="")
    is_active: Optional[bool] = Field(None, alias="is_active", title="Is Active", description="")
    display_name: Optional[str] = Field(None, alias="display_name", title="Display Name", description="")

    class ConfigDict:
        from_attributes = True

    @classmethod
    def from_execute_kw(cls, item:dict[str, any]) -> 'DocumentFollowersModel':
        filtered_item = {}
        schema = DocumentFollowersModel.model_json_schema()

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
    def list_from_execute_kw(cls, data:List[dict], fields:List[str] = []) -> List['DocumentFollowersModel']:
        transformed = []
        schema = DocumentFollowersModel.model_json_schema()
        
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
