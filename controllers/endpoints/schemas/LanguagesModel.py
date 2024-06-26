
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class LanguagesModel(BaseModel):
    id: Optional[int] = Field(None, alias="id", title="ID", description="")
    name: str = Field("", alias="name", title="Name", description="")
    code: str = Field("", alias="code", title="Locale Code", description="This field is used to set/get locales for user")
    url_code: str = Field("", alias="url_code", title="URL Code", description="The Lang Code displayed in the URL")
    direction: Any = Field(None, alias="direction", title="Direction", description="")
    date_format: str = Field("", alias="date_format", title="Date Format", description="")
    time_format: str = Field("", alias="time_format", title="Time Format", description="")
    week_start: Any = Field(None, alias="week_start", title="First Day of Week", description="")
    grouping: str = Field("", alias="grouping", title="Separator Format", description="The Separator Format should be like [,n] where 0 < n :starting from Unit digit. -1 will end the separation. e.g. [3,2,-1] will represent 106500 to be 1,06,500; [1,2,-1] will represent it to be 106,50,0;[3] will represent it as 106,500. Provided ',' as the thousand separator in each case.")
    decimal_point: str = Field("", alias="decimal_point", title="Decimal Separator", description="")
    iso_code: Optional[str] = Field(None, alias="iso_code", title="ISO code", description="This ISO code is the name of po files to use for translations")
    active: Optional[bool] = Field(None, alias="active", title="Active", description="")
    thousands_sep: Optional[str] = Field(None, alias="thousands_sep", title="Thousands Separator", description="")
    flag_image: Optional[Any] = Field(None, alias="flag_image", title="Image", description="")
    flag_image_url: Optional[str] = Field(None, alias="flag_image_url", title="Flag Image Url", description="")
    display_name: Optional[str] = Field(None, alias="display_name", title="Display Name", description="")
    create_uid: Optional[int] = Field(None, alias="create_uid", title="Created by", description="")
    create_date: Optional[str] = Field(None, alias="create_date", title="Created on", description="")
    write_uid: Optional[int] = Field(None, alias="write_uid", title="Last Updated by", description="")
    write_date: Optional[str] = Field(None, alias="write_date", title="Last Updated on", description="")

    class ConfigDict:
        from_attributes = True

    @classmethod
    def from_execute_kw(cls, item:dict[str, any]) -> 'LanguagesModel':
        filtered_item = {}
        schema = LanguagesModel.model_json_schema()

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
    def list_from_execute_kw(cls, data:List[dict], fields:List[str] = []) -> List['LanguagesModel']:
        transformed = []
        schema = LanguagesModel.model_json_schema()
        
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
