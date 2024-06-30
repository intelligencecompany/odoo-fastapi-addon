# models/res_users.py
from odoo import models, fields, api, _
from ..controllers import fastapi_server

class OpenModel(models.Model):
    _name = 'openapi.model'
    _description = 'OpenAPI Model'
        
    name = fields.Char('Name')
    description = fields.Text('Description')
    status = fields.Boolean(True)

    @api.model
    def action_button_1(self, args):
        # Define action for button 1
        # self.ensure_one()
        fastapi_server.start_fastapi_in_thread()
        self.status = True
        return True

    @api.model
    def action_button_2(self, args):
        # Define action for button 2
        # self.ensure_one()
        fastapi_server.stop_fastapi()
        self.status = False
        return True

    @api.model
    def action_button_3(self, args):
        # Define action for button 3
        self.ensure_one()
        self.name = 'Button 3 Clicked'
        return True