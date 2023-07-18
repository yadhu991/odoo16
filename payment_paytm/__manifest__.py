# -*- coding: utf-8 -*-
{
    'name': 'Payment Provider : Paytm',
    'version': '16.0.1.0.0',
    'category': 'Payment provider/Paytm',
    'description': "Module for integrating Paytm provider t oodoo payments.",
    'summary': 'Payments',
    'sequence': 5,
    'depends': ['base', 'payment'],
    'license': 'LGPL-3',
    'data': [
        'data/paytm_payment_record.xml',
        'views/payment_provider_views.xml',
    ],
    'images': [
        'static/description/icon.png'
    ],
    'application': False,
    'installable': True,
    'auto_install': True,

}
