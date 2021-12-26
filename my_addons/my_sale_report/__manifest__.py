# -*- coding: utf-8 -*-
{
    'name': "销售报表",

    'summary': """
        销售报表""",

    'description': """
        销售报表
    """,
    'depends': ['sale'],

    'author': "Leo Bian",
    'website': "http://learning.odoodev.cn/",

    # for the full list
    'version': '0.1',

    # always loaded
    'data': [
        'report/sale_report_view.xml',
    ],
    'installable': True,
}
