from odoo import fields, models, api


class CocBot4(models.Model):
    _name = "coc.bot.4"
    _description = "coc"

    partner_id = fields.Many2one(
        comodel_name='res.partner',
        string="Partner",
        required=True, index=True
    )
