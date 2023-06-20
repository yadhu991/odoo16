# -*- coding: utf-8 -*-
from odoo import fields, models


class ProductProduct(models.Model):
    """field for choosing owner"""
    _inherit = 'product.product'

    owner_id = fields.Many2one(comodel_name='res.partner',
                               string=" Product Owner")
