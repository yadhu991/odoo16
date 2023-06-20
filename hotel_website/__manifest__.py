{
    'name': 'Hotel Website',
    'version': '16.0.1.0.0',
    'category': 'hotel/website',
    'sequence': 10,
    'depends': ['base', 'website'],
    'license': 'LGPL-3',
    'data': [
        'views/hotel_website_views.xml',
        'views/hotel_website_template.xml',
        'views/form_success.xml',

    ],
    'assets': {
        'web.assets_frontend': [
            'hotel_website/static/src/js/hotel_website_event.js',
        ],
    },
    'installable': True,
    'auto_install': True,
}
