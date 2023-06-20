# -*- coding: utf-8 -*-

from odoo import fields, models, api


class ResConfigSettings(models.TransientModel):
    """to inherit employee settings """
    _inherit = 'res.config.settings'

    days = fields.Integer(string="Days :  ", default=1)
    expiry_mail_active = fields.Boolean(store=True)

    def set_values(self):
        """to set field values"""
        res = super(ResConfigSettings, self).set_values()
        self.env['ir.config_parameter'].sudo().set_param('days', self.days)
        self.env['ir.config_parameter'].sudo().set_param('expiry_mail.active',
                                                         self.expiry_mail_active)
        self.days = self.env['ir.config_parameter'].get_param('days')
        return res

    @api.model
    def get_values(self):
        """to super save button and save the field values"""
        res = super(ResConfigSettings, self).get_values()
        ICPSudo = self.env['ir.config_parameter'].sudo()
        res.update(
            days=ICPSudo.get_param('days'),
            expiry_mail_active=ICPSudo.get_param('expiry_mail.active'),
        )
        return res
