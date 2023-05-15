{
    'name': 'Purchase edit',
    'version': '16.0.1.0.0',
    'category': 'purchase_edit/purchase',
    'sequence': '10',
    'installable': True,
    'application': True,
    'depends': ['base', 'purchase'],

    'data': [
        'views/purchase_order_edit_views.xml',
        'views/purchase_order_line_views.xml',
    ],

}
