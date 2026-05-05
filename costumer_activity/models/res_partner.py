from odoo import models, fields, api
from odoo.fields import Command


class ResPartner(models.Model):
    _inherit = "res.partner"

    activity_followup_count = fields.Integer(
        string="Nº de seguimientos",
        compute="_compute_activity_followup_count",
        store=False,
    )

    def _compute_activity_followup_count(self):
        for partner in self:
            partner.activity_followup_count = len(partner.activity_ids)