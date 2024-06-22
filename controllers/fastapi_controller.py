
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
        url = 'http://127.0.0.1:8000/partners'
        response = requests.get(url)
        return { 'url': url, 'status_code': response.status_code }