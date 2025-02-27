# Copyright 2025 PT Solusi Aglis Indonesia
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl-3.0).

{
    "name": "Purchase Request Validation Report",
    "version": "14.0.1.0.0",
    "author": "PT Solusi Aglis Indonesia",
    "category": "Purchase",
    "summary": "Add validation history to purchase request report",
    "depends": [
        "purchase_request_as_tor",
        "purchase_request_tier_validation",
    ],
    "website": "https://github.com/solusiaglis/sai-addons",
    "data": [
        "reports/purchase_request_report_templates.xml",
    ],
    "installable": True,
    "application": False,
    "auto_install": False,
    "license": "LGPL-3",
}
