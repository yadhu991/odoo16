{
    'name': 'hotel website',
    'version': '16.0.1.0.0',
    'category': 'hotel/website',
    'sequence': 10,
    'depends': ['base','website'],
    'license': 'LGPL-3',
    'data': [
        'views/hotel_website_views.xml',
        'views/hotel_website_template.xml',
        # 'views/sale_order_views.xml',

    ],
    'installable': True,
    'application': True,
}