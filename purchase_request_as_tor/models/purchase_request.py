# Copyright 2025 PT Solusi Aglis Indonesia
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl-3.0)

from odoo import fields, models


class PurchaseRequest(models.Model):
    _inherit = "purchase.request"

    date_end = fields.Date(
        string="End date",
        help="The Date expected end date for this TOR",
        tracking=True,
        copy=False,
    )

    description = fields.Html(
        string="Description",
        help="Detailed description of the ToR requirements",  # Added help text
        tracking=True,  # Added tracking for description changes
    )
