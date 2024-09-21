{
    'name':'Hospital Management' ,
    'description': 'hospital management system' ,
    'category': 'Services',
    'version': '0.1',
    'author': 'Sama Mostafa',
    "installable": True,
    'auto_install': True,
    'license': "GPL-3",
    'sequence': -100,
    'application': True,
    'depends': ['mail' , 'sale' , 'product' , 'base' , 'web'],


    'data': [
        'security/ir.model.access.csv',
        'data/templ_mail.xml',
        'views/menu.xml',
        'views/patient.xml',
        'views/order.xml',
        'views/appointment.xml',
        'views/crm.xml',
        'report/appointment_report.xml',
        'report/appointment_template.xml',
    ],

}
