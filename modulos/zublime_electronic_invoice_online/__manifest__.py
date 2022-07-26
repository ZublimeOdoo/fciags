{
    'name': 'Facturación electrónica en linea (base)',
    'version': '14.0.1.0.0',
    'summary': 'Zublime Electronic Invoice Online',
    'category': 'Electronic Invoice Online',
    'author': 'Zublime',
    "website": "https://zublime.mx",
    'depends': [
        'base',
        'account',
        'base_setup',
        'sale',
    ],
    'data': [
        'data/security_electronic_invoice_online.xml',
        'views/res_config_settings_view.xml',
        'views/sale_order_view.xml',
        'report/report_sale_order.xml',
        'report/reporte_leyendas_sale.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}