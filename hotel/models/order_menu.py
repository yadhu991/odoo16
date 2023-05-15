from odoo import models, fields
from odoo import Command


class OrderMenu(models.Model):
    _name = "order.menu"
    _description = "menu"
    name = fields.Char(required=True)
    category = fields.Many2one('food.categories', string="Category")
    quantity = fields.Integer(string="Quantity", )
    order_id = fields.Many2one('order.food')
    accommodation_id = fields.Many2one(related="order_id.accommodation_id", string="Accommodation Id")


