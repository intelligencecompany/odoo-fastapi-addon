
import json
import logging
import xmlrpc.client
from fastapi import APIRouter, Depends, HTTPException, Query
from fastapi.security import APIKeyHeader
from fastapi.responses import JSONResponse
from typing import List, Optional, Dict, Any
from .schemas import PrivacyLookupWizardLineModel as Model

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

@router.get("/api/privacy.lookup.wizard.line", response_model=List[Model.PrivacyLookupWizardLineModel], tags=['privacy', 'lookup', 'wizard', 'line'])
async def get_privacylookupwizardline(fields:str = '', offset:int = 0, limit:int = 10, api_key:str = Depends(api_key_header)):
    uid, models = get_connection(api_key)
    field_list = [x.strip() for x in fields.split(',') if x != '']

    if not uid:
        return JSONResponse(content={'status': 'Connection failed'}, status_code=401)
        
    try:
        results = models.execute_kw(ODOO_DB, uid, api_key, 'privacy.lookup.wizard.line', 'search_read', [[]], {'fields': field_list, 'offset': offset, 'limit': limit})

        if results is None:
            return JSONResponse(content=[], status_code=204)
    
        results = Model.PrivacyLookupWizardLineModel.list_from_execute_kw(results, field_list)

    except Exception as e:
        logging.error(str(e))
        # match = re.match(r'<Fault (\d+): '(.*)'>', str(e), re.DOTALL)
        # if match:
        #     error_code = int(match.group(1))
        #     error_message = match.group(2)

        #     error_info = {
        #         "error_code": error_code,
        #         "error_message": error_message
        #     }
        #     return JSONResponse(content=str(e), status_code=400)
        return JSONResponse(content={ "error": str(e)}, status_code=400)

    return JSONResponse(content=results)

    
@router.post("/api/privacy.lookup.wizard.line", response_model=Model.PrivacyLookupWizardLineModel, tags=['privacy', 'lookup', 'wizard', 'line'])
async def post_blog(data:dict, api_key:str = Depends(api_key_header)):
    uid, models = get_connection(api_key)

    if not uid:
        return JSONResponse(content={'status': 'Connection failed'}, status_code=401)

    id = models.execute_kw(ODOO_DB, uid, api_key, 'privacy.lookup.wizard.line', 'create', [data])
    results = models.execute_kw(ODOO_DB, uid, api_key, 'privacy.lookup.wizard.line', 'read', [id])
    
    if results is None or len(results) == 0:
        return JSONResponse(content=[])
    
    results = Model.BlogModel.from_execute_kw(results[0])

    return JSONResponse(content=results)

    
@router.put("/api/privacy.lookup.wizard.line/{post_id}", response_model=Dict[str, str], tags=['privacy', 'lookup', 'wizard', 'line'])
async def put_privacylookupwizardline(post_id:int, data:dict, api_key:str = Depends(api_key_header)):
    uid, models = get_connection(api_key)

    print(post_id)
    print(data)

    if not uid:
        return JSONResponse(content={'status': 'Connection failed'}, status_code=401)

    result = models.execute_kw(ODOO_DB, uid, api_key, 'privacy.lookup.wizard.line', 'write', [[post_id], data])
    print(result)

    return JSONResponse(content={'success': 'Post updated successfully.'})
