# -*- coding: utf-8 -*-
{
    'name': "疫情数据统计",

    'summary': """
        疫情数据统计""",

    'description': """
        疫情数据统计
    """,

    'author': "Leo Bian",
    'website': "todo",

    # for the full list
    'version': '0.1',

    'depends': ['base', 'china_city'],

    # always loaded
    'data': [
        'views/history_data_days_view.xml',
        'views/tongji_to_province_view.xml',
        'views/template.xml',
        'views/epidemic_tongji_page_view.xml',
        'views/menu_views.xml',
        'security/ir.model.access.csv',
    ],
    'qweb': ['static/src/xml/tongji_page.xml'],

    # 'installable': True,
    'application': True,
}
