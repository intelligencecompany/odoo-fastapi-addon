
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
    
    @http.route('/api/test', methods=['GET'], auth='public')
    def test(self):
        url = 'http://127.0.0.1:8000/api/test'
        response = requests.get(url)
        # Parse the response content as JSON
        response_json = response.json()
        # Return the JSON response
        return response_json
    
    @http.route('/api/models', methods=['GET'], auth='public')
    def test(self):
        url = 'http://127.0.0.1:8000/api/models'
        response = requests.get(url)
        # Parse the response content as JSON
        response_json = response.json()
        # Return the JSON response
        return response_json

    # @http.route('/api/partners', methods=['GET'], auth='public')
    # def parnters(self):
    #     url = 'http://127.0.0.1:8000/api/partners'
    #     response = requests.get(url)
    #     # Parse the response content as JSON
    #     response_json = response.json()
    #     # Return the JSON response
    #     return response_json
    
    @http.route('/api/<string:model>', methods=['GET'], auth='public')
    def model(self, model=None):
        url = f'http://127.0.0.1:8000/api/{model}'
        response = requests.get(url)
        # Parse the response content as JSON
        response_json = response.json()
        # Return the JSON response
        return response_json