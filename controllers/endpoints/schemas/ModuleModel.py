
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class ModuleModel(BaseModel):
    id: Optional[int] = Field(None, alias="id", title="ID", description="")
    name: str = Field("", alias="name", title="Technical Name", description="")
    category_id: Optional[int] = Field(None, alias="category_id", title="Category", description="")
    dependencies_id: Optional[List[int]] = Field(None, alias="dependencies_id", title="Dependencies", description="")
    exclusion_ids: Optional[List[int]] = Field(None, alias="exclusion_ids", title="Exclusions", description="")
    image_ids: Optional[List[int]] = Field(None, alias="image_ids", title="Screenshots", description="")
    shortdesc: Optional[str] = Field(None, alias="shortdesc", title="Module Name", description="")
    summary: Optional[str] = Field(None, alias="summary", title="Summary", description="")
    description: Optional[Any] = Field(None, alias="description", title="Description", description="")
    description_html: Optional[Any] = Field(None, alias="description_html", title="Description HTML", description="")
    author: Optional[str] = Field(None, alias="author", title="Author", description="")
    maintainer: Optional[str] = Field(None, alias="maintainer", title="Maintainer", description="")
    contributors: Optional[Any] = Field(None, alias="contributors", title="Contributors", description="")
    website: Optional[str] = Field(None, alias="website", title="Website", description="")
    installed_version: Optional[str] = Field(None, alias="installed_version", title="Latest Version", description="")
    latest_version: Optional[str] = Field(None, alias="latest_version", title="Installed Version", description="")
    published_version: Optional[str] = Field(None, alias="published_version", title="Published Version", description="")
    url: Optional[str] = Field(None, alias="url", title="URL", description="")
    sequence: Optional[int] = Field(None, alias="sequence", title="Sequence", description="")
    auto_install: Optional[bool] = Field(None, alias="auto_install", title="Automatic Installation", description="An auto-installable module is automatically installed by the system when all its dependencies are satisfied. If the module has no dependency, it is always installed.")
    state: Optional[Any] = Field(None, alias="state", title="Status", description="")
    demo: Optional[bool] = Field(None, alias="demo", title="Demo Data", description="")
    license: Optional[Any] = Field(None, alias="license", title="License", description="")
    menus_by_module: Optional[Any] = Field(None, alias="menus_by_module", title="Menus", description="")
    reports_by_module: Optional[Any] = Field(None, alias="reports_by_module", title="Reports", description="")
    views_by_module: Optional[Any] = Field(None, alias="views_by_module", title="Views", description="")
    application: Optional[bool] = Field(None, alias="application", title="Application", description="")
    icon: Optional[str] = Field(None, alias="icon", title="Icon URL", description="")
    icon_image: Optional[Any] = Field(None, alias="icon_image", title="Icon", description="")
    icon_flag: Optional[str] = Field(None, alias="icon_flag", title="Flag", description="")
    to_buy: Optional[bool] = Field(None, alias="to_buy", title="Odoo Enterprise Module", description="")
    has_iap: Optional[bool] = Field(None, alias="has_iap", title="Has Iap", description="")
    display_name: Optional[str] = Field(None, alias="display_name", title="Display Name", description="")
    create_uid: Optional[int] = Field(None, alias="create_uid", title="Created by", description="")
    create_date: Optional[str] = Field(None, alias="create_date", title="Created on", description="")
    write_uid: Optional[int] = Field(None, alias="write_uid", title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, alias="write_date", title="Last Updated on", description="")
    imported: Optional[bool] = Field(None, alias="imported", title="Imported Module", description="")
    module_type: Optional[Any] = Field(None, alias="module_type", title="Module Type", description="")
    is_installed_on_current_website: Optional[bool] = Field(None, alias="is_installed_on_current_website", title="Is Installed On Current Website", description="")

    class Config:
        from_attributes = True

    @classmethod
    def from_execute_kw(cls, data:List[dict], fields:List[str] = []) -> List['ModuleModel']:
        transformed = []
        schema = ModuleModel.model_json_schema()
        
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
