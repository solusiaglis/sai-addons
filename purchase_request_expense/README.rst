===========================
Purchase Request to Expense
===========================

This module extends the functionality to create expense from purchase requests

**Table of contents**

.. contents::
   :local:

Configuration
=============

To use this module:

1. Configure expandable products that can be used in both expenses and purchase requests
2. Set up approval workflows as needed for both processes
3. If using advance clearing features, ensure the hr_expense_advance_clearing module is installed

Note: When creating expenses from purchase requests, the system maintains the link between both documents for proper tracking and reconciliation.

Usage
=====

Expense from Purchase Requests

You can create expenses from existing purchase requests:

1. Create Purchase Request
   * Navigate to Purchase > Purchase Requests
   * Create a new purchase request
   * Add products and quantities as needed
   * Submit for approval

2. Create Expense
   * Select one or more purchase request lines (only lines with expandable products can be selected)
   * Click on "Create Expense" action
   * The system will generate an expense record with the selected lines
   * The expense will be linked to the original purchase request

Advanced Features

When hr_expense_advance_clearing module is installed:
   * You can create advance expense reports from purchase requests

   * This enables better tracking of advance payments and their clearance through the purchase request process



Authors
~~~~~~~

* PT Solusi Aglis Indonesia

Contributors
~~~~~~~~~~~~

* Panca Putra Pakpahan <ppakpahan@solusiaglis.co.id>

