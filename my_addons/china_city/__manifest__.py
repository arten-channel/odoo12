# -*- coding: utf-8 -*-
{
    'name': "城市信息",

    'summary': """
        城市信息""",

    'description': """
        城市信息
    """,
    'depends': [],

    'author': "Leo Bian",
    'website': "todo",

    # for the full list
    'version': '0.1',

    'depends': ['base', 'base_address_city'],

    # always loaded
    'data': [
        'views/res_city_view.xml',
        'views/menu_views.xml',
    ],
    # 'installable': True,
    'application': True,
}
