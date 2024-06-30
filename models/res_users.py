# models/res_users.py
from odoo import models, fields, api, _
from ..controllers import fastapi_server

class OpenModel(models.Model):
    _name = 'openapi.model'
    _description = 'OpenAPI Model'
        
    name = fields.Char('Name')
    description = fields.Text('Description')
    status = fields.Boolean(True)

    def action_button_1(self):
        # Define action for button 1
        self.ensure_one()
        fastapi_server.start_fastapi_in_thread()
    # self.status = True
        return True

    def action_button_2(self):
        # Define action for button 2
        self.ensure_one()
        fastapi_server.stop_fastapi()
        # self.status = False
        return True

    def action_button_3(self):
        # Define action for button 3
        self.ensure_one()
        # self.name = 'Button 3 Clicked'
        return True