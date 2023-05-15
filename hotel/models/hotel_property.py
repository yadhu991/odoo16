from odoo import fields, models, api

from datetime import timedelta

from odoo.exceptions import ValidationError


class HotelProperty(models.Model):
    _name = "hotel.property"
    _description = "Accommodation"
    _inherit = 'mail.thread'
    _rec_name = 'reference_no'

    """accommodation fields"""

    partner_id = fields.Many2one(
        comodel_name='res.partner',
        string="Guest",
        required=True, index=True
    )
    created_date = fields.Datetime(default=fields.Datetime.today())
    payment_id = fields.Many2one('account.move', string="Invoice")
    payment_state = fields.Selection(related="payment_id.payment_state", string="payment state")
    room_id = fields.One2many('hotel.room', 'reception_id', string="Room")
    room_rent = fields.Monetary(related="room_id.fee", string="Room rent per day", required=True)

    number_of_guests = fields.Integer(string="Number of guests", tracking=True)
    date_check_in = fields.Datetime('Check-in-date', tracking=True)
    date_check_out = fields.Datetime('Check-out-date', tracking=True)
    type = fields.Selection(
        string='Bed-Type',
        selection=[('single', 'Single'), ('double', 'Double'), ('dormitory', 'Dormitory'), ],
        help="Type is used to select type of bed that you wanted")

    reference_no = fields.Char(string='Order Reference',
                               readonly=True, default=lambda self: 'New')
    room_facilities_id = fields.Many2many('room.tags', string='Room facilities')
    expected_days = fields.Integer(string="Expected days")
    date_field_check_in = fields.Datetime(string='Check-in date', readonly=True)
    date_field_check_out = fields.Datetime(string='Check-out date', readonly=True)

    state = fields.Selection(
        selection=[('draft', "draft"), ('check-in', "check-in"), ('check-out', "check-out"),
                   ('cancel', "Cancelled")], string="Status", default='draft')
    guest_info_id = fields.One2many('guest.info', 'accommodation_id', string='Guest information')
    payment_ids = fields.One2many('payment.guest', 'acc_id', string='list')

    status = fields.Selection(related="room_id.state", string="Room status")
    # attachment_ids = fields.Many2many('ir.attachment', compute='_compute_attachments',
    #                                   required=True)
    company_id = fields.Many2one('res.company', store=True, copy=False,
                                 string="Company",
                                 default=lambda self: self.env.user.company_id.id)
    currency_id = fields.Many2one('res.currency', string="Currency",
                                  related='company_id.currency_id',
                                  default=lambda self: self.env.user.company_id.currency_id.id)
    total = fields.Monetary(compute='_compute_total', string="total")
    order_id = fields.Many2one('order.food', readonly=True)

    def show_invoice(self):
        """ for showing invoice"""
        return {
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'res_model': 'account.move',
            'res_id': self.payment_id.id,
        }

    def show_order(self):
        """ for showing order"""
        if not self.order_id:
            order = self.env['order.food'].create({'room_id': self.room_id.id})
            return {
                'type': 'ir.actions.act_window',
                'view_mode': 'form',
                'res_model': 'order.food',
                'res_id': order.id,
            }
        else:
            return {
                'type': 'ir.actions.act_window',
                'view_mode': 'form',
                'res_model': 'order.food',
                'res_id': self.order_id.id,
            }

    @api.depends('payment_ids')
    def _compute_total(self):
        """ for computing total"""
        self.total = 0
        for update in self.payment_ids:
            self.total += update.sub_total

    @api.model
    def create(self, vals):
        """for creating sequence for accommodation"""
        if vals.get('reference_no', 'New') == 'New':
            vals['reference_no'] = self.env['ir.sequence'].next_by_code(
                'hotel.property') or 'New'
        return super(HotelProperty, self).create(vals)

    def action_checkout(self):
        """action for checkout button"""
        self.state = "check-out"
        self.room_id.state = "available"
        self.date_field_check_out = fields.Datetime.today()

        payment_list = []
        for item in self.payment_ids:
            payment_list.append(fields.Command.create({
                'name': item.product_name.name,
                'quantity': item.quantity,
                'price_unit': item.unit_price,
                'price_subtotal': item.sub_total,
            }))

        invoice_vals = self.env['account.move'].create([
            {
                'move_type': 'out_invoice',
                'invoice_date': fields.Date.context_today(self),
                'partner_id': self.partner_id.id,
                'amount_total': self.total,
                'invoice_origin': self.reference_no,
                'invoice_line_ids': payment_list

            },
        ])
        self.write({'payment_id': invoice_vals.id})
        return {
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'res_model': 'account.move',
            'res_id': invoice_vals.id,
            'context': self.env.context
        }

    def action_cancel(self):
        """action for cancel button"""
        self.state = "cancel"
        self.room_id.state = "available"
        return True

    def action_draft(self):
        """action for draft button"""
        self.state = "draft"

        return True

    @api.depends('guest_info_id')
    def action_confirm(self):
        """raise warnings when given guest details are mismatch also for attaching docs"""

        guest_number = len(self.guest_info_id)
        if self.number_of_guests > guest_number:
            raise ValidationError("Please provide details of all the guests!!!")
        if self.number_of_guests == 0:
            raise ValidationError("Number of guests should not be 0!!!")

        else:
            if self.number_of_guests < guest_number:
                raise ValidationError("check number of  guests!!!")
            # if not self.attachment_ids:
            #     raise ValidationError('Attach the required  documents for address proof!!!')
            self.state = "check-in"
            self.room_id.state = "booked"
            self.room_id.guest_id = self.partner_id
            self.date_field_check_in = fields.Datetime.today()
            for rec in self.room_id:
                print(rec.days, rec.fee, rec.reception_id.id)
                self.payment_ids.create({'product_name': 4,
                                         'quantity': rec.days,
                                         'unit_price': rec.fee,
                                         'acc_id': rec.reception_id.id,
                                         })

    # def _compute_attachments(self):
    #     """compute attachments"""
    #     attachment_ids = self.env['ir.attachment'].search([
    #         ('res_model', '=', self._name),
    #         ('res_id', '=', self.id)
    #     ])
    #     self.attachment_ids = attachment_ids.ids

    @api.onchange('expected_days')
    def onchange_expected_days(self):
        """compute expected days"""
        for item in self:
            if item.expected_days:
                item.date_check_out = fields.Datetime.add(fields.Datetime.now(), days=item.expected_days)
