from odoo import fields, models


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def create_wizard(self):
        wizard = self.env['import.wizard'].create({

            'order': self.id
        })
        return {
            'name': 'Import Items',
            'type': 'ir.actions.act_window',
            'res_model': 'import.wizard',
            'view_mode': 'form',
            'res_id': wizard.id,
            'target': 'new'
        }
