# -*- coding: utf-8 -*-
{
    'name': "Real Estate",

    'summary': "This module is used to manage real estate properties",

    'description': """
        This module is used to manage real estate properties. It includes features like:
        - Property management
        - Property listing
        - Property booking
        - Property valuation
    """,

    'author': "Dine Company",
    'website': "https://www.dinecompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        # 'views/templates.xml',
        'views/estate_property_views.xml',
    ],
    # only loaded in demonstration mode
    # 'demo': [
    #     'demo/demo.xml',
    # ],

    'application': True,
}

