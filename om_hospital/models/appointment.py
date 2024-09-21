from email.policy import default

from odoo import fields, models, api
from pkg_resources import require


class Appointment(models.Model):
    _name = 'hospital.appointment'
    _description = 'Hospital Doctors Table'
    _inherit = ['mail.thread' , 'mail.activity.mixin']
    _rec_name = 'patient_id'

    patient_id = fields.Many2one(
        comodel_name='hospital.patient',
        string='Patient',
        options={'no_create': True, 'no_create_edit': True}
    )

    appointment_time = fields.Datetime(string="Appointment Time" , default= fields.Datetime.now)
    booking_date = fields.Date(string="Booking Date")
    gender = fields.Selection(related='patient_id.gender')
    prescription = fields.Html(string="Prescription")
    pharmacy_name = fields.Char(string="Pharmacy Name")

    priority = fields.Selection([
        ('0', 'Normal'),
        ('1', 'Low'),
        ('2', 'High'),
        ('3', 'Very High')], string="Priority")

    state = fields.Selection([
        ('draft', 'Draft'),
        ('in_consultation', 'In Consultation'),
        ('done', 'Done'),
        ('cancel', 'Cancelled')], default='draft' , string="Status", required = True)


    doctor_id = fields.Many2one('res.users',string="Doctor")