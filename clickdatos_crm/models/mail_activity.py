# Copyright 2018-22 ForgeFlow <http://www.forgeflow.com>
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).
from odoo import api, fields, models
from odoo.osv import expression

class MailActivity(models.Model):

    _inherit = "mail.activity"

    def activity_format(self):
        return super(MailActivity, self.filtered_domain([('active', '=', True)])).activity_format()
    
    def action_res_partner_activity(self):
        return {
            'name': 'Actividades',
            'type': 'ir.actions.act_window',
            'res_model': 'mail.activity',
            'res_id': self.id,
            'view_mode': 'form',
            'domain': [('res_model', '=', 'res.partner')],
            'context': {'default_res_model': 'res.partner', 'default_res_id': self.res_id},
            'target': 'new',
        }