
import json
import xmlrpc.client
from fastapi import APIRouter, Depends, HTTPException, Query
from fastapi.security import APIKeyHeader
from fastapi.responses import JSONResponse
from typing import List, Optional, Dict, Any
from .schemas import ActionWindowViewModel as Model

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

@router.get("/api/ir.actions.act_window.view", response_model=List[Model.ActionWindowViewModel], tags=["ir"])
async def get_actionwindowview(fields:str = '', offset:int = 0, limit:int = 1000, api_key:str = Depends(api_key_header)):
    uid, models = get_connection(api_key)
    field_list = [x.strip() for x in fields.split(',') if x != '']

    if not uid:
        return JSONResponse(content={'status': 'Connection failed'}, status_code=401)
        

    results = models.execute_kw(ODOO_DB, uid, api_key, 'ir.actions.act_window.view', 'search_read', [[]], {'fields': field_list, 'offset': offset, 'limit': limit})
    if results is None:
        return JSONResponse(content=[])
    
    results = Model.ActionWindowViewModel.list_from_execute_kw(results, field_list)
    return JSONResponse(content=results)

    
@router.post("/api/ir.actions.act_window.view", response_model=Model.ActionWindowViewModel, tags=["ir"])
async def post_blog(data:dict, api_key:str = Depends(api_key_header)):
    uid, models = get_connection(api_key)

    if not uid:
        return JSONResponse(content={'status': 'Connection failed'}, status_code=401)

    id = models.execute_kw(ODOO_DB, uid, api_key, 'ir.actions.act_window.view', 'create', [data])
    results = models.execute_kw(ODOO_DB, uid, api_key, 'ir.actions.act_window.view', 'read', [id])
    
    if results is None or len(results) == 0:
        return JSONResponse(content=[])
    
    results = Model.BlogModel.from_execute_kw(results[0])

    return JSONResponse(content={'success': 'Post updated successfully.'})

    
@router.put("/api/ir.actions.act_window.view/{post_id}", response_model=Dict[str, str], tags=["ir"])
async def put_actionwindowview(post_id:int, data:dict, api_key:str = Depends(api_key_header)):
    uid, models = get_connection(api_key)

    print(post_id)
    print(data)

    if not uid:
        return JSONResponse(content={'status': 'Connection failed'}, status_code=401)

    result = models.execute_kw(ODOO_DB, uid, api_key, 'ir.actions.act_window.view', 'write', [[post_id], data])
    print(result)

    return JSONResponse(content={'success': 'Post updated successfully.'})
