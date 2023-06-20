# -*- coding: utf-8 -*-

from odoo import models


class PosSession(models.Model):
    """for inheriting POS session"""
    _inherit = 'pos.session'

    def _loader_params_product_product(self):
        """for loading fields into POS"""
        result = super()._loader_params_product_product()
        result['search_params']['fields'].append('owner_id')
        return result
