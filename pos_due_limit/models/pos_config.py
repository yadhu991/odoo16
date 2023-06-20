from odoo import fields, models


class PosConfig(models.Model):
    _inherit = 'pos.config'

    pos_payment_method_id = fields.Many2one('pos.payment.method',
                                            string="Payment Method : ")
    due_limit = fields.Boolean(string="Due limit", store=True)
