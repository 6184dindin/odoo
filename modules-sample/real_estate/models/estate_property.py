from odoo import models, fields, api
from datetime import timedelta

class EstateProperty(models.Model):
    _name = 'estate_property'
    _description = 'Real Estate Property'

    name = fields.Char(string='Name', required=True, index=True, default='Unknown')
    description = fields.Text()
    postcode = fields.Char()
    # The availability date should not be copied when duplicating a record. The default availability date should be in 3 months.
    date_availability = fields.Datetime(string='Available From', copy=False, default=lambda self: fields.Datetime.now() + timedelta(days=90))
    expected_price = fields.Float()
    # The selling price should be read-only (it will be automatically filled in later)
    selling_price = fields.Float(readonly=True, store=True)
    bedrooms = fields.Integer(default=2)
    living_area = fields.Integer(string='Living Area (m²)')
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer(string='Garden Area (m²)')
    garden_orientation = fields.Selection([
        ('north', 'North'),
        ('south', 'South'),
        ('east', 'East'),
        ('west', 'West')
    ])
    active = fields.Boolean(default=True)
    status = fields.Selection([
        ('new', 'New'),
        ('offer_received', 'Offer Received'),
        ('offer_accepted', 'Offer Accepted'),
        ('sold', 'Sold'),
    ], default='new', required=True)
