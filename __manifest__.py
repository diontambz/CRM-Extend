{
    'name': 'CRM Extension',
    'version': '13.0.1.0.0',
    'category': 'Sales/CRM',
    'summary': 'Extend CRM functionality',
    'description': """
    """,
    'author': 'Dion Tambunan',
    'depends': ['crm'],
    'data': [
        'security/ir.model.access.csv',
        'views/crm_lead_views.xml',
        'views/segment_product_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}