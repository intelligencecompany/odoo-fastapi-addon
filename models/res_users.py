# models/res_users.py
from odoo import models, fields, api, _

class OpenModel(models.Model):
    _name = 'openapi.model'
    _description = 'OpenAPI Model'
        
    name = fields.Char('Name')
    # description = fields.Text('Description')

    @api.model
    def action_button_1(self):
        # Define action for button 1
        self.ensure_one()
        self.name = 'Button 1 Clicked'
        pass

    @api.model
    def action_button_2(self):
        # Define action for button 2
        self.ensure_one()
        self.name = 'Button 2 Clicked'
        pass

    @api.model
    def action_button_3(self):
        # Define action for button 3
        self.ensure_one()
        self.name = 'Button 3 Clicked'
        pass