from odoo import models, fields, api
import logging
_logger = logging.getLogger(__name__)

class SaleOrder(models.Model):

    _inherit = ['sale.order']

    available_products = fields.Many2many(
        'product.product', 'sale_order_available',
        'product_id', 'sale_order_id', string="Available Products"
    )

    selected_products = fields.Many2many(
        'product.product', 'sale_order_selected',
        'product_id', 'sale_order_id', string="Selected Products"
    )

    selected_users = fields.Many2many(
        'res.users', string="Selected Users", compute='_compute_selected_users' , readonly=True
    )

    @api.onchange('selected_users')
    @api.depends('selected_users')
    def _compute_selected_users(self):
        config = self.env['res.config.settings'].sudo().search([], order="id desc", limit=1)
        if config:
            self.selected_users = config.users_id


    def action_send_mail_custom(self):
        _logger.info("Email: sending")
        for user in self.selected_users:
            _logger.info(f"Email: sending to user: {user.email}")
            mail_values = {
                'email_to': user.email,
                'email_from': self.env.user.email,
                'subject': f"User Mail to {user.email}",
                'body_html': f"<p>Dear {user.name},<br /><br />Here is your mail.<br /><br />Do not hesitate to contact us if you have any questions.</p>",
            }
            try:
                mail = self.env['mail.mail'].create(mail_values)
                mail.send()
                _logger.info(f"Email sent to {user.email}")
            except Exception as e:
                _logger.error(f"Failed to send email to {user.email}: {str(e)}")




    @api.onchange('available_products')
    def _onchange_available_products(self):
        available_product_ids = self.available_products.ids
        selected_product_ids = self.selected_products.ids
        selected = []
        for prod_id in selected_product_ids:
            if prod_id in available_product_ids:
                selected.append(prod_id)

        self.selected_products = [(6, 0, [])]
        self.selected_products = selected

        if self.available_products:
            return { 'domain': {'selected_products': [('id', 'in', available_product_ids)]} }
        else:
            return {'domain': {'selected_products' : []} }


