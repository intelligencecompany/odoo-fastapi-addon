{
    'name': 'Odoo REST API',
    'version': '1.0',
    'category': 'Tools',
    'summary': 'Converting XML-RPC to a OpenAPI REST API',
    'description': """
        This module integrates Odoo with FASTAPI using the XML-RPC external API client.
    """,
    'website': 'https://intelligencecompany.net',
    'author': 'Gijs Segerink',
    "license": "LGPL-3",
    'depends': ['base'],
    'external_dependencies': {
        'python' : [
            'fastapi',
            'requests',
            'uvicorn'
        ],
    },
    'data': [
        'views/openapi_view.xml',
        'data/openapi_data.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
