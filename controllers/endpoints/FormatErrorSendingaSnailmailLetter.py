
import json
import xmlrpc.client
from fastapi import APIRouter, Depends, HTTPException, Query
from fastapi.security import APIKeyHeader
from typing import List, Optional, Dict, Any
from .schemas import FormatErrorSendingaSnailmailLetterModel as Model

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

@router.get("/api/snailmail.letter.format.error", response_model=List[Model.FormatErrorSendingaSnailmailLetterModel], tags=["snailmail"])
async def get_formaterrorsendingasnailmailletter(api_key:str = Depends(api_key_header)):
    uid, models = get_connection(api_key)
    if uid:
        results = models.execute_kw(ODOO_DB, uid, api_key, 'snailmail.letter.format.error', 'search_read', [[]])
        if results is None:
            return json.dumps([])
        
        return json.dumps(results)
    else:
        return json.dumps({'status': 'Connection failed'})
