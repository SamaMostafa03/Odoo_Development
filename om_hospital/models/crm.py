from odoo import models, fields, api
from odoo.exceptions import ValidationError

class CRM(models.TransientModel):

    _inherit = ['crm.lead.lost']

    reason = fields.Html(string="Lost Reason" , store=True)


    def action_lost_reason_apply(self):
        leads = self.env['crm.lead'].browse(self.env.context.get('active_ids'))
        leads.action_set_lost(reason=self.reason)
