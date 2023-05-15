from odoo import models, fields


class HotelProducts(models.Model):
    _name = "hotel.products"
    _description = "product"
    _rec_name = 'product_name'

    product_name = fields.Many2one('order.menu', string="Product name", required=True)
    category = fields.Many2one(related='product_name.category', string="Category")
    description = fields.Char(string="Description", )
    product_image = fields.Image()
    company_id = fields.Many2one('res.company', store=True, copy=False,
                                 string="Company",
                                 default=lambda self: self.env.user.company_id.id)
    currency_id = fields.Many2one('res.currency', string="Currency",
                                  related='company_id.currency_id',
                                  default=lambda self: self.env.user.company_id.currency_id.id)
    price = fields.Monetary(string="Price", required=True)

    quantity = fields.Integer(string="Quantity", )
    order_id = fields.Many2one('order.food')
    accommodation_id = fields.Many2one(related="order_id.accommodation_id", string="Accommodation Id")

    def add_quantity(self, ):
        """for adding quantity"""
        for rec in self:
            rec.quantity += 1

    def remove_quantity(self, ):
        """for removing  quantity"""
        for rec in self:
            rec.quantity -= 1

    def add_to_list(self, ):
        """for add to list"""
        for rec in self:
            rec.accommodation_id = rec.order_id.accommodation_id
            print(rec.accommodation_id.id, rec.product_name.id, rec.quantity, rec.price, rec.order_id.id)
            self.env['order.list'].create({'product_name': rec.product_name.id,
                                           'quantity': rec.quantity,
                                           'description': rec.description,
                                           'unit_price': rec.price,
                                           'order_id': rec.order_id.id,
                                           })

            self.env['payment.guest'].create({'product_name': rec.product_name.id,
                                              'quantity': rec.quantity,
                                              'description': rec.description,
                                              'unit_price': rec.price,
                                              'acc_id': rec.accommodation_id.id,
                                              })
            rec.quantity = 1
        return {
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'res_model': 'order.food',
            'res_id': self.order_id.id,
            'context': self.env.context
        }
