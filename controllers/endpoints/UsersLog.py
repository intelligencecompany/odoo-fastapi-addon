
import json
import xmlrpc.client
from fastapi import APIRouter, Depends, HTTPException, Query
from fastapi.security import APIKeyHeader
from typing import List, Optional, Dict, Any
from .schemas import UsersLogModel as Model

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

@router.get("/api/res.users.log", response_model=List[Model.UsersLogModel], tags=["res"])
async def get_userslog(fields:str = '', offset:int = 0, limit:int = 1000, api_key:str = Depends(api_key_header)):
    uid, models = get_connection(api_key)
    field_list = [x.strip() for x in fields.split(',') if x != '']

    if uid:
        results = models.execute_kw(ODOO_DB, uid, api_key, 'res.users.log', 'search_read', [[]], {'fields': field_list, 'offset': offset, 'limit': limit})
        if results is None:
            return json.dumps([])
        
        results = Model.UsersLogModel.from_execute_kw(results, field_list)
        return results
    else:
        return json.dumps({'status': 'Connection failed'})
