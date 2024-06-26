
import json
import xmlrpc.client
from fastapi import APIRouter, Depends, HTTPException, Query
from fastapi.security import APIKeyHeader
from fastapi.responses import JSONResponse
from typing import List, Optional, Dict, Any
from .schemas import ConfigSettingsModel as Model

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

@router.get("/api/res.config.settings", response_model=List[Model.ConfigSettingsModel], tags=["res"])
async def get_configsettings(fields:str = '', offset:int = 0, limit:int = 1000, api_key:str = Depends(api_key_header)):
    uid, models = get_connection(api_key)
    field_list = [x.strip() for x in fields.split(',') if x != '']

    if not uid:
        return JSONResponse(content={'status': 'Connection failed'}, status_code=401)
        

    results = models.execute_kw(ODOO_DB, uid, api_key, 'res.config.settings', 'search_read', [[]], {'fields': field_list, 'offset': offset, 'limit': limit})
    if results is None:
        return JSONResponse(content=[])
    
    results = Model.ConfigSettingsModel.list_from_execute_kw(results, field_list)
    return JSONResponse(content=results)

    
@router.post("/api/res.config.settings", response_model=Model.ConfigSettingsModel, tags=["res"])
async def post_blog(data:dict, api_key:str = Depends(api_key_header)):
    uid, models = get_connection(api_key)

    if not uid:
        return JSONResponse(content={'status': 'Connection failed'}, status_code=401)

    id = models.execute_kw(ODOO_DB, uid, api_key, 'res.config.settings', 'create', [data])
    results = models.execute_kw(ODOO_DB, uid, api_key, 'res.config.settings', 'read', [id])
    results = Model.ConfigSettingsModel.from_execute_kw(results)

    return JSONResponse(content={'success': 'Post updated successfully.'})

    
@router.put("/api/res.config.settings/{post_id}", response_model=Dict[str, str], tags=["res"])
async def put_configsettings(post_id:int, data:dict, api_key:str = Depends(api_key_header)):
    uid, models = get_connection(api_key)

    print(post_id)
    print(data)

    if not uid:
        return JSONResponse(content={'status': 'Connection failed'}, status_code=401)

    result = models.execute_kw(ODOO_DB, uid, api_key, 'res.config.settings', 'write', [[post_id], data])
    print(result)

    return JSONResponse(content={'success': 'Post updated successfully.'})
