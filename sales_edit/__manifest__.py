{
    'name': 'Sales edit',
    'version': '16.0.1.0.0',
    'sequence': '10',
    'depends': ['base', 'sale_management'],
    'data': [
        'security/ir.model.access.csv',
        'views/sale_order_views.xml',
        'views/wizard_view.xml',
    ],
    'installable': True,
    'application': True,
}
