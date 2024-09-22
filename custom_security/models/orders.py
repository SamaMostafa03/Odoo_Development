from odoo import models, fields, api , _
from odoo.exceptions import AccessError


class SaleOrder(models.Model):

    _inherit = ['sale.order']

    def action_confirm(self):
        current_user = self.env.user
        restricted_group = self.env.ref('custom_security.access_confirmation_of_sale_order')
        if restricted_group in current_user.groups_id:
            raise AccessError(_("You do not have permission to confirm Sales Orders."))
        return super(SaleOrder, self).action_confirm()


