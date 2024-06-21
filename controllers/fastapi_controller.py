from fastapi import FastAPI
import uvicorn
import xmlrpc.client
from odoo import http, route
import requests


class FastApiController(http.Controller):
    @route('/api/partners', auth='public')
    def handler(self):
        url = 'http://localhost:8000/partners'
        response = requests.get(url)
        return response.json()
    
app = FastAPI()

ODOO_URL = 'https://dataruba.com'
ODOO_DB = 'azureuser'
ODOO_USERNAME = 'admin'
ODOO_PASSWORD = 'AdminOdoo2024!'

# XML-RPC connection
common = xmlrpc.client.ServerProxy(f'{ODOO_URL}/xmlrpc/2/common')
uid = common.authenticate(ODOO_DB, ODOO_USERNAME, ODOO_PASSWORD, {})
models = xmlrpc.client.ServerProxy(f'{ODOO_URL}/xmlrpc/2/object')

@app.get("/test")
async def test_connection():
    if uid:
        return {'status': 'Connection successful', 'uid': uid}
    else:
        return {'status': 'Connection failed'}

@app.get("/partners")
async def get_partners():
    if uid:
        partners = models.execute_kw(ODOO_DB, uid, ODOO_PASSWORD, 'res.partner', 'search_read', [[]])
        return partners
    else:
        return {'status': 'Connection failed'}
    
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)