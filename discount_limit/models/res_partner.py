from odoo import fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    discount_total = fields.Float(compute="compute_total", string=" given discount")

    def compute_total(self):
        """compute discounts given monthly"""
        for rec in self:
            currentMonth = fields.Datetime.now().month
            search_rec = rec.env['sale.order'].search([('partner_id', '=', rec.id)])
            for item in search_rec.filtered(lambda x: x.date_order.month == currentMonth):
                rec.discount_total += item.discount_here


