from odoo import models, fields, api

class CRMLead(models.Model):
    _inherit = 'crm.lead'


    reason = fields.Html(string="Lost Reason")
