# -*- coding: utf-8 -*-
# Part of Warlock Technologies Pvt. Ltd. See COPYRIGHT & LICENSE files for full copyright and licensing details.

{
    "name": "medquest website",
    "version": "14.0.0.2",
    "category": "website",
    "summary": "design static form template",
    "description": """
    design static form template.
    """,
    "author": "Warlock Technologies Pvt Ltd.",
    "website": "http://warlocktechnologies.com",
    "support": "support@warlocktechnologies.com",
    "depends": ["website"],
    "data": [
        'views/assets.xml',
        'views/medquest_form_template.xml',
        'views/about.xml',
        'views/website_menu.xml',
        'views/header_snippet.xml',
        'views/template.xml',
        'views/case_detail.xml',
        "views/medquest_home.xml",
        "views/service_details.xml",
        "views/service_general.xml",
        'views/header.xml',
        'views/overlaytemplate.xml',
        ],
    "images": ["static/src/img/service_form.PNG"],
    "application": True,
    "installable": True,
    "auto_install": False,
    "license": "OPL-1",
}
