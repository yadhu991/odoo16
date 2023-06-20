# -*- coding: utf-8 -*-

from odoo import fields, models


class ResPartner(models.Model):
    """fields for Due limit"""
    _inherit = 'res.partner'

    pos_due_limit_checkbox = fields.Boolean("Due Limit")
    pos_due_limit = fields.Integer("Limit")
