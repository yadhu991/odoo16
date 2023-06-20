# -*- coding: utf-8 -*-

from odoo import models, fields
from odoo.http import request


class HrContract(models.Model):
    """inheriting the hr_contract for adding the functionality of sending
    contract expiry mail"""
    _inherit = 'hr.contract'

    def get_contracts(self):
        """to get running contracts which are going to be expired within the
        given days in the settings"""
        params = request.env['ir.config_parameter'].sudo()
        expiry_mail_active = params.get_param('expiry_mail.active')
        if expiry_mail_active:
            days = params.get_param('days')
            today = fields.Date.today()
            running_contracts = self.search(
                [('state', '=', 'open'), ('date_end', '!=', False)])
            for item in running_contracts:
                date = fields.Datetime.add(item.date_end, days=-(int(days)))
                if today == date:
                    item.action_send_email()

    def action_send_email(self):
        """to send the contract expiry mail to hr manager"""
        mail_template = self.env.ref('employee_contract_expiry.contract_expire')
        mail_template.send_mail(self.ids[0])
