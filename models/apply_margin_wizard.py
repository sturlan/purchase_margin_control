from odoo import models, fields

class ApplyMarginWizard(models.TransientModel):
    _name = 'apply.margin.wizard'
    _description = 'Apply Margin to All Lines'

    margin_percentage = fields.Float(string='Margin %', digits='Product Price')
    order_id = fields.Many2one('purchase.order', string='Purchase Order')

    def apply_margin(self):
        self.ensure_one()
        if self.order_id:
            self.order_id.apply_margin_to_all_lines(self.margin_percentage)
        return {'type': 'ir.actions.act_window_close'} 