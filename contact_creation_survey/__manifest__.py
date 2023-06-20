# -*- coding: utf-8 -*-
{
    'name': 'Contact Creation From Survey',
    'version': '16.0.1.0.0',
    'category': 'Marketing/contact creation',
    'description': "Module for creating contact from the surveys",
    'summary': 'Marketing & surveys',
    'sequence': 6,
    'depends': ['base', 'survey'],
    'license': 'LGPL-3',
    'data': [
        'security/ir.model.access.csv',
        'views/contact_relation_views.xml',
        'views/survey_survey_views.xml',
    ],
    'application': False,
    'installable': True,
    'auto_install': True,

}
