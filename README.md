# Bosnia - Payment Reference Sync

Odoo module that syncs the `payment_reference` and `ref` fields to the payable/receivable line name when updated.

## Problem Solved

When creating a payment from a vendor bill, the `communication` field in the payment wizard shows the payable line's `name` field. If the invoice's `payment_reference` or `ref` was updated after the invoice was created, the payable line's `name` would still show the old value.

This module ensures that when `payment_reference` or `ref` is updated on an invoice, the payable/receivable line's `name` is also updated to match.

## Installation

Install this module in Odoo 16.0.

## Author

- Ernad Husremovic, bring.out doo Sarajevo
- https://www.bring.out.ba
