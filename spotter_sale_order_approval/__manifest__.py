# -*- coding: utf-8 -*-
{
    'name': ' Sale Order Approval',
    'version': '16.0.1.0.0',
    'category': 'Sales/approval',
    'description': "Module for adding sale order approval if total above 25k",
    'summary': 'sale & approvals',
    'sequence': 6,
    'depends': ['base', 'sale'],
    'license': 'LGPL-3',
    'data': [
        'views/sale_order_views.xml',

    ],
    'application': False,
    'installable': True,
    'auto_install': True,

}
