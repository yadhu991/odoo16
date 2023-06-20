# -*- coding: utf-8 -*-
{
    'name': ' POS Due Limit',
    'version': '16.0.1.0.0',
    'category': 'Sales/Pos',
    'description': "Module for adding Due limit in POS",
    'summary': 'Pos & products',
    'sequence': 10,
    'depends': ['base', 'point_of_sale','contacts' ],
    'license': 'LGPL-3',
    'data': [
        'views/res_partner_views.xml',
        'views/res_config_settings_views.xml',
        'views/pos_config_views.xml'
    ],
    'application': False,
    'installable': True,
    'auto_install': True,
    'assets': {
        'point_of_sale.assets': [
                'pos_due_limit/static/src/js/due_limit.js',
        ],

    }
}
