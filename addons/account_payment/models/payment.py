# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

import logging

from odoo import fields, models, _
from odoo.tools import float_compare

_logger = logging.getLogger(__name__)


class PaymentTransaction(models.Model):
    _inherit = 'payment.transaction'

    def render_invoice_button(self, invoice, submit_txt=None, render_values=None):
        values = {
            'partner_id': invoice.partner_id.id,
        }
        if render_values:
            values.update(render_values)
        return self.acquirer_id.with_context(submit_class='btn btn-primary', submit_txt=submit_txt or _('Pay Now')).sudo().render(
            self.reference,
            invoice.amount_residual_signed,
            invoice.currency_id.id,
            values=values,
        )
