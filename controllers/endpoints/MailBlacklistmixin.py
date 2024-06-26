
import json
import xmlrpc.client
from fastapi import APIRouter, Depends, HTTPException, Query
from fastapi.security import APIKeyHeader
from fastapi.responses import JSONResponse
from typing import List, Optional, Dict, Any
from .schemas import MailBlacklistmixinModel as Model

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

@router.get("/api/mail.thread.blacklist", response_model=List[Model.MailBlacklistmixinModel], tags=['mail', 'thread', 'blacklist'])
async def get_mailblacklistmixin(fields:str = '', offset:int = 0, limit:int = 10, api_key:str = Depends(api_key_header)):
    uid, models = get_connection(api_key)
    field_list = [x.strip() for x in fields.split(',') if x != '']

    if not uid:
        return JSONResponse(content={'status': 'Connection failed'}, status_code=401)
        
    try:
        results = models.execute_kw(ODOO_DB, uid, api_key, 'mail.thread.blacklist', 'search_read', [[]], {'fields': field_list, 'offset': offset, 'limit': limit})
    except Exception as e:
        return JSONResponse(content={'error': e }, status_code=400)

    if results is None:
        return JSONResponse(content=[])
    
    results = Model.MailBlacklistmixinModel.list_from_execute_kw(results, field_list)
    return JSONResponse(content=results)

    
@router.post("/api/mail.thread.blacklist", response_model=Model.MailBlacklistmixinModel, tags=['mail', 'thread', 'blacklist'])
async def post_blog(data:dict, api_key:str = Depends(api_key_header)):
    uid, models = get_connection(api_key)

    if not uid:
        return JSONResponse(content={'status': 'Connection failed'}, status_code=401)

    id = models.execute_kw(ODOO_DB, uid, api_key, 'mail.thread.blacklist', 'create', [data])
    results = models.execute_kw(ODOO_DB, uid, api_key, 'mail.thread.blacklist', 'read', [id])
    
    if results is None or len(results) == 0:
        return JSONResponse(content=[])
    
    results = Model.BlogModel.from_execute_kw(results[0])

    return JSONResponse(content=results)

    
@router.put("/api/mail.thread.blacklist/{post_id}", response_model=Dict[str, str], tags=['mail', 'thread', 'blacklist'])
async def put_mailblacklistmixin(post_id:int, data:dict, api_key:str = Depends(api_key_header)):
    uid, models = get_connection(api_key)

    print(post_id)
    print(data)

    if not uid:
        return JSONResponse(content={'status': 'Connection failed'}, status_code=401)

    result = models.execute_kw(ODOO_DB, uid, api_key, 'mail.thread.blacklist', 'write', [[post_id], data])
    print(result)

    return JSONResponse(content={'success': 'Post updated successfully.'})
