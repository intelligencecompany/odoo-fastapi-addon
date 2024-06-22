
from odoo import http
import requests
import json
import logging

class FastApiController(http.Controller):
    @http.route('/openapi.json', methods=['GET'], auth='public')
    def openapi(self):
        url = 'http://127.0.0.1:8000/openapi.json'
        response = requests.get(url)
        return response.content
    
    @http.route('/api/docs', methods=['GET'], auth='public')
    def docs(self):
        url = 'http://127.0.0.1:8000/docs'
        response = requests.get(url)
        return response.content
    
    # @http.route('/api/test', methods=['GET'], auth='public')
    # def test(self):
    #     try:            
    #         x_key_header = http.request.httprequest.headers.get('x-key')
    #         headers = {
    #             'x-key': x_key_header
    #         }

    #         url = 'http://127.0.0.1:8000/api/test'
    #         response = requests.get(url=url, headers=headers)
    #         response.raise_for_status()
    #         # Parse the response content as JSON
    #         response_json = response.json()
    #         # Return the JSON response
    #         return response_json
    #     except requests.exceptions.RequestException as e:
    #         logging.error(e)
    #         response_data = {'error': str(e)}
    #         return json.dumps(response_data)
        
    # @http.route('/api/models', methods=['GET'], auth='public')
    # def models(self):       
    #     x_key_header = http.request.httprequest.headers.get('x-key')
    #     headers = {
    #         'x-key': x_key_header
    #     }
    #     url = 'http://127.0.0.1:8000/api/models'
    #     response = requests.get(url=url, headers=headers)
    #     # Parse the response content as JSON
    #     response_json = response.json()
    #     # Return the JSON response
    #     return response_json
    
    @http.route('/api/<string:action>', methods=['GET'], auth='public')
    def model(self, action=None):
        x_key_header = http.request.httprequest.headers.get('x-key')
        headers = {
            'x-key': x_key_header
        }

        url = f'http://127.0.0.1:8000/api/{action}'
        response = requests.get(url=url, headers=headers)
        # Parse the response content as JSON
        response_json = response.json()
        # Return the JSON response
        return response_json