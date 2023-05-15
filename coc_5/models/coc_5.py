from odoo import fields, models


class Coc5(models.Model):
    _name = "coc.5"
    _description = "coc 5 "

    state = fields.Selection(
        selection=[('Pass', 'Pass'), ('Fail', 'Fail')], string="Resistance", default='Fail')
