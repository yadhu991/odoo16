from odoo import fields, models, api


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    is_vendor_products = fields.Boolean(string="Is vendor products")
    products_ids = fields.Many2many('product.product', string="products")

    @api.onchange('is_vendor_products', 'partner_id')
    def compute_products(self):
        search_rec = self.env['product.product'].search([('variant_seller_ids.partner_id.id', '=', self.partner_id.id)])
        rec = self.env['product.product'].search([('id', '!=', False)])
        self.products_ids = False
        if self.is_vendor_products:
            self.write({'products_ids': search_rec.ids})

        else:
            self.write({'products_ids': rec.ids})

    @api.onchange('partner_id','is_vendor_products')
    def clear_product(self):

        for item in self.order_line:
            if self.is_vendor_products:
                if self.partner_id.id not in item.product_id.variant_seller_ids.partner_id.ids:
                    item.unlink()
