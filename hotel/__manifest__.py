{
    'name': 'Hotel',
    'version': '16.0.1.0.0',
    'category': 'hotel/management',
    'sequence': '1',
    'installable': True,
    'application': True,
    'depends': ['base', 'mail', 'account_payment'],

    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/hotel_room_views.xml',
        'views/room_tags_views.xml',
        'views/guest_info_views.xml',
        'views/order_list_views.xml',
        'views/payment_guest_views.xml',
        'views/order_food_views.xml',
        'views/order_menu_views.xml',
        'views/food_category_views.xml',
        'views/hotel_products_views.xml',
        'wizard/wizard_report_views.xml',
        'views/hotel_property_views.xml',
        'views/snippet_template.xml',
        'views/partner_details.xml',
        'data/sequence.xml',
        'reports/hotel_report.xml',
        'reports/hotel_report_templates.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'hotel/static/src/js/action_manager.js',
        ],
        'web.assets_frontend': [
            'hotel/static/src/xml/dynamic_customers.xml',
            'hotel/static/src/js/snippet_dynamic.js',
        ],
    },
    'images': [
        'static/description/33777.png'
    ]

}
