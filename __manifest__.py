{
    'name': 'Odoo REST OpenAPI',
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
        'data/openapi_data.xml',
        'views/openapi_view.xml'
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
