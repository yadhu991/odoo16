"""partner inherit for availability of products """
from odoo import fields, models


class ResPartner(models.Model):
    """fields for choosing availability of products and categories"""
    _inherit = 'res.partner'

    allowed_products_ids = fields.Many2many(comodel_name='product.template',
                                            string="Allowed Products")
    allowed_product_category_ids = fields.Many2many(
        comodel_name='product.public.category', string="Allowed Categories")
    product_visibility_products = fields.Boolean("Products")
    product_visibility_category = fields.Boolean("Category")
