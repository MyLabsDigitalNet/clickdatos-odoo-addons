# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import fields, models, Command


class CrmLead(models.Model):
    _inherit = "crm.lead"

    employee_quantity_range_id = fields.Many2one(
        comodel_name="res.partner.employee_quantity_range",
        string="Rango de Empleados",
        help="Range of this partner depending on the employee quantity.",
    )
    web_seal = fields.Char(string='Sello Web')
    is_on_site = fields.Boolean(string='¿Presencial?', default=False, copy=False)
    advertisement = fields.Selection([("si", "Sí"), 
                                      ("no", "No"),
                                      ("falta_contrato", "Falta contrato")], string='Acepta Publicidad', default=False, copy=False)

    def _prepare_customer_values(self, partner_name, is_company=False, parent_id=False):
        res = super(CrmLead, self)._prepare_customer_values(partner_name, is_company=is_company, parent_id=parent_id)
        if is_company:
            res.update({
                'employee_quantity_range_id': self.employee_quantity_range_id.id,
            })
        res.update({'web_seal': self.web_seal,
                    'is_on_site': self.is_on_site,
                    'advertisement': self.advertisement, 
                    'source_id': self.source_id.id,})
        return res