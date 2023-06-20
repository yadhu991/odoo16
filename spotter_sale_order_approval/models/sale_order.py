# -*- coding: utf-8 -*-

from odoo import fields, models
from odoo.exceptions import ValidationError


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    state = fields.Selection(
        selection_add=[('verification', 'Approval'), ('sent',)])

    def action_confirm(self):
        res = super(SaleOrder, self).action_confirm()
        if self.amount_total > 25000:
            self.state = 'verification'

        return res

    def action_quotation_send(self):
        if self.amount_total > 25000 and self.state == 'draft':
            raise ValidationError("Since the  amount is higher it should be "
                                  "approved by the Manager. Click Confirm "
                                  "button to send for approval.")

        return super(SaleOrder, self).action_quotation_send()

    def action_confirm_quotation(self):

        return super(SaleOrder, self).action_confirm()

    def action_refuse_quotation(self):

        self.state = 'draft'
