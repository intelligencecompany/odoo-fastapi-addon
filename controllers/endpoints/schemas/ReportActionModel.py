
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class ReportActionModel(BaseModel):
    id: Optional[int] = Field(None, title="ID", description="")
    name: str = Field("", title="Action Name", description="")
    type: str = Field("", title="Action Type", description="")
    binding_type: Any = Field(None, title="Binding Type", description="")
    model: str = Field("", title="Model Name", description="")
    report_type: Any = Field(None, title="Report Type", description="The type of the report that will be rendered, each one having its own rendering method. HTML means the report will be opened directly in your browser PDF means the report will be rendered using Wkhtmltopdf and downloaded by the user.")
    report_name: str = Field("", title="Template Name", description="")
    xml_id: Optional[str] = Field(None, title="External ID", description="")
    binding_model_id: Optional[int] = Field(None, title="Binding Model", description="Setting a value makes this action available in the sidebar for the given model.")
    model_id: Optional[int] = Field(None, title="Model", description="")
    groups_id: Optional[List[int]] = Field(None, title="Groups", description="")
    paperformat_id: Optional[int] = Field(None, title="Paper Format", description="")
    help: Optional[Any] = Field(None, title="Action Description", description="Optional help text for the users with a description of the target view, such as its usage and purpose.")
    binding_view_types: Optional[str] = Field(None, title="Binding View Types", description="")
    display_name: Optional[str] = Field(None, title="Display Name", description="")
    create_uid: Optional[int] = Field(None, title="Created by", description="")
    create_date: Optional[str] = Field(None, title="Created on", description="")
    write_uid: Optional[int] = Field(None, title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, title="Last Updated on", description="")
    report_file: Optional[str] = Field(None, title="Report File", description="The path to the main report file (depending on Report Type) or empty if the content is in another field")
    multi: Optional[bool] = Field(None, title="On Multiple Doc.", description="If set to true, the action will not be displayed on the right toolbar of a form view.")
    print_report_name: Optional[str] = Field(None, title="Printed Report Name", description="This is the filename of the report going to download. Keep empty to not change the report filename. You can use a python expression with the 'object' and 'time' variables.")
    attachment_use: Optional[bool] = Field(None, title="Reload from Attachment", description="If enabled, then the second time the user prints with same attachment name, it returns the previous report.")
    attachment: Optional[str] = Field(None, title="Save as Attachment Prefix", description="This is the filename of the attachment used to store the printing result. Keep empty to not save the printed reports. You can use a python expression with the object and time variables.")

