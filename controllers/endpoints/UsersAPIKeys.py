
import json
import re
import xmlrpc.client
from fastapi import APIRouter, Depends, HTTPException, Query
from fastapi.security import APIKeyHeader
from fastapi.responses import JSONResponse
from typing import List, Optional, Dict, Any
from .schemas import UsersAPIKeysModel as Model

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

@router.get("/api/res.users.apikeys", response_model=List[Model.UsersAPIKeysModel], tags=['res', 'users', 'apikeys'])
async def get_usersapikeys(fields:str = '', offset:int = 0, limit:int = 10, api_key:str = Depends(api_key_header)):
    uid, models = get_connection(api_key)
    field_list = [x.strip() for x in fields.split(',') if x != '']

    if not uid:
        return JSONResponse(content={'status': 'Connection failed'}, status_code=401)
        
    try:
        results = models.execute_kw(ODOO_DB, uid, api_key, 'res.users.apikeys', 'search_read', [[]], {'fields': field_list, 'offset': offset, 'limit': limit})

        if results is None:
            return JSONResponse(content=[], status_code=204)
    
        results = Model.UsersAPIKeysModel.list_from_execute_kw(results, field_list)

    except Exception as e:
        match = re.match(r"<Fault (\d+): "(.*)">", str(e), re.DOTALL)
        if match:
            error_code = int(match.group(1))
            error_message = match.group(2)

            error_info = {
                "error_code": error_code,
                "error_message": error_message
            }
            return JSONResponse(content=error_info, status_code=400)
        return JSONResponse(content={ "error": "An unknown error occurred."}, status_code=400)

    return JSONResponse(content=results)

    
@router.post("/api/res.users.apikeys", response_model=Model.UsersAPIKeysModel, tags=['res', 'users', 'apikeys'])
async def post_blog(data:dict, api_key:str = Depends(api_key_header)):
    uid, models = get_connection(api_key)

    if not uid:
        return JSONResponse(content={'status': 'Connection failed'}, status_code=401)

    id = models.execute_kw(ODOO_DB, uid, api_key, 'res.users.apikeys', 'create', [data])
    results = models.execute_kw(ODOO_DB, uid, api_key, 'res.users.apikeys', 'read', [id])
    
    if results is None or len(results) == 0:
        return JSONResponse(content=[])
    
    results = Model.BlogModel.from_execute_kw(results[0])

    return JSONResponse(content=results)

    
@router.put("/api/res.users.apikeys/{post_id}", response_model=Dict[str, str], tags=['res', 'users', 'apikeys'])
async def put_usersapikeys(post_id:int, data:dict, api_key:str = Depends(api_key_header)):
    uid, models = get_connection(api_key)

    print(post_id)
    print(data)

    if not uid:
        return JSONResponse(content={'status': 'Connection failed'}, status_code=401)

    result = models.execute_kw(ODOO_DB, uid, api_key, 'res.users.apikeys', 'write', [[post_id], data])
    print(result)

    return JSONResponse(content={'success': 'Post updated successfully.'})
