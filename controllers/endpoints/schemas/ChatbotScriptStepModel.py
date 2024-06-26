
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class ChatbotScriptStepModel(BaseModel):
    id: Optional[int] = Field(None, alias="id", title="ID", description="")
    step_type: Any = Field(None, alias="step_type", title="Step Type", description="")
    chatbot_script_id: int = Field(0, alias="chatbot_script_id", title="Chatbot", description="")
    answer_ids: Optional[List[int]] = Field(None, alias="answer_ids", title="Answers", description="")
    triggering_answer_ids: Optional[List[int]] = Field(None, alias="triggering_answer_ids", title="Only If", description="Show this step only if all of these answers have been selected.")
    message: Optional[Any] = Field(None, alias="message", title="Message", description="")
    sequence: Optional[int] = Field(None, alias="sequence", title="Sequence", description="")
    is_forward_operator_child: Optional[bool] = Field(None, alias="is_forward_operator_child", title="Is Forward Operator Child", description="")
    display_name: Optional[str] = Field(None, alias="display_name", title="Display Name", description="")
    create_uid: Optional[int] = Field(None, alias="create_uid", title="Created by", description="")
    create_date: Optional[str] = Field(None, alias="create_date", title="Created on", description="")
    write_uid: Optional[int] = Field(None, alias="write_uid", title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, alias="write_date", title="Last Updated on", description="")

    class Config:
        from_attributes = True

    @classmethod
    def from_execute_kw(cls, data:List[dict], fields:List[str] = []) -> List['ChatbotScriptStepModel']:
        transformed = []
        schema = ChatbotScriptStepModel.model_json_schema()
        
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