
import json
import logging
import xmlrpc.client
from fastapi import APIRouter, Depends, HTTPException, Query
from fastapi.security import APIKeyHeader
from fastapi.responses import JSONResponse
from typing import List, Optional, Dict, Any
from .schemas import UpdateModuleModel as Model
from odoo import http
from odoo.http import request

router = APIRouter()

ODOO_URL = 'http://127.0.0.1:8069'
ODOO_DB = 'azureuser'
ODOO_USERNAME = 'admin'

api_key_header = APIKeyHeader(name='x-key')

def get_connection(api_key: str):
    common = xmlrpc.client.ServerProxy(f'{ODOO_URL}/xmlrpc/2/common')

    if not api_key:
        return request.make_response("API key missing", status=400)

    user_id = request.env["res.users.apikeys"]._check_credentials(
        scope="rpc", key=api_key
    )

    if not user_id:
        return request.make_response("API key invalid", status=400)
    
    print(user_id)

    uid = common.authenticate(ODOO_DB, user_id, api_key, {})
    models = xmlrpc.client.ServerProxy(f'{ODOO_URL}/xmlrpc/2/object')
    return uid, models

@router.get("/api/base.module.update", response_model=List[Model.UpdateModuleModel], tags=['base', 'module', 'update'])
async def get_updatemodule(fields:str = '', offset:int = 0, limit:int = 10, api_key:str = Depends(api_key_header)):
    uid, models = get_connection(api_key)
    field_list = [x.strip() for x in fields.split(',') if x != '']

    if not uid:
        return JSONResponse(content={'status': 'Connection failed'}, status_code=401)
        
    try:
        results = models.execute_kw(ODOO_DB, uid, api_key, 'base.module.update', 'search_read', [[]], {'fields': field_list, 'offset': offset, 'limit': limit})

        if results is None:
            return JSONResponse(content=[], status_code=204)
    
        results = Model.UpdateModuleModel.list_from_execute_kw(results, field_list)

    except Exception as e:
        logging.error(str(e))
        return JSONResponse(content={ "error": str(e)}, status_code=500)

    return JSONResponse(content=results)

    
@router.post("/api/base.module.update", response_model=Model.UpdateModuleModel, tags=['base', 'module', 'update'])
async def post_blog(data:dict, api_key:str = Depends(api_key_header)):
    uid, models = get_connection(api_key)

    if not uid:
        return JSONResponse(content={'status': 'Connection failed'}, status_code=401)

    try:
        id = models.execute_kw(ODOO_DB, uid, api_key, 'base.module.update', 'create', [data])
        results = models.execute_kw(ODOO_DB, uid, api_key, 'base.module.update', 'read', [id])
        
        if results is None or len(results) == 0:
            return JSONResponse(content=[])
        
        results = Model.BlogModel.from_execute_kw(results[0])
    except Exception as e:
        logging.error(str(e))
        return JSONResponse(content={ "error": str(e)}, status_code=500)

    return JSONResponse(content=results)

    
@router.put("/api/base.module.update/{post_id}", response_model=Dict[str, str], tags=['base', 'module', 'update'])
async def put_updatemodule(post_id:int, data:dict, api_key:str = Depends(api_key_header)):
    uid, models = get_connection(api_key)

    print(post_id)
    print(data)

    if not uid:
        return JSONResponse(content={'status': 'Connection failed'}, status_code=401)

    try:
        result = models.execute_kw(ODOO_DB, uid, api_key, 'base.module.update', 'write', [[post_id], data])
    except Exception as e:
        logging.error(str(e))
        return JSONResponse(content={ "error": str(e)}, status_code=500)

    return JSONResponse(content={'success': 'Post updated successfully.'})
