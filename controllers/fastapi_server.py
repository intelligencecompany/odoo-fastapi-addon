from fastapi import FastAPI, Depends, HTTPException, Query
from typing import List, Optional, Dict, Any
from fastapi.security import APIKeyHeader
from fastapi.responses import RedirectResponse
import uvicorn
import xmlrpc.client
import logging
import json 
from odoo import http
from .endpoints import *

ODOO_URL = 'http://127.0.0.1:8069'
ODOO_DB = 'azureuser'
ODOO_USERNAME = 'admin'

# app = FastAPI()

api_key_header = APIKeyHeader(name='x-key')

# XML-RPC connection
def get_connection(api_key: str):
    common = xmlrpc.client.ServerProxy(f'{ODOO_URL}/xmlrpc/2/common')

    user_id = http.request.env["res.users.apikeys"]._check_credentials(
        scope="rpc", key=api_key
    )

    if not user_id:
            raise http.BadRequest("API key invalid")
    
    print(user_id)
    
    uid = common.authenticate(ODOO_DB, user_id, api_key, {})
    models = xmlrpc.client.ServerProxy(f'{ODOO_URL}/xmlrpc/2/object')
    return uid, models

@app.get("/api/test")
async def test_connection(api_key:str = Depends(api_key_header)):
    # api_key = 'admin'
    uid, models = get_connection(api_key)
    if uid:
        return json.dumps({'status': 'Connection successful', 'uid': uid })
    else:
        return json.dumps({'status': 'Connection failed' })

@app.get("/api/models", response_model=List[Dict[str, Any]])
async def get_models(api_key:str = Depends(api_key_header)):
    uid, models = get_connection(api_key)
    if uid:
        model_ids = models.execute_kw(ODOO_DB, uid, api_key, 'ir.model', 'search', [[]])
        model_names = models.execute_kw(ODOO_DB, uid, api_key, 'ir.model', 'read', [model_ids, ['model', 'name']])

        return json.dumps(model_names)
    else:
        return json.dumps({'status': 'Connection failed'})

# @app.get("/api/{model}", response_model=List[Dict[str, Any]])
# async def get_model(
#     model: str, 
#     api_key:str = Depends(api_key_header),
#     fields: Optional[List[str]] = Query(None)
# ):
#     uid, models = get_connection(api_key)
#     if uid:
#         results = models.execute_kw(ODOO_DB, uid, api_key, model, 'search_read', [[]])
#         if results == None:
#             return json.dumps([])
        
#         return json.dumps(results)
#     else:
#         return json.dumps({'status': 'Connection failed'})
    
# Endpoint defined in a separate file
# from .endpoints import AnalyticAccount  # Adjust the import path based on your project structure
# app.include_router(AnalyticAccount.router)