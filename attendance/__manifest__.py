{
    'name': 'Day wise attendance',
    'version': '16.0.1.0.0',
    'category': 'attendance/employee',
    'sequence': 10,
    'depends': ['base', 'hr'],
    'license': 'LGPL-3',
    'data': [
             'security/ir.model.access.csv',
             'views/attendance_list.xml',

             ],
    'installable': True,
    'application': True,
}
