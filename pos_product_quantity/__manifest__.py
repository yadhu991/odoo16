# -*- coding: utf-8 -*-
{
    'name': ' POS Product Quantity',
    'version': '16.0.1.0.0',
    'category': 'Sales/Pos',
    'description': "Module for showing product Quanity in selected location in POS",
    'summary': 'Pos & products',
    'sequence': 6,
    'depends': ['base', 'point_of_sale', 'stock'],
    'license': 'LGPL-3',
    'data': [
        'views/product_product_views.xml',

    ],
    'application': False,
    'installable': True,
    'auto_install': True,
    'assets': {
        'point_of_sale.assets': [
            'pos_product_quantity/static/src/xml/product_quantity_template.xml',

        ],

    }
}
