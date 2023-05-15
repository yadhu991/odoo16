import base64
from io import BytesIO
import openpyxl

from odoo import fields, models
from odoo.exceptions import UserError


class ImportWizard(models.TransientModel):
    _name = "import.wizard"
    _description = "wizard for importing order lines"

    order = fields.Many2one('sale.order', readonly=True)
    file = fields.Binary(string="file")

    def import_order_lines(self):
        try:

            wb = openpyxl.load_workbook(

                filename=BytesIO(base64.b64decode(self.file)), read_only=True)

            ws = wb.active

            for record in ws.iter_rows(min_row=2, max_row=None, min_col=None,

                                       max_col=None, values_only=True):
                search_product = self.env['product.product'].search([('name', '=', record[0])])
                if search_product:
                    self.order.order_line.create({
                        'product_id': search_product.id,
                        'name': str(record[1]),
                        'product_uom_qty': record[2],
                        'price_unit': search_product.lst_price,
                        'product_uom': search_product.uom_id.id,
                        'order_id': self.order.id,
                    })
                if not search_product:
                    find_uom = self.env['uom.uom'].search([('name', '=', record[3])])
                    new_product = self.env['product.product'].create({
                        'name': str(record[0]),
                        'lst_price': record[4],
                        'uom_id': find_uom.id,
                        'uom_po_id': find_uom.id
                    })
                    self.order.order_line.create({
                        'product_id': new_product.id,
                        'name': str(record[1]),
                        'product_uom_qty': record[2],
                        'price_unit': new_product.lst_price,
                        'product_uom': new_product.id,
                        'order_id': self.order.id,
                    })
        except:
            raise UserError('Please insert a valid file')
