from odoo import api, models


class AccountMove(models.Model):
    _inherit = "account.move"

    def write(self, vals):
        """Sync payable/receivable line name when payment_reference or ref is updated."""
        result = super().write(vals)

        # If payment_reference or ref was updated, sync to payable/receivable line name
        if 'payment_reference' in vals or 'ref' in vals:
            for move in self:
                if not move.is_invoice(include_receipts=True):
                    continue

                # Determine the new name value (payment_reference takes priority over ref)
                new_name = move.payment_reference or move.ref or False

                # Find payable/receivable lines (display_type == 'payment_term')
                term_lines = move.line_ids.filtered(
                    lambda l: l.display_type == 'payment_term'
                )

                # Update the name on all term lines
                if term_lines and new_name:
                    term_lines.with_context(check_move_validity=False).write({
                        'name': new_name
                    })

        return result
