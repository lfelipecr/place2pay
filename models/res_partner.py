# -*- coding: utf-8 -*-
from odoo import api, fields, models, _

class res_partner(models.Model):
    _inherit = 'res.partner'

    p2p_document_type = fields.Many2one (comodel_name="l10n_latam.document.type", string="Document type",  help="")

    zip = fields.Char('Zip', required=False)
    city = fields.Char('City', required=False)