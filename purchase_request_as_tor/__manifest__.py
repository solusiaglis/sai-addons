# Copyright 2025 PT Solusi Aglis Indonesia
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl-3.0).

{
    "name": "Purchase Request as Term of Reference",
    "author": "PT Solusi Aglis Indonesia",
    "version": "14.0.0.1.0",
    "summary": "This module to inherit the purchase request as Term of Reference ",
    "website": "https://github.com/solusiaglis/sai-addons",
    "category": "Purchase Management",
    "depends": ["purchase_request"],
    "data": [
        "reports/report_purchase_request.xml",
        "views/purchase_request_report.xml",
        "views/purchase_request_view.xml",
    ],
    "license": "LGPL-3",
    "installable": True,
    "application": False,
}
