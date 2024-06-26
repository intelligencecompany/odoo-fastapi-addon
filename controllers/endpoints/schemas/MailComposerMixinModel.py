
from pydantic import BaseModel, Field
from typing import Optional, List, Any, Dict

class MailComposerMixinModel(BaseModel):

    template_id: Optional[int] = Field(None, alias="template_id", title="Mail Template", description="")
    lang: Optional[str] = Field(None, alias="lang", title="Language", description="Optional translation language (ISO code) to select when sending out an email. If not set, the english version will be used. This should usually be a placeholder expression that provides the appropriate language, e.g. {{ object.partner_id.lang }}.")
    render_model: Optional[str] = Field(None, alias="render_model", title="Rendering Model", description="")
    subject: Optional[str] = Field(None, alias="subject", title="Subject", description="")
    body: Optional[Any] = Field(None, alias="body", title="Contents", description="")
    body_has_template_value: Optional[bool] = Field(None, alias="body_has_template_value", title="Body content is the same as the template", description="")
    is_mail_template_editor: Optional[bool] = Field(None, alias="is_mail_template_editor", title="Is Editor", description="")
    can_edit_body: Optional[bool] = Field(None, alias="can_edit_body", title="Can Edit Body", description="")

    class ConfigDict:
        from_attributes = True

    @classmethod
    def from_execute_kw(cls, item:Dict[str, Any]) -> 'MailComposerMixinModel':
        filtered_item = {}
        schema = MailComposerMixinModel.model_json_schema()

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
    def list_from_execute_kw(cls, data:List[dict], fields:List[str] = []) -> List['MailComposerMixinModel']:
        transformed = []
        schema = MailComposerMixinModel.model_json_schema()
        
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
