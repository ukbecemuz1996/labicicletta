{
    'name': 'Labicicletta',
    'version': '1.0',
    'category': 'Administration',
    'sequence': 501,
    'summary': 'Labicicletta Customizations',
    'description': """Labicicletta Customizations""",
    'depends': ['website','website_sale'],
    'data': [
        'views/res_config_settings_views.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            'labicicletta/static/src/js/labicicletta.js'
        ]
    },
    'application': True,
    'license': 'LGPL-3',
}
