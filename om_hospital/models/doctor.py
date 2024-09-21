from odoo import fields, models, api


class Doctor(models.Model):
    _name = 'hospital.doctor'
    _description = 'Hospital Doctors Table'

    name = fields.Char()
    image = fields.Image(string='Image of doctor')
    age = fields.Integer(string='Age of doctor')
    gender = fields.Selection([
        ("male", "Male"),
        ("female", "Female")

    ], string="Gender")
    patient_ids = fields.Many2many('hospital.patient', string="Patients")
