# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    employee_quantity = fields.Integer()
    employee_quantity_range_id = fields.Many2one(
        comodel_name="res.partner.employee_quantity_range",
        string="Rango de Empleados",
        help="Range of this partner depending on the employee quantity.",
    )
    web_seal = fields.Char(string='Sello Web')
    is_on_site = fields.Boolean(string='¿Presencial?', default=False, copy=False)
    is_advertisement_friedly = fields.Boolean(string='Acepta Publicidad', default=False, copy=False)

class ResPartnerEmployeeQuantityRange(models.Model):
    _name = "res.partner.employee_quantity_range"
    _description = "Partner employee quantity range"

    name = fields.Char(required=True, translate=True)
    sequence = fields.Integer(default=10)