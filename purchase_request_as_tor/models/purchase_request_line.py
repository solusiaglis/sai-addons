# Copyright 2025 PT Solusi Aglis Indonesia
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl-3.0)

from odoo import fields, models


class PurchaseRequestLine(models.Model):
    _inherit = "purchase.request.line"
    date_end = fields.Date(related="request_id.date_end", store=True)

    description = fields.Html(
        related="request_id.description",
        string="Additional Description",
        help="Detailed description of the ToR requirements",
        store=True,
        readonly=False,
    )
