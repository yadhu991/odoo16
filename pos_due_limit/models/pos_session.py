# -*- coding: utf-8 -*-

from odoo import models


class PosSession(models.Model):
    """for inheriting POS session"""
    _inherit = 'pos.session'

    def _loader_params_res_partner(self):
        """for loading fields into POS"""
        result = super()._loader_params_res_partner()
        result['search_params']['fields'].append('pos_due_limit')
        return result
