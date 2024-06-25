
from pydantic import BaseModel, Field
from typing import Optional, List, Any

class GoogleGmailMixinModel(BaseModel):

    google_gmail_authorization_code: Optional[str] = Field(None, title="Authorization Code", description="")
    google_gmail_refresh_token: Optional[str] = Field(None, title="Refresh Token", description="")
    google_gmail_access_token: Optional[str] = Field(None, title="Access Token", description="")
    google_gmail_access_token_expiration: Optional[int] = Field(None, title="Access Token Expiration Timestamp", description="")
    google_gmail_uri: Optional[str] = Field(None, title="URI", description="The URL to generate the authorization code from Google")

