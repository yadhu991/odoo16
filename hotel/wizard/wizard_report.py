from datetime import date

import xlsxwriter
from odoo import fields, models
from odoo.exceptions import UserError
import io
import json

from odoo.tools import date_utils


class WizardReport(models.TransientModel):
    _name = "wizard.report"
    _description = "wizard for reporting "

    partner_id = fields.Many2many('res.partner', string="Guest")
    date_from = fields.Date(string="Date From")
    date_to = fields.Date(string="Date To")

    def fetch_data(self, ):
        customers = []
        partners = str(tuple(self.partner_id.ids))
        date_from = str(self.date_from)
        date_to = str(self.date_to)
        query = "SELECT hotel_property.id,reference_no,partner_id,res_partner.name,number_of_guests," \
                "date_field_check_in,date_field_check_out,state FROM hotel_property INNER JOIN res_partner ON " \
                "hotel_property.partner_id = res_partner.id"
        len_p = len(self.partner_id)
        if self.date_from and self.date_to:
            if self.date_from > self.date_to:
                raise UserError('From Date Greater Than To Date !')
        if self.partner_id:
            search_guest = self.env['hotel.property'].search([('partner_id', 'in', self.partner_id.ids)])
            if not search_guest:
                raise UserError('No Records')
            if len_p == 1:
                this = self.partner_id.id
                single_id = str(this)
                query += " WHERE partner_id = " + single_id + ""
            else:
                query += " WHERE partner_id in " + partners + ""

            if self.date_from:
                query += " and  created_date >= '" + date_from + "'"
            if self.date_to:
                query += " and created_date <= '" + date_to + "' "
        elif self.date_from:
            query += " WHERE  created_date >= '" + date_from + "'"
            if self.date_to:
                query += " and created_date <= '" + date_to + "' "
        elif self.date_to:
            query += " WHERE created_date <= '" + date_to + "' "
        self.env.cr.execute(query)
        docids = self.env.cr.dictfetchall()
        print(docids)
        for item in docids:
            customers.append(item['name'])
        res_partners = [*set(customers)]
        if not docids:
            raise UserError('No Records')
        data = {
            'docids': docids,
            'model_id': self.id,
            'partner_id': self.partner_id,
            'from_date': self.date_from,
            'to_date': self.date_to,
            'customer': res_partners,
            'current_date': date.today()
        }
        return data

    def action_confirm(self, ):
        """for generating pdf report"""
        data = self.fetch_data()
        return self.env.ref('hotel.action_report_hotel_management').report_action(self, data=data)

    def print_xlsx(self):
        """for generating xlsx report"""
        data = self.fetch_data()
        return {
            'type': 'ir.actions.report',
            'data': {'model': 'wizard.report',
                     'options': json.dumps(data,
                                           default=date_utils.json_default),
                     'output_format': 'xlsx',
                     'report_name': 'Hotel Report',
                     },
            'report_type': 'xlsx',
        }

    def get_xlsx_report(self, data, response):
        from_date = data['from_date']
        to_date = data['to_date']
        partner = data['customer']
        docids = data['docids']
        today = data['current_date']
        output = io.BytesIO()
        workbook = xlsxwriter.Workbook(output, {'in_memory': True})
        sheet = workbook.add_worksheet()
        cell_format = workbook.add_format(
            {'font_size': '12px', 'align': 'center'})
        head = workbook.add_format(
            {'align': 'center', 'bold': True, 'font_size': '20px', 'bg_color': '#d9d9d9'})
        bold = workbook.add_format(
            {'align': 'center', 'bold': True, 'font_size': '12px', 'bg_color': '#cccccc'})
        sheet.merge_range('B2:H3', ' Hotel Management Report', head)
        sheet.set_column(0, 8, 15)
        if from_date:
            sheet.write('B9', 'From Date:', bold)
            sheet.write('C9', from_date, cell_format)
        if to_date:
            sheet.write('F9', 'To Date:', bold)
            sheet.write('G9', to_date, cell_format)
        sheet.write('B5', 'Date :', bold)
        sheet.write('C5', today, cell_format)

        sheet.write('B7', 'Guests :', bold)
        x = 6
        y = 2
        for item in partner:
            sheet.write(x, y, item, cell_format)
            y += 1
        sheet.write('B11', 'S.L.No.', bold)
        sheet.write('C11', 'Reference.No.', bold)
        sheet.write('D11', 'Guest', bold)
        sheet.write('E11', 'No.of Guests', bold)
        sheet.write('F11', 'Check-IN', bold)
        sheet.write('G11', 'Check-OUT', bold)
        sheet.write('H11', 'State', bold)
        row = 11
        column = 1
        c = 1
        for item in docids:
            if item['date_field_check_in']:
                check_in_date = item['date_field_check_in'].split()[0]
                sheet.write(row, column + 4, check_in_date, cell_format)
            else:
                sheet.write(row, column + 4, '-', cell_format)

            if item['date_field_check_out']:
                check_out_date = item['date_field_check_out'].split()[0]
                sheet.write(row, column + 5, check_out_date, cell_format)
            else:
                sheet.write(row, column + 5, '-', cell_format)
            sheet.write(row, column, c, cell_format)
            sheet.write(row, column + 1, item['reference_no'], cell_format)
            sheet.write(row, column + 2, item['name'], cell_format)
            sheet.write(row, column + 3, item['number_of_guests'], cell_format)
            sheet.write(row, column + 6, item['state'], cell_format)
            row += 1
            c += 1
        workbook.close()
        output.seek(0)
        response.stream.write(output.read())
        output.close()
