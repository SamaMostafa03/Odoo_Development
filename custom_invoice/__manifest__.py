{
    'name':'Custom Invoice' ,
    'description': 'Custom Invoice' ,
    'category': 'Invoice',
    'version': '0.4',
    'author': 'odootec',
    "installable": True,
    'depends': ['odt_invoice_dossary','l10n_sa_invoice','web'],

    'assets': {
        'web.report_assets_common': [
            'custom_invoice/static/src/css/invoice_style.css',
        ]
    },

    'data': [
        'report/internal_template.xml',
        'report/accounting_report.xml',
        'report/accounting_template.xml',
    ]
}
