{
    'name': 'My Odoo FASTAPI Integration',
    'version': '1.0',
    'category': 'Tools',
    'summary': 'Integration with FASTAPI using XML-RPC',
    'description': """
        This module integrates Odoo with FASTAPI using the XML-RPC external API client.
    """,
    'author': 'Your Name',
    'depends': ['base'],
    'data': [
        'views/res_users_view.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
