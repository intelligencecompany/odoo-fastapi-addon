
import json
import xmlrpc.client
from fastapi import APIRouter, Depends, HTTPException, Query
from fastapi.security import APIKeyHeader
from typing import List, Optional, Dict, Any
from .schemas import WebsiteThemeMenuModel as Model

router = APIRouter()

ODOO_URL = 'http://127.0.0.1:8069'
ODOO_DB = 'azureuser'
ODOO_USERNAME = 'admin'

api_key_header = APIKeyHeader(name='x-key')

def get_connection(api_key: str):
    common = xmlrpc.client.ServerProxy(f'{ODOO_URL}/xmlrpc/2/common')
    uid = common.authenticate(ODOO_DB, ODOO_USERNAME, api_key, {})
    models = xmlrpc.client.ServerProxy(f'{ODOO_URL}/xmlrpc/2/object')
    return uid, models

@router.get("/api/theme.website.menu", response_model=List[Model.WebsiteThemeMenuModel], tags=["theme"])
async def get_websitethememenu(api_key:str = Depends(api_key_header)):
    uid, models = get_connection(api_key)
    if uid:
        results = models.execute_kw(ODOO_DB, uid, api_key, 'theme.website.menu', 'search_read', [[]])
        if results is None:
            return json.dumps([])
        
        return json.dumps(results)
    else:
        return json.dumps({'status': 'Connection failed'})
