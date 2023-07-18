# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from werkzeug import urls

from odoo import _, api, fields, models


class PaymentProvider(models.Model):
    _inherit = 'payment.provider'

    code = fields.Selection(
        selection_add=[('paytm', "Paytm")],
        ondelete={'paytm': 'set default'})
    paytm_merchant_id = fields.Char(
        string="Merchant ID",
        help="Registered Paytm merchant ID",
        required_if_provider='paytm')
    paytm_merchant_key = fields.Char(string="Merchant Key",
                                     groups='base.group_system',
                                     help=" Merchant key registered with Paytm")

    # def paytm_form_generate_values(self, values, base_url=None):
    #     paytm_values = dict(
    #         MID=self.paytm_merchant_id,
    #         ORDER_ID=str(values['reference']),
    #         CUST_ID=str(values.get('partner_id')),
    #         INDUSTRY_TYPE_ID='Retail',
    #         CHANNEL_ID='WEB',
    #         TXN_AMOUNT=str(values['amount']),
    #         WEBSITE='WEBSTAGING',
    #         EMAIL=str(values.get('partner_email')),
    #         MOBILE_NO=str(values.get('partner_phone')),
    #         CALL_BACK_URL=urls.url_join(base_url, '/payment/paytm/return/'),
    #     )
