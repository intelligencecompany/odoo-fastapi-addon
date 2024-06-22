import json
from odoo import http
import xmlrpc.client
import logging


ODOO_URL = 'http://127.0.0.1:8069'
ODOO_DB = 'azureuser'
ODOO_USERNAME = 'admin'
ODOO_PW = 'admin'

common = xmlrpc.client.ServerProxy(f'{ODOO_URL}/xmlrpc/2/common')
uid = common.authenticate(ODOO_DB, ODOO_USERNAME, ODOO_PW, {})
models = xmlrpc.client.ServerProxy(f'{ODOO_URL}/xmlrpc/2/object')
model_ids = models.execute_kw(ODOO_DB, uid, ODOO_PW, 'ir.model', 'search', [[]])
model_names = models.execute_kw(ODOO_DB, uid, ODOO_PW, 'ir.model', 'read', [model_ids, ['model', 'name']])


# Define a function to dynamically create controller classes
def create_odoo_controller(route, methods, function_name):
    methods = [m.upper() for m in methods]

    # Define a new class for each controller dynamically
    new_class = type(function_name.capitalize() + 'Controller', (http.Controller,), {
        function_name: lambda self, **kwargs: f"{methods} request received for {route}"
    })

    # Register the route dynamically
    http.root.add_routes([http.route(route, auth='public', methods=methods)(new_class())])

# Dynamically create controllers based on JSON input
for n in model_names:
    logging.info(n.model)
    route = f'/api/{n.model}'
    methods = ['GET']
    function_name = f'get_{n.model}'

    create_odoo_controller(route, methods, function_name)