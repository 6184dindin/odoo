# -*- coding: utf-8 -*-

from odoo import models, fields, api


class TestModel(models.Model):
    _name = 'test_model'
    _description = 'Test Model'

    name = fields.Char()
    value = fields.Integer()
    value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()
    age = fields.Integer()

    @api.depends('value')
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100

