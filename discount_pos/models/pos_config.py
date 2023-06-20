# -*- coding: utf-8 -*-

from odoo import fields, models


class PosConfig(models.Model):
    _inherit = 'pos.config'

    discount = fields.Boolean(string="discount", store=True)
    discount_type = fields.Selection(
        selection=[('percentage', "Percentage"), ('amount', "Amount")], string="Discount type", default='percentage')