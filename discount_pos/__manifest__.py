# -*- coding: utf-8 -*-
{
    'name': ' POS Discount',
    'version': '16.0.1.0.0',
    'category': 'Sales/Pos',
    'description': "Module for adding Discount in POS",
    'summary': 'Pos & products',
    'sequence': 6,
    'depends': ['base', 'point_of_sale'],
    'license': 'LGPL-3',
    'data': [

        'views/pos_config_views.xml'
    ],
    'application': False,
    'installable': True,
    'auto_install': True,
    'assets': {
        'point_of_sale.assets': [
            'discount_pos/static/src/xml/button_template.xml',
            'discount_pos/static/src/xml/order_line_template.xml',
            'discount_pos/static/src/js/discount_pos.js',
            'discount_pos/static/src/js/discount_amount.js'
        ],

    }
}
