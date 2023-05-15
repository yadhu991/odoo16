from odoo import fields, models


class PurchaseOrderLine(models.Model):
    _inherit = ['purchase.order.line']

    vendor_checkbox = fields.Boolean(string="vendor product")
    vendor_products_ids = fields.Many2many(related='order_id.products_ids')


