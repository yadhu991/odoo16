{
    'name': 'Clear cart Website',
    'version': '16.0.1.0.0',
    'category': 'website_clear_cart/website',
    'sequence': 10,
    'depends': ['base', 'website', 'sale'],
    'license': 'LGPL-3',
    'data': [
        'views/clear_cart_view.xml',
        ],
    'assets': {
        'web.assets_frontend': [
            'website_clear_cart/static/src/js/clear_cart_button.js',
        ],
    },
    'installable': True,
    'auto_install': True,
}
