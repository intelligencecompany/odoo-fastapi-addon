
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class MessagesubtypesModel(BaseModel):
    id: Optional[int] = Field(None, alias="id", title="ID", description="")
    name: str = Field("", alias="name", title="Message Type", description="Message subtype gives a more precise type on the message, especially for system notifications. For example, it can be a notification related to a new record (New), or to a stage change in a process (Stage change). Message subtypes allow to precisely tune the notifications the user want to receive on its wall.")
    parent_id: Optional[int] = Field(None, alias="parent_id", title="Parent", description="Parent subtype, used for automatic subscription. This field is not correctly named. For example on a project, the parent_id of project subtypes refers to task-related subtypes.")
    description: Optional[Any] = Field(None, alias="description", title="Description", description="Description that will be added in the message posted for this subtype. If void, the name will be added instead.")
    internal: Optional[bool] = Field(None, alias="internal", title="Internal Only", description="Messages with internal subtypes will be visible only by employees, aka members of base_user group")
    relation_field: Optional[str] = Field(None, alias="relation_field", title="Relation field", description="Field used to link the related model to the subtype model when using automatic subscription on a related document. The field is used to compute getattr(related_document.relation_field).")
    res_model: Optional[str] = Field(None, alias="res_model", title="Model", description="Model the subtype applies to. If False, this subtype applies to all models.")
    default: Optional[bool] = Field(None, alias="default", title="Default", description="Activated by default when subscribing.")
    sequence: Optional[int] = Field(None, alias="sequence", title="Sequence", description="Used to order subtypes.")
    hidden: Optional[bool] = Field(None, alias="hidden", title="Hidden", description="Hide the subtype in the follower options")
    track_recipients: Optional[bool] = Field(None, alias="track_recipients", title="Track Recipients", description="Whether to display all the recipients or only the important ones.")
    display_name: Optional[str] = Field(None, alias="display_name", title="Display Name", description="")
    create_uid: Optional[int] = Field(None, alias="create_uid", title="Created by", description="")
    create_date: Optional[str] = Field(None, alias="create_date", title="Created on", description="")
    write_uid: Optional[int] = Field(None, alias="write_uid", title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, alias="write_date", title="Last Updated on", description="")

    class ConfigDict:
        from_attributes = True

    @classmethod
    def from_execute_kw(cls, item:dict[str, any]) -> 'MessagesubtypesModel':
        filtered_item = {}
        schema = MessagesubtypesModel.model_json_schema()

        for key, value in item.items():
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
    def list_from_execute_kw(cls, data:List[dict], fields:List[str] = []) -> List['MessagesubtypesModel']:
        transformed = []
        schema = MessagesubtypesModel.model_json_schema()
        
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
