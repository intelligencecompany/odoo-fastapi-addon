# models/res_users.py
from odoo import models, fields, api

class FastApiModel(models.Model):
    _name = 'openapi.model'
    _description = 'OpenAPI Model'
    
    name = fields.Char(string='Name')
    fastapi_url = fields.Char(string="FASTAPI URL")

    @api.multi
    def action_button_1(self):
        # Define action for button 1
        pass

    @api.multi
    def action_button_2(self):
        # Define action for button 2
        pass

    @api.multi
    def action_button_3(self):
        # Define action for button 3
        pass