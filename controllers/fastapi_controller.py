
from odoo import http
import requests
from urllib.parse import urlencode
import json
import logging
from odoo import http
from odoo.http import request

def get_user_id(api_key: str):
    user_id = request.env["res.users.apikeys"]._check_credentials(
        scope="rpc", key=api_key
    )

    if not user_id:
            raise http.BadRequest("API key invalid")
    
    logging.info(f'Request for user: {user_id}')
    return user_id

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

        x_key_header = http.request.httprequest.headers.get('x-key')
        user_id = get_user_id(x_key_header)            

        headers = {
            'x-key': x_key_header,
            'user_id': user_id
        }

        url = f'http://127.0.0.1:8000/api/{action}'
        response = requests.get(url=url, headers=headers, params=params)
        
        return http.request.make_response(
            response.content,
            headers={'Content-Type': 'application/json'}, 
            status=response.status_code
        )

    @http.route('/api/<string:action>', type='http', methods=['POST'], auth='public', csrf=False)
    def create_record(self, action:str=None):
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


        if not data:
            return http.request.make_response(
                json.dumps({'error': 'Missing data'}),
                headers={'Content-Type': 'application/json'}, 
                status=400
            )
        
        x_key_header = http.request.httprequest.headers.get('x-key')              
        user_id = get_user_id(x_key_header)            

        headers = {
            'x-key': x_key_header,
            'user_id': user_id
        }

        url = f'http://127.0.0.1:8000/api/{action}'
        response = requests.post(url=url, headers=headers, data=json.dumps(data))
        
        if response.status_code == 200:
            return http.request.make_response(
                response.content,
                headers={'Content-Type': 'application/json'}, 
                status=response.status_code
            )
        else: 
            return http.request.make_response(
                json.dumps({'error': response.text}),
                headers={'Content-Type': 'application/json'}, 
                status=response.status_code
            )
        
    @http.route('/api/<string:action>/<int:id>', type='http', methods=['PUT'], auth='public', csrf=False)
    def update_record(self, action:str=None, id:int=-1):
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
        
        x_key_header = http.request.httprequest.headers.get('x-key')              
        user_id = get_user_id(x_key_header)            

        headers = {
            'x-key': x_key_header,
            'user_id': user_id
        }

        url = f'http://127.0.0.1:8000/api/{action}/{id}'
        response = requests.put(url=url, headers=headers, params=params, data=json.dumps(data))
        
        if response.status_code == 200:
            return http.request.make_response(
                json.dumps({'success': True}),
                headers={'Content-Type': 'application/json'}, 
                status=200
            )
        else: 
            return http.request.make_response(
                json.dumps({'error': response.text}),
                headers={'Content-Type': 'application/json'}, 
                status=response.status_code
            )

