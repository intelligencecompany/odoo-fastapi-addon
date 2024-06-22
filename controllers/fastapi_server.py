from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import APIKeyHeader
from fastapi.responses import RedirectResponse
import uvicorn
import xmlrpc.client
import logging
import json

ODOO_URL = 'http://127.0.0.1:8069'
ODOO_DB = 'azureuser'
ODOO_USERNAME = 'admin'

app = FastAPI()



api_key_header = APIKeyHeader(name='x-key')

async def create_dynamic_endpoint(model: str, method: str):
    method = method.upper()
    if method == 'GET':
        setattr(app, 'get_' + model, lambda: get_model(model))
    elif method == 'POST':
        setattr(app, 'post_' + model, lambda: get_model(model))

def get_models():
    api_key = 'admin'
    uid, models = get_connection(api_key)
    model_ids = models.execute_kw(ODOO_DB, uid, api_key, 'ir.model', 'search', [[]])
    model_names = models.execute_kw(ODOO_DB, uid, api_key, 'ir.model', 'read', [model_ids, ['model', 'name']])

    for n in model_names:
        app.add_api_route(f'api/{n.model}', create_dynamic_endpoint(n.model, 'GET'), methods=['GET'])

# XML-RPC connection
def get_connection(api_key: str):
    common = xmlrpc.client.ServerProxy(f'{ODOO_URL}/xmlrpc/2/common')
    uid = common.authenticate(ODOO_DB, ODOO_USERNAME, api_key, {})
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

@app.get("/api/models")
async def get_models(api_key:str = Depends(api_key_header)):
    uid, models = get_connection(api_key)
    if uid:
        model_ids = models.execute_kw(ODOO_DB, uid, api_key, 'ir.model', 'search', [[]])
        model_names = models.execute_kw(ODOO_DB, uid, api_key, 'ir.model', 'read', [model_ids, ['model', 'name']])

        return json.dumps(model_names)
    else:
        return json.dumps({'status': 'Connection failed'})

@app.get("/api/{model}")
async def get_model(model: str, api_key:str = Depends(api_key_header)):
    uid, models = get_connection(api_key)
    if uid:
        partners = models.execute_kw(ODOO_DB, uid, api_key, model, 'search_read', [[]])
        return json.dumps(partners)
    else:
        return json.dumps({'status': 'Connection failed'})