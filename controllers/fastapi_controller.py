
from odoo import http
import requests

class FastApiController(http.Controller):
    @http.route('/api/docs', auth='public')
    def docs(self):
        url = 'http://127.0.0.1:8000/docs'
        response = requests.get(url)
        return response
    
    @http.route('/api/test', auth='public')
    def test(self):
        url = 'http://127.0.0.1:8000/test'
        response = requests.get(url)
        return response.json()
    
    @http.route('/api/partners', type='json', auth='public')
    def parnters(self):
        url = 'http://127.0.0.1:8000/partners'
        response = requests.get(url)
        return response