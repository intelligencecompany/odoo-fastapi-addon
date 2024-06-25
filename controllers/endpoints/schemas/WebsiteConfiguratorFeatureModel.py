
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class WebsiteConfiguratorFeatureModel(BaseModel):
    id: Optional[int] = Field(None, title="ID", description="")
    page_view_id: Optional[int] = Field(None, title="Page View", description="")
    module_id: Optional[int] = Field(None, title="Module", description="")
    sequence: Optional[int] = Field(None, title="Sequence", description="")
    name: Optional[str] = Field(None, title="Name", description="")
    description: Optional[str] = Field(None, title="Description", description="")
    icon: Optional[str] = Field(None, title="Icon", description="")
    iap_page_code: Optional[str] = Field(None, title="Iap Page Code", description="Page code used to tell IAP website_service for which page a snippet list should be generated")
    website_config_preselection: Optional[str] = Field(None, title="Website Config Preselection", description="Comma-separated list of website type/purpose for which this feature should be pre-selected")
    feature_url: Optional[str] = Field(None, title="Feature Url", description="")
    menu_sequence: Optional[int] = Field(None, title="Menu Sequence", description="If set, a website menu will be created for the feature.")
    menu_company: Optional[bool] = Field(None, title="Menu Company", description="If set, add the menu as a second level menu, as a child of \"Company\" menu.")
    display_name: Optional[str] = Field(None, title="Display Name", description="")
    create_uid: Optional[int] = Field(None, title="Created by", description="")
    create_date: Optional[str] = Field(None, title="Created on", description="")
    write_uid: Optional[int] = Field(None, title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, title="Last Updated on", description="")

