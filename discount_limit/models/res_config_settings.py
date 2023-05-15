from odoo import fields, models, api


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    discount_limit = fields.Float(string="amount : ")
    active = fields.Boolean(string="Discount limit", store=True)

    def set_values(self):
        res = super(ResConfigSettings, self).set_values()
        self.env['ir.config_parameter'].sudo().set_param('discount.discount_limit', self.discount_limit)
        self.env['ir.config_parameter'].sudo().set_param('discount.active', self.active)
        self.discount_limit = self.env['ir.config_parameter'].get_param('discount.discount_limit')
        return res

    @api.model
    def get_values(self):
        res = super(ResConfigSettings, self).get_values()
        ICPSudo = self.env['ir.config_parameter'].sudo()
        res.update(
            discount_limit=ICPSudo.get_param('discount.discount_limit'),
            active=ICPSudo.get_param('discount.active'),
        )
        return res
