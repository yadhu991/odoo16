from odoo import fields, models, api, _


class FoodCategories(models.Model):
    _name = "food.categories"
    _description = "categories"

    name = fields.Char(string="category name", required=True)
    color = fields.Integer(string="Color Picker")
    products_ids = fields.One2many('order.menu', 'category', string="products")
