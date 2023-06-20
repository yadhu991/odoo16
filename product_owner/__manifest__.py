# -*- coding: utf-8 -*-
{
    'name': ' POS Product Owner',
    'version': '16.0.1.0.0',
    'category': 'Sales/Pos',
    'description': "Module for adding product owner in POS",
    'summary': 'Pos & products',
    'sequence': 10,
    'depends': ['base', 'point_of_sale', ],
    'license': 'LGPL-3',
    'data': [
        'views/product_product_views.xml',
    ],
    'application': False,
    'installable': True,
    'auto_install': True,
    'assets': {
        'point_of_sale.assets': [
            'product_owner/static/src/xml/product_owner_receipt.xml',
            'product_owner/static/src/xml/product_owner_pos.xml',
            'product_owner/static/src/js/pos_receipt.js',

        ],

    }
}
