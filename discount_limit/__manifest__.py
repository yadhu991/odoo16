{
    'name': 'Discount limit',
    'version': '16.0.1.0.0',
    'category': 'discount_limit/sales',
    'sequence': 10,
    'depends': ['base', 'sale_management'],
    'license': 'LGPL-3',
    'data': [
        'views/discount_limit_view.xml',
        'views/res_partner_view.xml',
        'views/sale_order_views.xml',

    ],
    'installable': True,
    'application': True,
}
