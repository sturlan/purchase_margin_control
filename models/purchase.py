from odoo import models, fields, api
from odoo.exceptions import UserError

class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'

    margin_percentage = fields.Float(
        string='Margin %',
        digits='Product Price',
        help="Margin percentage based on purchase price"
    )
    sales_price = fields.Float(
        string='Sales Price',
        digits='Product Price',
        help="Product sales price"
    )

    @api.onchange('margin_percentage', 'price_unit')
    def _onchange_margin_percentage(self):
        if self.margin_percentage and self.price_unit:
            self.sales_price = self.price_unit * (1 + self.margin_percentage / 100)

    @api.onchange('sales_price', 'price_unit')
    def _onchange_sales_price(self):
        if self.sales_price and self.price_unit and self.price_unit != 0:
            self.margin_percentage = ((self.sales_price / self.price_unit) - 1) * 100

    def _prepare_margin_wizard_values(self):
        return {
            'margin_percentage': self.margin_percentage,
            'order_id': self.order_id.id,
        }

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    def button_confirm(self):
        res = super().button_confirm()
        for order in self:
            for line in order.order_line:
                if line.product_id and line.sales_price:
                    line.product_id.write({
                        'lst_price': line.sales_price
                    })
        return res

    def apply_margin_to_all_lines(self, margin_percentage):
        self.ensure_one()
        for line in self.order_line:
            line.margin_percentage = margin_percentage
            line._onchange_margin_percentage() 