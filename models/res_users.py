# models/res_users.py
from odoo import models, fields

class OpenModel(models.Model):
    _name = 'openapi.model'
    _description = 'OpenAPI Model'
    
    name = fields.Char(string='Name')
    description = fields.Text(string='Description')

    def action_button_1(self):
        # Define action for button 1
        self.ensure_one()
        self.name = 'Button 1 Clicked'
        pass

    def action_button_2(self):
        # Define action for button 2
        self.ensure_one()
        self.name = 'Button 2 Clicked'
        pass

    def action_button_3(self):
        # Define action for button 3
        self.ensure_one()
        self.name = 'Button 3 Clicked'
        pass