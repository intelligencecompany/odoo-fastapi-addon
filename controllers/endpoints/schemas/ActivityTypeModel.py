
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class ActivityTypeModel(BaseModel):
    id: Optional[int] = Field(None, alias="id", title="ID", description="")
    name: str = Field("", alias="name", title="Name", description="")
    delay_unit: Any = Field(None, alias="delay_unit", title="Delay units", description="Unit of delay")
    delay_from: Any = Field(None, alias="delay_from", title="Delay Type", description="Type of delay")
    chaining_type: Any = Field(None, alias="chaining_type", title="Chaining Type", description="")
    triggered_next_type_id: Optional[int] = Field(None, alias="triggered_next_type_id", title="Trigger", description="Automatically schedule this activity once the current one is marked as done.")
    default_user_id: Optional[int] = Field(None, alias="default_user_id", title="Default User", description="")
    suggested_next_type_ids: Optional[List[int]] = Field(None, alias="suggested_next_type_ids", title="Suggest", description="Suggest these activities once the current one is marked as done.")
    previous_type_ids: Optional[List[int]] = Field(None, alias="previous_type_ids", title="Preceding Activities", description="")
    mail_template_ids: Optional[List[int]] = Field(None, alias="mail_template_ids", title="Email templates", description="")
    summary: Optional[str] = Field(None, alias="summary", title="Default Summary", description="")
    sequence: Optional[int] = Field(None, alias="sequence", title="Sequence", description="")
    active: Optional[bool] = Field(None, alias="active", title="Active", description="")
    create_uid: Optional[int] = Field(None, alias="create_uid", title="Create Uid", description="")
    delay_count: Optional[int] = Field(None, alias="delay_count", title="Schedule", description="Number of days/week/month before executing the action. It allows to plan the action deadline.")
    delay_label: Optional[str] = Field(None, alias="delay_label", title="Delay Label", description="")
    icon: Optional[str] = Field(None, alias="icon", title="Icon", description="Font awesome icon e.g. fa-tasks")
    decoration_type: Optional[Any] = Field(None, alias="decoration_type", title="Decoration Type", description="Change the background color of the related activities of this type.")
    res_model: Optional[Any] = Field(None, alias="res_model", title="Model", description="Specify a model if the activity should be specific to a model and not available when managing activities for other models.")
    category: Optional[Any] = Field(None, alias="category", title="Action", description="Actions may trigger specific behavior like opening calendar view or automatically mark as done when a document is uploaded")
    default_note: Optional[Any] = Field(None, alias="default_note", title="Default Note", description="")
    keep_done: Optional[bool] = Field(None, alias="keep_done", title="Keep Done", description="Keep activities marked as done in the activity view")
    initial_res_model: Optional[Any] = Field(None, alias="initial_res_model", title="Initial model", description="Technical field to keep track of the model at the start of editing to support UX related behaviour")
    res_model_change: Optional[bool] = Field(None, alias="res_model_change", title="Model has change", description="")
    display_name: Optional[str] = Field(None, alias="display_name", title="Display Name", description="")
    create_date: Optional[str] = Field(None, alias="create_date", title="Created on", description="")
    write_uid: Optional[int] = Field(None, alias="write_uid", title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, alias="write_date", title="Last Updated on", description="")

    class ConfigDict:
        from_attributes = True

    @classmethod
    def from_execute_kw(cls, item:dict[str, any]) -> 'ActivityTypeModel':
        filtered_item = {}
        schema = ActivityTypeModel.model_json_schema()

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
    def list_from_execute_kw(cls, data:List[dict], fields:List[str] = []) -> List['ActivityTypeModel']:
        transformed = []
        schema = ActivityTypeModel.model_json_schema()
        
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
