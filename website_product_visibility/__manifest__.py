{
    'name': ' Website Product Visibility',
    'version': '16.0.1.0.0',
    'category': 'Website/Product visibility',
    'sequence': 10,
    'depends': ['base', 'contacts', 'website_sale_product_configurator'],
    'license': 'LGPL-3',
    'data': [
        'views/res_partner_views.xml',
        ],

    'installable': True,
    'auto_install': True,
}