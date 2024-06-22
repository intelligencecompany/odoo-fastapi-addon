
from odoo import http
import requests

class FastApiController(http.Controller):
    @http.route('/api/docs', auth='public')
    def handler(self):
        url = 'http://localhost:8000/docs'
        response = requests.get(url)
        return response
    
    @http.route('/api/test', auth='public')
    def handler(self):
        url = 'http://localhost:8000/test'
        response = requests.get(url)
        return response.json()
    
    @http.route('/api/partners', auth='public')
    def handler(self):
        url = 'http://localhost:8000/partners'
        response = requests.get(url)
        return response.json()