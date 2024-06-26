
from pydantic import BaseModel, Field
from typing import Optional, List, Any, Dict

class WebsiteConfiguratorFeatureModel(BaseModel):
    id: Optional[int] = Field(None, alias="id", title="ID", description="")
    page_view_id: Optional[int] = Field(None, alias="page_view_id", title="Page View", description="")
    module_id: Optional[int] = Field(None, alias="module_id", title="Module", description="")
    sequence: Optional[int] = Field(None, alias="sequence", title="Sequence", description="")
    name: Optional[str] = Field(None, alias="name", title="Name", description="")
    description: Optional[str] = Field(None, alias="description", title="Description", description="")
    icon: Optional[str] = Field(None, alias="icon", title="Icon", description="")
    iap_page_code: Optional[str] = Field(None, alias="iap_page_code", title="Iap Page Code", description="Page code used to tell IAP website_service for which page a snippet list should be generated")
    website_config_preselection: Optional[str] = Field(None, alias="website_config_preselection", title="Website Config Preselection", description="Comma-separated list of website type/purpose for which this feature should be pre-selected")
    feature_url: Optional[str] = Field(None, alias="feature_url", title="Feature Url", description="")
    menu_sequence: Optional[int] = Field(None, alias="menu_sequence", title="Menu Sequence", description="If set, a website menu will be created for the feature.")
    menu_company: Optional[bool] = Field(None, alias="menu_company", title="Menu Company", description="If set, add the menu as a second level menu, as a child of \"Company\" menu.")
    display_name: Optional[str] = Field(None, alias="display_name", title="Display Name", description="")
    create_uid: Optional[int] = Field(None, alias="create_uid", title="Created by", description="")
    create_date: Optional[str] = Field(None, alias="create_date", title="Created on", description="")
    write_uid: Optional[int] = Field(None, alias="write_uid", title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, alias="write_date", title="Last Updated on", description="")

    class ConfigDict:
        from_attributes = True

    @classmethod
    def from_execute_kw(cls, item:dict) -> 'WebsiteConfiguratorFeatureModel':
        filtered_item = {}
        schema = WebsiteConfiguratorFeatureModel.model_json_schema()

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
    def list_from_execute_kw(cls, data:List[dict], fields:List[str] = []) -> List['WebsiteConfiguratorFeatureModel']:
        transformed = []
        schema = WebsiteConfiguratorFeatureModel.model_json_schema()
        
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
