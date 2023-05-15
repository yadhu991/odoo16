from odoo import fields, models, api, _
from datetime import datetime


class OrderFood(models.Model):
    _name = "order.food"
    _description = "Order"
    _inherit = 'mail.thread'
    _rec_name = 'reference_no'

    reference_no = fields.Char(string='Order Reference', required=True,
                               readonly=True, default=lambda self: 'New')
    room_id = fields.Many2one('hotel.room', string="Room", domain="[('state', '=', 'booked')]", tracking=True)
    accommodation_id = fields.Many2one(related="room_id.reception_id", string="Accommodation Id")
    guest_id = fields.Many2one(related="room_id.guest_id", string='Guest', tracking=True)

    order_time = fields.Datetime(string='Order time', default=datetime.today(), readonly=True)

    category_ids = fields.Many2many('food.categories', tracking=True)
    order_ids = fields.One2many('hotel.products', 'order_id', string='Menu')

    order_list_ids = fields.One2many('order.list', 'order_id', string='list')
    company_id = fields.Many2one('res.company', store=True, copy=False,
                                 string="Company",
                                 default=lambda self: self.env.user.company_id.id)
    currency_id = fields.Many2one('res.currency', string="Currency",
                                  related='company_id.currency_id',
                                  default=lambda self: self.env.user.company_id.currency_id.id)
    total = fields.Monetary(compute='_compute_total', string="total")

    @api.onchange('room_id')
    def change_order(self):
        """ update total based on items"""
        print(self.id)
        self.accommodation_id.write({'order_id': self.id})

    @api.depends('order_list_ids', )
    def _compute_total(self):
        """ update total based on items"""
        self.total = 0
        for update in self.order_list_ids:
            self.total += update.sub_total

    @api.model
    def create(self, vals):
        """for creating sequence for order"""
        if vals.get('reference_no', 'New') == 'New':
            vals['reference_no'] = self.env['ir.sequence'].next_by_code(
                'order.food') or 'New'
        return super(OrderFood, self).create(vals)

    @api.onchange('category_ids')
    def _add_menu(self):
        """for displaying products based on category in  order"""
        search_rec = self.env['hotel.products'].search([('category', 'in', self.category_ids.ids)])
        self.write({'order_ids': search_rec.ids})

    def add_to_list(self):
        """for add to list"""

        for rec in self.order_ids:
            self.order_list_ids.create({'name': rec.name,
                                        'quantity': rec.quantity,
                                        'unit_price': rec.price,
                                        })

    def show_accommodation(self):
        """ for showing accommodation"""
        return {
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'res_model': 'hotel.property',
            'res_id': self.accommodation_id.id,
        }
