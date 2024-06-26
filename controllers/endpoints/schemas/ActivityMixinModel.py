
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class ActivityMixinModel(BaseModel):

    activity_user_id: Optional[int] = Field(None, alias="activity_user_id", title="Responsible User", description="")
    activity_type_id: Optional[int] = Field(None, alias="activity_type_id", title="Next Activity Type", description="")
    activity_ids: Optional[List[int]] = Field(None, alias="activity_ids", title="Activities", description="")
    activity_state: Optional[Any] = Field(None, alias="activity_state", title="Activity State", description="Status based on activities\nOverdue: Due date is already passed\nToday: Activity date is today\nPlanned: Future activities.")
    activity_type_icon: Optional[str] = Field(None, alias="activity_type_icon", title="Activity Type Icon", description="Font awesome icon e.g. fa-tasks")
    activity_date_deadline: Optional[str] = Field(None, alias="activity_date_deadline", title="Next Activity Deadline", description="")
    my_activity_date_deadline: Optional[str] = Field(None, alias="my_activity_date_deadline", title="My Activity Deadline", description="")
    activity_summary: Optional[str] = Field(None, alias="activity_summary", title="Next Activity Summary", description="")
    activity_exception_decoration: Optional[Any] = Field(None, alias="activity_exception_decoration", title="Activity Exception Decoration", description="Type of the exception activity on record.")
    activity_exception_icon: Optional[str] = Field(None, alias="activity_exception_icon", title="Icon", description="Icon to indicate an exception activity.")

    class ConfigDict:
        from_attributes = True

    @classmethod
    def from_execute_kw(cls, item:dict[str, any]) -> 'ActivityMixinModel':
        filtered_item = {}
        schema = ActivityMixinModel.model_json_schema()

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
    def list_from_execute_kw(cls, data:List[dict], fields:List[str] = []) -> List['ActivityMixinModel']:
        transformed = []
        schema = ActivityMixinModel.model_json_schema()
        
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
