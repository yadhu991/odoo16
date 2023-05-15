from odoo import fields, models, api, _


class HotelRoom(models.Model):
    _name = "hotel.room"
    _description = "Hotel Room"
    _inherit = 'mail.thread'
    _rec_name = 'reference_no'

    reference_no = fields.Char(string='Order Reference', required=True,
                               readonly=True, default=lambda self: 'New')
    reception_id = fields.Many2one('hotel.property', string='Reception', tracking=True)
    days = fields.Integer(related='reception_id.expected_days')
    guest_id = fields.Many2one(related="reception_id.partner_id", string='guest', tracking=True)
    type = fields.Selection(
        string='Bed-Type',
        selection=[('single', 'Single'), ('double', 'Double'), ('dormitory', 'Dormitory'), ], tracking=True)
    attrs = fields.Char("Available beds", default="5")

    room_facilities_id = fields.Many2many('room.tags', string='Room facilities', tracking=True)
    company_id = fields.Many2one('res.company', store=True, copy=False,
                                 string="Company",
                                 default=lambda self: self.env.user.company_id.id)
    currency_id = fields.Many2one('res.currency', string="Currency",
                                  related='company_id.currency_id',
                                  default=lambda self: self.env.user.company_id.currency_id.id)
    fee = fields.Monetary(string="Fee", required=True)
    state = fields.Selection(
        selection=[('available', "Available"), ('booked', "Booked"),
                   ('cancel', "Cancelled"), ], string="Status", default='available')
    order_id = fields.Many2one('order.food')

    @api.model
    def create(self, vals):
        """for creating sequence for accommodation"""
        if vals.get('reference_no', 'New') == 'New':
            vals['reference_no'] = self.env['ir.sequence'].next_by_code(
                'hotel.room') or 'New'
        return super(HotelRoom, self).create(vals)

