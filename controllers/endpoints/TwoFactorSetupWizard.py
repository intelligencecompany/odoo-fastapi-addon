
import json
import xmlrpc.client
from fastapi import APIRouter, Depends, HTTPException, Query
from fastapi.security import APIKeyHeader
from fastapi.responses import JSONResponse
from typing import List, Optional, Dict, Any
from .schemas import TwoFactorSetupWizardModel as Model

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

@router.get("/api/auth_totp.wizard", response_model=List[Model.TwoFactorSetupWizardModel], tags=['auth_totp', 'wizard'])
async def get_twofactorsetupwizard(fields:str = '', offset:int = 0, limit:int = 10, api_key:str = Depends(api_key_header)):
    uid, models = get_connection(api_key)
    field_list = [x.strip() for x in fields.split(',') if x != '']

    if not uid:
        return JSONResponse(content={'status': 'Connection failed'}, status_code=401)
        
    try:
        results = models.execute_kw(ODOO_DB, uid, api_key, 'auth_totp.wizard', 'search_read', [[]], {'fields': field_list, 'offset': offset, 'limit': limit})
    except Exception as e:
        return JSONResponse(content={'error': e }, status_code=400)

    if results is None:
        return JSONResponse(content=[])
    
    results = Model.TwoFactorSetupWizardModel.list_from_execute_kw(results, field_list)
    return JSONResponse(content=results)

    
@router.post("/api/auth_totp.wizard", response_model=Model.TwoFactorSetupWizardModel, tags=['auth_totp', 'wizard'])
async def post_blog(data:dict, api_key:str = Depends(api_key_header)):
    uid, models = get_connection(api_key)

    if not uid:
        return JSONResponse(content={'status': 'Connection failed'}, status_code=401)

    id = models.execute_kw(ODOO_DB, uid, api_key, 'auth_totp.wizard', 'create', [data])
    results = models.execute_kw(ODOO_DB, uid, api_key, 'auth_totp.wizard', 'read', [id])
    
    if results is None or len(results) == 0:
        return JSONResponse(content=[])
    
    results = Model.BlogModel.from_execute_kw(results[0])

    return JSONResponse(content=results)

    
@router.put("/api/auth_totp.wizard/{post_id}", response_model=Dict[str, str], tags=['auth_totp', 'wizard'])
async def put_twofactorsetupwizard(post_id:int, data:dict, api_key:str = Depends(api_key_header)):
    uid, models = get_connection(api_key)

    print(post_id)
    print(data)

    if not uid:
        return JSONResponse(content={'status': 'Connection failed'}, status_code=401)

    result = models.execute_kw(ODOO_DB, uid, api_key, 'auth_totp.wizard', 'write', [[post_id], data])
    print(result)

    return JSONResponse(content={'success': 'Post updated successfully.'})
