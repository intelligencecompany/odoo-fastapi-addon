
import json
import xmlrpc.client
from fastapi import APIRouter, Depends, HTTPException, Query
from fastapi.security import APIKeyHeader
from typing import List, Optional, Dict, Any
from .schemas import WebsiteSnippetFilterModel as Model

router = APIRouter()

ODOO_URL = 'https://dataruba.com'
ODOO_DB = 'azureuser'
ODOO_USERNAME = 'admin'

api_key_header = APIKeyHeader(name='x-key')

def get_connection(api_key: str):
    common = xmlrpc.client.ServerProxy(f'{ODOO_URL}/xmlrpc/2/common')
    uid = common.authenticate(ODOO_DB, ODOO_USERNAME, api_key, {})
    models = xmlrpc.client.ServerProxy(f'{ODOO_URL}/xmlrpc/2/object')
    return uid, models

@router.get("/api/website.snippet.filter", response_model=List[Model.WebsiteSnippetFilterModel], tags=["website"])
async def get_websitesnippetfilter(fields:str = '', offset:int = 0, limit:int = 1000, api_key:str = Depends(api_key_header)):
    uid, models = get_connection(api_key)
    field_list = [x.strip() for x in fields.split(',') if x != '']

    if uid:
        results = models.execute_kw(ODOO_DB, uid, api_key, 'website.snippet.filter', 'search_read', [[]], {'fields': field_list, 'offset': offset, 'limit': limit})
        if results is None:
            return json.dumps([])
        
        results = Model.WebsiteSnippetFilterModel.from_execute_kw(results, field_list)
        return results
    else:
        return json.dumps({'status': 'Connection failed'})

@router.put("/api/website.snippet.filter/{post_id}", response_model=Dict[str, str], tags=["website"])
async def put_websitesnippetfilter(post_id:int, fields:Dict[str, Any], api_key:str = Depends(api_key_header)):
    uid, models = get_connection(api_key)

    print(post_id)
    print(fields)

    if uid:
        result = models.execute_kw(ODOO_DB, uid, api_key, 'website.snippet.filter', 'write', [[post_id], fields])
        print(result)

        return json.dumps({'success': 'Post updated successfully.'})
    else:
        return json.dumps({'status': 'Connection failed'})
