
from odoo import models, fields, api


class Patient(models.Model):
    _name = 'hospital.patient'
    _inherit = ['mail.thread' , 'mail.activity.mixin']
    _description = 'Hospital Patients Table'

    fName = fields.Char(string="First Name", required=True , tracking=True)
    lName = fields.Char(string="Last Name", required=True, tracking=True)
    image = fields.Image(string='Image', tracking=True)
    age = fields.Integer(string='Age',required=True, tracking=True)
    gender = fields.Selection([
        ("male", "Male"),
        ("female", "Female")

    ], string="Gender", required=True, tracking=True)
    active = fields.Boolean(string="Active", default = False, tracking=True)
    email_id = fields.Char(string="Email", required=True, tracking=True)
    history = fields.Binary()
    user_id = fields.Many2one('res.users', string='Assigned User')  # New field for linking to a user


    @api.model
    def name_get(self):
        result = []
        for record in self:
            name = f"[{record.id}] {record.fName} {record.lName}"
            result.append((record.id, name))
        return result


    def action_send_mail(self):
        template_id = self.env.ref('om_hospital.email_tem_user').id
        template = self.env['mail.template'].browse(template_id)
        template.send_mail(self.id, force_send=True)


