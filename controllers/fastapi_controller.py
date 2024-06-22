
from odoo import http
import requests
import json

class FastApiController(http.Controller):
    @http.route('/openapi.json', auth='public')
    def openapi(self):
        url = 'http://127.0.0.1:8000/openapi.json'
        response = requests.get(url)
        return response.content
    
    @http.route('/api/docs', auth='public')
    def docs(self):
        url = 'http://127.0.0.1:8000/docs'
        response = requests.get(url)
        return response.content
    
    @http.route('/api/test', auth='public')
    def test(self):
        url = 'http://127.0.0.1:8000/api/test'
        response = requests.get(url)
        return json.dumps(response.text)
    
    @http.route('/api/partners', auth='public')
    def parnters(self):
        url = 'http://127.0.0.1:8000/api/partners'
        response = requests.get(url)
        return json.dumps(response.text)