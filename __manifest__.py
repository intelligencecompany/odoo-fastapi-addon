{
    'name': 'Odoo REST OpenAPI',
    'version': '1.01',
    'category': 'Technical',
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
        'security/ir.model.access.csv',
        'security/openapi_record_rules.xml',
        'views/openapi_view.xml'
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
