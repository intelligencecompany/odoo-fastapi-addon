
import json
import logging
import xmlrpc.client
from typing import Annotated, Union
from fastapi import APIRouter, Depends, HTTPException, Query, Header
from typing import Annotated, Union
from fastapi.security import APIKeyHeader
from fastapi.responses import JSONResponse
from typing import List, Optional, Dict, Any
from .schemas import ThemeAttachmentsModel as Model

router = APIRouter()

ODOO_URL = 'http://127.0.0.1:8069'
ODOO_DB = 'azureuser'
ODOO_USERNAME = 'admin'

api_key_header = APIKeyHeader(name='x-key')

def get_connection(uid: int, api_key: str):
    common = xmlrpc.client.ServerProxy(f'{ODOO_URL}/xmlrpc/2/common')
    uid = common.authenticate(ODOO_DB, uid, api_key, {})
    models = xmlrpc.client.ServerProxy(f'{ODOO_URL}/xmlrpc/2/object')
    return uid, models

@router.get("/api/theme.ir.attachment", response_model=List[Model.ThemeAttachmentsModel], tags=["theme"])
async def get_themeattachments(
        fields:str = '', 
        offset:int = 0, 
        limit:int = 10, 
        api_key:str = Depends(api_key_header),
        uid:str | None = Header(default=None)
    ):
    uid, models = get_connection(uid, api_key)
    field_list = [x.strip() for x in fields.split(',') if x != '']

    if not uid:
        return JSONResponse(content={'status': 'Connection failed'}, status_code=401)
        
    try:
        results = models.execute_kw(ODOO_DB, uid, api_key, 'theme.ir.attachment', 'search_read', [[]], {'fields': field_list, 'offset': offset, 'limit': limit})

        if results is None:
            return JSONResponse(content=[], status_code=204)
    
        results = Model.ThemeAttachmentsModel.list_from_execute_kw(results, field_list)

    except Exception as e:
        logging.error(str(e))
        return JSONResponse(content={ "error": str(e)}, status_code=500)

    return JSONResponse(content=results)

    
@router.post("/api/theme.ir.attachment", response_model=Model.ThemeAttachmentsModel, tags=["theme"])
async def post_blog(data:dict, api_key:str = Depends(api_key_header)):
    uid, models = get_connection(api_key)

    if not uid:
        return JSONResponse(content={'status': 'Connection failed'}, status_code=401)

    try:
        id = models.execute_kw(ODOO_DB, uid, api_key, 'theme.ir.attachment', 'create', [data])
        results = models.execute_kw(ODOO_DB, uid, api_key, 'theme.ir.attachment', 'read', [id])
        
        if results is None or len(results) == 0:
            return JSONResponse(content=[])
        
        results = Model.BlogModel.from_execute_kw(results[0])
    except Exception as e:
        logging.error(str(e))
        return JSONResponse(content={ "error": str(e)}, status_code=500)

    return JSONResponse(content=results)

    
@router.put("/api/theme.ir.attachment/{post_id}", response_model=Dict[str, str], tags=["theme"])
async def put_themeattachments(post_id:int, data:dict, api_key:str = Depends(api_key_header)):
    uid, models = get_connection(api_key)

    print(post_id)
    print(data)

    if not uid:
        return JSONResponse(content={'status': 'Connection failed'}, status_code=401)

    try:
        result = models.execute_kw(ODOO_DB, uid, api_key, 'theme.ir.attachment', 'write', [[post_id], data])
    except Exception as e:
        logging.error(str(e))
        return JSONResponse(content={ "error": str(e)}, status_code=500)

    return JSONResponse(content={'success': 'Post updated successfully.'})
