from odoo import models, fields, api

class SaleConfig(models.TransientModel):

    _inherit = 'res.config.settings'

    users_id = fields.Many2many(
        'res.users', 'users_conf_order',
        'users_mail_id', 'order_conf_id', string='Assigned Users'
    )
