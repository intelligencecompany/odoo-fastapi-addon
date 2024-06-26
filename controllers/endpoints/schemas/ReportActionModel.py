
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class ReportActionModel(BaseModel):
    id: Optional[int] = Field(None, alias="id", title="ID", description="")
    name: str = Field("", alias="name", title="Action Name", description="")
    type: str = Field("", alias="type", title="Action Type", description="")
    binding_type: Any = Field(None, alias="binding_type", title="Binding Type", description="")
    model: str = Field("", alias="model", title="Model Name", description="")
    report_type: Any = Field(None, alias="report_type", title="Report Type", description="The type of the report that will be rendered, each one having its own rendering method. HTML means the report will be opened directly in your browser PDF means the report will be rendered using Wkhtmltopdf and downloaded by the user.")
    report_name: str = Field("", alias="report_name", title="Template Name", description="")
    xml_id: Optional[str] = Field(None, alias="xml_id", title="External ID", description="")
    binding_model_id: Optional[int] = Field(None, alias="binding_model_id", title="Binding Model", description="Setting a value makes this action available in the sidebar for the given model.")
    x_model_id: Optional[int] = Field(None, alias="x_model_id", title="Model", description="")
    groups_id: Optional[List[int]] = Field(None, alias="groups_id", title="Groups", description="")
    paperformat_id: Optional[int] = Field(None, alias="paperformat_id", title="Paper Format", description="")
    help: Optional[Any] = Field(None, alias="help", title="Action Description", description="Optional help text for the users with a description of the target view, such as its usage and purpose.")
    binding_view_types: Optional[str] = Field(None, alias="binding_view_types", title="Binding View Types", description="")
    display_name: Optional[str] = Field(None, alias="display_name", title="Display Name", description="")
    create_uid: Optional[int] = Field(None, alias="create_uid", title="Created by", description="")
    create_date: Optional[str] = Field(None, alias="create_date", title="Created on", description="")
    write_uid: Optional[int] = Field(None, alias="write_uid", title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, alias="write_date", title="Last Updated on", description="")
    report_file: Optional[str] = Field(None, alias="report_file", title="Report File", description="The path to the main report file (depending on Report Type) or empty if the content is in another field")
    multi: Optional[bool] = Field(None, alias="multi", title="On Multiple Doc.", description="If set to true, the action will not be displayed on the right toolbar of a form view.")
    print_report_name: Optional[str] = Field(None, alias="print_report_name", title="Printed Report Name", description="This is the filename of the report going to download. Keep empty to not change the report filename. You can use a python expression with the 'object' and 'time' variables.")
    attachment_use: Optional[bool] = Field(None, alias="attachment_use", title="Reload from Attachment", description="If enabled, then the second time the user prints with same attachment name, it returns the previous report.")
    attachment: Optional[str] = Field(None, alias="attachment", title="Save as Attachment Prefix", description="This is the filename of the attachment used to store the printing result. Keep empty to not save the printed reports. You can use a python expression with the object and time variables.")

    class ConfigDict:
        from_attributes = True

    @classmethod
    def from_execute_kw(cls, item:dict) -> 'ReportActionModel':
        filtered_item = {}
        schema = ReportActionModel.model_json_schema()

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
    def list_from_execute_kw(cls, data:List[dict], fields:List[str] = []) -> List['ReportActionModel']:
        transformed = []
        schema = ReportActionModel.model_json_schema()
        
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
