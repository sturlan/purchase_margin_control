# Purchase Margin Control

This Odoo module extends the Purchase app to add margin control features to purchase orders.

## Features

- Adds `margin_percentage` and `sales_price` fields to purchase order lines, visible on the purchase order form view
- Provides an "Apply Margin to All Lines" wizard that allows setting a margin percentage to apply to all lines on a purchase order

## Installation

To install this module, add the `purchase_margin_control` directory to your Odoo addons path and install the module named "Purchase Margin Control" from the Apps menu.

## Usage

On a purchase order, you will see two new fields on each order line:

- Margin Percentage: The margin percentage to apply to the cost price to calculate the sales price
- Sales Price: The calculated sales price based on the cost price and margin percentage 

To bulk update the margin on all lines, click the "Apply Margin" button at the top of the purchase order form. This will open a wizard where you can enter a margin percentage to apply to all order lines.

## Configuration

This module does not require any additional configuration.

## Known Issues

There are no known issues at this time. Please report any bugs or suggestions via the issue tracker.

## License

This module is licensed under the terms of the [Odoo Proprietary License v1.0](https://www.odoo.com/documentation/user/14.0/legal/licenses/licenses.html#odoo-apps).
