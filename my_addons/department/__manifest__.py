# -*- coding: utf-8 -*-
{
    'name': "部门-员工",

    'summary': """
        部门-员工""",

    'description': """
        部门-员工
    """,

    'author': "Leo Bian",
    'website': "todo",

    # for the full list
    'version': '0.1',

    'depends': [],

    # always loaded
    'data': [
        'views/test_department_view.xml',
        'views/test_employee_view.xml',
        'security/ir.model.access.csv',
        'wizard/test_department_wizard_view.xml',
        'views/menu_views.xml',
    ],
    # 'qweb': ['static/src/xml/tongji_page.xml'],

    # 'installable': True,
    'application': True,
}
