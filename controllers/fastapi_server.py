from fastapi import Depends
from typing import List, Dict, Any
from fastapi.security import APIKeyHeader
import xmlrpc.client
import logging
import json 
from odoo import http
from odoo.http import request
from .endpoints import *

ODOO_URL = 'http://127.0.0.1:8069'

api_key_header = APIKeyHeader(name='x-key')

def get_user_id(api_key: str):
    if not api_key:
            raise http.make_response("API key invalid", status=400)

    user_id = request.env["res.users.apikeys"]._check_credentials(
        scope="rpc", key=api_key
    )

    if not user_id:
            raise http.make_response("API key invalid", status=400)
    
    user = request.env['res.users'].browse(user_id)

    if not user.exists():
        return request.make_response("User not found", status=400)
    
    logging.info(f'Request for user: {user_id} {user.login}')

    database_name = request.env.cr.dbname
    logging.info(f'Request database: {database_name}')

    return user.login, database_name

# XML-RPC connection
def get_connection(api_key: str):
    common = xmlrpc.client.ServerProxy(f'{ODOO_URL}/xmlrpc/2/common')

    user_id, database = get_user_id(api_key)
        
    uid = common.authenticate(database, user_id, api_key, {})
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