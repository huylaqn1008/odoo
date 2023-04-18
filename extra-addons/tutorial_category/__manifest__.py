# -*- coding: utf-8 -*-
{
    "name": "Sport Category",
    "summary": """Tutorial, Extended""",
    "author": "HuyLT",
    "website": "https://github.com/huylaqn1008/odoo",
    "category": "Services/Sport",
    "version": "16.0.0.1",
    "depends": ["tutorial"],
    "data": [
        'security/ir.model.access.csv',
        'views/tag_view.xml',
        'views/game_view.xml',
        'views/menu_view.xml',
        'views/game_list_template.xml',
    ],
    "application": True,
}
