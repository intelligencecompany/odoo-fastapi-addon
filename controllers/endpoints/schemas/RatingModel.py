
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class RatingModel(BaseModel):
    id: Optional[int] = Field(None, alias="id", title="ID", description="")
    res_model_id: Optional[int] = Field(None, alias="res_model_id", title="Related Document Model", description="")
    res_id: Any = Field(None, alias="res_id", title="Document", description="")
    parent_res_model_id: Optional[int] = Field(None, alias="parent_res_model_id", title="Parent Related Document Model", description="")
    parent_res_id: Optional[int] = Field(None, alias="parent_res_id", title="Parent Document", description="")
    rated_partner_id: Optional[int] = Field(None, alias="rated_partner_id", title="Rated Operator", description="")
    partner_id: Optional[int] = Field(None, alias="partner_id", title="Customer", description="")
    message_id: Optional[int] = Field(None, alias="message_id", title="Message", description="")
    publisher_id: Optional[int] = Field(None, alias="publisher_id", title="Commented by", description="")
    create_date: Optional[str] = Field(None, alias="create_date", title="Submitted on", description="")
    res_name: Optional[str] = Field(None, alias="res_name", title="Resource name", description="")
    res_model: Optional[str] = Field(None, alias="res_model", title="Document Model", description="")
    resource_ref: Optional[Any] = Field(None, alias="resource_ref", title="Resource Ref", description="")
    parent_res_name: Optional[str] = Field(None, alias="parent_res_name", title="Parent Document Name", description="")
    parent_res_model: Optional[str] = Field(None, alias="parent_res_model", title="Parent Document Model", description="")
    parent_ref: Optional[Any] = Field(None, alias="parent_ref", title="Parent Ref", description="")
    rated_partner_name: Optional[str] = Field(None, alias="rated_partner_name", title="Name", description="")
    rating: Optional[Any] = Field(None, alias="rating", title="Rating Value", description="")
    rating_image: Optional[Any] = Field(None, alias="rating_image", title="Image", description="")
    rating_image_url: Optional[str] = Field(None, alias="rating_image_url", title="Image URL", description="")
    rating_text: Optional[Any] = Field(None, alias="rating_text", title="Rating", description="")
    feedback: Optional[Any] = Field(None, alias="feedback", title="Comment", description="")
    is_internal: Optional[bool] = Field(None, alias="is_internal", title="Visible Internally Only", description="Hide to public / portal users, independently from subtype configuration.")
    access_token: Optional[str] = Field(None, alias="access_token", title="Security Token", description="")
    consumed: Optional[bool] = Field(None, alias="consumed", title="Filled Rating", description="")
    display_name: Optional[str] = Field(None, alias="display_name", title="Display Name", description="")
    create_uid: Optional[int] = Field(None, alias="create_uid", title="Created by", description="")
    write_uid: Optional[int] = Field(None, alias="write_uid", title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, alias="write_date", title="Last Updated on", description="")
    publisher_comment: Optional[Any] = Field(None, alias="publisher_comment", title="Publisher comment", description="")
    publisher_datetime: Optional[str] = Field(None, alias="publisher_datetime", title="Commented on", description="")

    class ConfigDict:
        from_attributes = True

    @classmethod
    def from_execute_kw(cls, item:dict) -> 'RatingModel':
        filtered_item = {}
        schema = RatingModel.model_json_schema()

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
    def list_from_execute_kw(cls, data:List[dict], fields:List[str] = []) -> List['RatingModel']:
        transformed = []
        schema = RatingModel.model_json_schema()
        
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
