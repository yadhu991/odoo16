from odoo import fields, models, api
from odoo.exceptions import UserError
from odoo.http import request


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    discount_here = fields.Float(string="discount given here")
    partner_discount = fields.Float(string="discount_update")
    total_disc = fields.Float(related="partner_id.discount_total", string="Total  Discount")

    def action_confirm(self):

        """ to update the total discount given to partner while confirming"""

        res = super(SaleOrder, self).action_confirm()
        self.discount_here = self.partner_discount
        return res

    @api.onchange('order_line')
    def onchange_order_line(self, net=0):

        """to calculate and update the total discount , raise warning if discount exceed the limit"""

        params = request.env['ir.config_parameter'].sudo()
        discount_limit = params.get_param('discount.discount_limit')
        total = float(discount_limit)
        self.partner_discount = 0
        if self.state == 'draft':
            for item in self.order_line:
                actual_total = item.product_uom_qty * item.price_unit
                net += actual_total

            invoice_total = self.amount_total
            given_discount = net - invoice_total
            self.partner_discount = given_discount
            new_total = self.partner_discount+self.total_disc
            if new_total >= total:
                raise UserError('discount limit exceeded')

