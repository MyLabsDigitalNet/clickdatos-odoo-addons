# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

{
    "name": "ClickDatos CRM",
    "summary": "Partner extra fields and CRM implementation",
    "version": "16.0.1.0.0",
    "category": "Customer Relationship Management",
    "author": "Qsimov Quantum Computing",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": ["contacts", "crm", "mail_activity_board", "mail_activity_done"],
    "data": [
        "security/ir.model.access.csv",
        "data/res_partner_data.xml",
        "views/res_partner_employee_quantity_range_views.xml",
        "views/res_partner_views.xml",
        "views/crm_lead_views.xml",
    ],
    'assets': {
        'web.assets_backend': [
            'clickdatos_crm/static/src/scss/activity.scss',
        ],
    },
}