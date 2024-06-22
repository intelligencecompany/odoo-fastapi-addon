from fastapi import FastAPI
from fastapi.responses import RedirectResponse
import uvicorn
import xmlrpc.client
import logging

ODOO_URL = 'http://127.0.0.1:8069'
ODOO_DB = 'azureuser'
ODOO_USERNAME = 'admin'

app = FastAPI()

# XML-RPC connection
def get_connection(api_key: str)-> str:
    print(f'{ODOO_URL}/xmlrpc/2/common')
    logging.info(f'{ODOO_URL}/xmlrpc/2/common')
    common = xmlrpc.client.ServerProxy(f'{ODOO_URL}/xmlrpc/2/common')
    print(common)
    logging.info(common)
    uid = common.authenticate(ODOO_DB, ODOO_USERNAME, api_key, {})
    models = xmlrpc.client.ServerProxy(f'{ODOO_URL}/xmlrpc/2/object')
    return uid, models

@app.get("/test")
async def test_connection():
    api_key = 'AdminOdoo2024!'
    uid, models = get_connection(api_key)
    if uid:
        return {'status': 'Connection successful', 'uid': uid, 'models': models }
    else:
        return {'status': 'Connection failed', 'uid': uid }

@app.get("/partners")
async def get_partners():
    api_key = 'AdminOdoo2024!'
    uid, models = get_connection(api_key)
    if uid:
        partners = models.execute_kw(ODOO_DB, uid, api_key, 'res.partner', 'search_read', [[]])
        return partners
    else:
        return {'status': 'Connection failed'}

# subprocess.check_call([sys.executable, '-m', 'fastapi', 'dev', '-r', requirements_file])
# if __name__ == "__main__":
# uvicorn.run(app, host="0.0.0.0", port=8000)