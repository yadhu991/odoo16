# -*- coding: utf-8 -*-
{
    'name': 'Employee Contract expiry Mail',
    'version': '16.0.1.0.0',
    'category': 'Human Resources/contract expiry',
    'description': "Module for sending contract expiry mail to HR before the contract is going to be expired.",
    'summary': 'Human Resources & employees',
    'sequence': 5,
    'depends': ['base', 'hr', 'hr_contract'],
    'license': 'LGPL-3',
    'data': [
        'data/email_template.xml',
        'views/res_config_settings_views.xml',
        'data/scheduled_action.xml'

    ],
    'application': False,
    'installable': True,
    'auto_install': True,

}
