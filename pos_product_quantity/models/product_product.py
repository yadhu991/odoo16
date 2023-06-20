# -*- coding: utf-8 -*-

from odoo import fields, models


class PosConfig(models.Model):
    _inherit = 'product.product'

    available_quantity = fields.Integer("Available Quantity",compute="_compute_quantity")

    def _compute_quantity(self):
        for rec in self:
            search_rec = rec.env['pos.config'].search([])
            loc_id = search_rec.picking_type_id.default_location_src_id.id
            if rec.detailed_type == 'product':
                search_stock = self.env['stock.quant'].search(
                    [('location_id', '=', loc_id), ('product_id', '=', rec.id)])
                if search_stock:
                    quantity = search_stock.quantity
                    if quantity > 0:
                        rec.available_quantity = quantity
                    else:
                        rec.available_quantity = 0
                else:
                    rec.available_quantity = 0
            else:
                rec.available_quantity = 0
