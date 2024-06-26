
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class GoogleGmailMixinModel(BaseModel):

    google_gmail_authorization_code: Optional[str] = Field(None, alias="google_gmail_authorization_code", title="Authorization Code", description="")
    google_gmail_refresh_token: Optional[str] = Field(None, alias="google_gmail_refresh_token", title="Refresh Token", description="")
    google_gmail_access_token: Optional[str] = Field(None, alias="google_gmail_access_token", title="Access Token", description="")
    google_gmail_access_token_expiration: Optional[int] = Field(None, alias="google_gmail_access_token_expiration", title="Access Token Expiration Timestamp", description="")
    google_gmail_uri: Optional[str] = Field(None, alias="google_gmail_uri", title="URI", description="The URL to generate the authorization code from Google")

    class Config:
        from_attributes = True

    @classmethod
    def from_execute_kw(cls, data:List[dict], fields:List[str] = []) -> List['GoogleGmailMixinModel']:
        transformed = []
        schema = GoogleGmailMixinModel.model_json_schema()
        
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
