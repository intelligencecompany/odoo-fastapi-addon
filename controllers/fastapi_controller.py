
from odoo import http
import requests
from urllib.parse import urlencode
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
        
    @http.route('/api/<string:action>', type='http', methods=['GET'], auth='public')
    def get_records(self, action=None):
        params = {k: v for k, v in http.request.params.items() if k != 'action'}

        # query_string = urlencode(params)

        x_key_header = http.request.httprequest.headers.get('x-key')

        headers = {
            'x-key': x_key_header
        }

        url = f'http://127.0.0.1:8000/api/{action}'
        response = requests.get(url=url, headers=headers, params=params)
        
        return http.request.make_response(
            response.content,
            headers={'Content-Type': 'application/json'}
        )
    
    @http.route('/api/<string:action>/<int:id>', type='http', methods=['PUT'], auth='public', csrf=False)
    def update_record(self, action:str=None, id:int=-1):
        try:
            if http.request.httprequest.content_type != 'application/json':
                return http.request.make_response(
                    json.dumps({'error': 'Invalid Content-Type'}),
                    headers={'Content-Type': 'application/json'}, 
                    status=400
                )
            
            try:
                data = json.loads(http.request.httprequest.data)
            except json.JSONDecodeError:
                return http.request.make_response(
                    json.dumps({'error': 'Invalid JSON data'}),
                    headers={'Content-Type': 'application/json'}, 
                    status=400
                )


            if not id or id < 0 or not data:
                return http.request.make_response(
                    json.dumps({'error': 'Missing id or fields'}),
                    headers={'Content-Type': 'application/json'}, 
                    status=400
                )
                                    
            params = {k: v for k, v in http.request.params.items() if k != 'action' and k != 'id'}
            headers = {
                'x-key': http.request.httprequest.headers.get('x-key')
            }

            url = f'http://127.0.0.1:8000/api/{action}/{id}'
            response = requests.put(url=url, headers=headers, params=params, data=data)
            
            if response.status_code == 200:
                return http.request.make_response(
                    json.dumps({'success': True}),
                    headers={'Content-Type': 'application/json'}, 
                    status=200
                )
            else: 
                return http.request.make_response(
                    json.dumps({'error': 'Whoops, something failed'}),
                    headers={'Content-Type': 'application/json'}, 
                    status=response.status_code
                )
        except Exception as e:
            logging.error(e)
            print(e)

