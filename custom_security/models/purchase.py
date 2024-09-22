from odoo import models, fields, api , _
from odoo.exceptions import AccessError


class Purchase(models.Model):

    _inherit = ['purchase.order']

    def button_confirm(self):
        current_user = self.env.user
        restricted_group = self.env.ref('custom_security.access_confirmation_of_purchase_order')
        if restricted_group in current_user.groups_id:
            raise AccessError(_("You do not have permission to confirm Purchase Orders."))
        return super(Purchase, self).button_confirm()

