from odoo import fields, models, api


class OrderList(models.Model):
    _name = "order.list"
    _description = "order list"
    _rec_name = 'product_name'

    product_name = fields.Many2one('order.menu', string="Product name")
    description = fields.Char(string="Description", )
    quantity = fields.Integer(string="Quantity", default=1)
    company_id = fields.Many2one('res.company', store=True, copy=False,
                                 string="Company",
                                 default=lambda self: self.env.user.company_id.id)
    currency_id = fields.Many2one('res.currency', string="Currency",
                                  related='company_id.currency_id',
                                  default=lambda self: self.env.user.company_id.currency_id.id)
    unit_price = fields.Float(string="Unit price", )
    sub_total = fields.Float(compute='compute_subtotal', string="Sub total", )
    order_id = fields.Many2one('order.food', )

    @api.depends('unit_price', 'quantity')
    def compute_subtotal(self):
        """ update subtotal"""
        for update in self:
            update.sub_total = update.quantity * update.unit_price
