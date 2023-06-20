from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    pos_payment_method_id = fields.Many2one('pos.payment.method',
                                            related='pos_config_id'
                                                    '.pos_payment_method_id',
                                            string="Payment Method : ",
                                            readonly=False,
                                            store=True)
    due_limit = fields.Boolean(related='pos_config_id.due_limit',
                               string="Due limit", readonly=False, store=True)


