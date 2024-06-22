from fastapi import FastAPI, Depends
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

key = APIKeyHeader(name='x-key')
# XML-RPC connection
def get_connection(api_key: str):
    common = xmlrpc.client.ServerProxy(f'{ODOO_URL}/xmlrpc/2/common')
    uid = common.authenticate(ODOO_DB, ODOO_USERNAME, api_key, {})
    models = xmlrpc.client.ServerProxy(f'{ODOO_URL}/xmlrpc/2/object')
    return uid, models

@app.get("/api/test")
async def test_connection(api_key:str = Depends(key)):
    # api_key = 'admin'
    uid, models = get_connection(api_key)
    if uid:
        return json.dumps({'status': 'Connection successful', 'uid': uid })
    else:
        return json.dumps({'status': 'Connection failed' })

# @app.get("/api/partners")
# async def get_partners():
#     api_key = 'admin'
#     uid, models = get_connection(api_key)
#     if uid:
#         partners = models.execute_kw(ODOO_DB, uid, api_key, 'res.partner', 'search_read', [[]])
#         return json.dumps(partners)
#     else:
#         return json.dumps({'status': 'Connection failed'})

@app.get("/api/{model}")
async def get_partners(model: str, api_key:str = Depends(key)):
    uid, models = get_connection(api_key)
    if uid:
        partners = models.execute_kw(ODOO_DB, uid, api_key, model, 'search_read', [[]])
        return json.dumps(partners)
    else:
        return json.dumps({'status': 'Connection failed'})
# subprocess.check_call([sys.executable, '-m', 'fastapi', 'dev', '-r', requirements_file])
# if __name__ == "__main__":
# uvicorn.run(app, host="0.0.0.0", port=8000)