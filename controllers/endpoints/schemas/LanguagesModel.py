
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class LanguagesModel(BaseModel):
    id: Optional[int] = Field(None, title="ID", description="")
    name: str = Field("", title="Name", description="")
    code: str = Field("", title="Locale Code", description="This field is used to set/get locales for user")
    url_code: str = Field("", title="URL Code", description="The Lang Code displayed in the URL")
    direction: Any = Field(None, title="Direction", description="")
    date_format: str = Field("", title="Date Format", description="")
    time_format: str = Field("", title="Time Format", description="")
    week_start: Any = Field(None, title="First Day of Week", description="")
    grouping: str = Field("", title="Separator Format", description="The Separator Format should be like [,n] where 0 < n :starting from Unit digit. -1 will end the separation. e.g. [3,2,-1] will represent 106500 to be 1,06,500; [1,2,-1] will represent it to be 106,50,0;[3] will represent it as 106,500. Provided ',' as the thousand separator in each case.")
    decimal_point: str = Field("", title="Decimal Separator", description="")
    iso_code: Optional[str] = Field(None, title="ISO code", description="This ISO code is the name of po files to use for translations")
    active: Optional[bool] = Field(None, title="Active", description="")
    thousands_sep: Optional[str] = Field(None, title="Thousands Separator", description="")
    flag_image: Optional[Any] = Field(None, title="Image", description="")
    flag_image_url: Optional[str] = Field(None, title="Flag Image Url", description="")
    display_name: Optional[str] = Field(None, title="Display Name", description="")
    create_uid: Optional[int] = Field(None, title="Created by", description="")
    create_date: Optional[str] = Field(None, title="Created on", description="")
    write_uid: Optional[int] = Field(None, title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, title="Last Updated on", description="")

