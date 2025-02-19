{
    'name': 'Purchase Margin Control',
    'version': '17.0.1.0.1',
    'category': 'Purchase',
    'summary': 'Add margin control to purchase order lines',
    'description': """
        Adds sales price and margin percentage fields to purchase order lines.
        Allows updating product sales price on purchase order confirmation.
    """,
    'depends': ['purchase'],
    'data': [
        'security/ir.model.access.csv',
        'views/purchase_views.xml',
        'wizard/apply_margin_wizard_views.xml',
    ],
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',
} 
