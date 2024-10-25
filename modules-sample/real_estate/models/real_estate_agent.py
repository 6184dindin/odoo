from odoo import models, fields


class RealEstateAgent(models.Model):
    _name = "real.estate.agent"
    _description = "Real Estate Agent"

    name = fields.Char(string="Name", required=True)
    phone = fields.Char(string="Phone")
    email = fields.Char(string="Email")
    license_number = fields.Char(string="License Number")
    active = fields.Boolean(string="Active", default=True)
