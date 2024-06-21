# models/res_users.py
from odoo import models, fields

class ResUsers(models.Model):
    _inherit = 'res.users'
    
    fastapi_url = fields.Char(string="FASTAPI URL")
