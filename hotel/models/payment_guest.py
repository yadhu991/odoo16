from odoo import fields, models, api


class PaymentGuest(models.Model):
    _name = "payment.guest"
    _description = "payment"
    _rec_name = 'product_name'

    product_name = fields.Many2one('order.menu', string="Name", )
    description = fields.Char(string="Description", )
    quantity = fields.Integer(string="Quantity", default=1)
    uom = fields.Many2one('uom.uom', string="Uom", )
    company_id = fields.Many2one('res.company', store=True, copy=False,
                                 string="Company",
                                 default=lambda self: self.env.user.company_id.id)
    currency_id = fields.Many2one('res.currency', string="Currency",
                                  related='company_id.currency_id',
                                  default=lambda self: self.env.user.company_id.currency_id.id)
    unit_price = fields.Monetary(string="Unit price", )
    sub_total = fields.Float(compute='compute_subtotal', string="Sub total", )
    acc_id = fields.Many2one('hotel.property', )

    @api.depends('unit_price', 'quantity')
    def compute_subtotal(self):
        """ update subtotal"""
        for update in self:
            update.sub_total = update.quantity * update.unit_price
