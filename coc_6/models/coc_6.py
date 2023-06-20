from odoo import fields, models


class Coc6(models.Model):
    _inherit = 'res.partner'

    property = fields.Image(string="Partner Details",
                                 )
    # customer_properties_definition = fields.PropertiesDefinition(
    #     'Customer Properties')


