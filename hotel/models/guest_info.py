from odoo import models, fields


class GuestInfo(models.Model):
    _name = "guest.info"
    _description = "information's about guests"
    _rec_name = 'partner_id'
    partner_id = fields.Many2one(
        comodel_name='res.partner',
        string="Guest",
        required=True, readonly=False, change_default=True, index=True,

    )
    guest_age = fields.Integer(string="Age")
    gender = fields.Selection(selection=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')], string="Gender",
                              default='male')
    accommodation_id = fields.Many2one('hotel.property', string="Accommodation Id", readonly=True)
