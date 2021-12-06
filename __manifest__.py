{
    'name': "Product Tags",
    'author': 'Bharat Yadav',
    'version': '1.0.4',
    'summary': 'You can create product tags and you can update mass product tags',
    'depends':['product'],
    'data': [
        'security/ir.model.access.csv',
        'wizard/update_mass_tags_wizard_views.xml',
        'views/product_tags.xml',
        'views/product_template_inherited.xml'
    ]

}