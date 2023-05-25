# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, models, fields, _


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    website_sale_whole_discount_code = fields.Char(string="Website Discount Code", readonly=False,config_parameter='labicicletta.website_sale_whole_discount_code')
    website_sale_cart_limit = fields.Float(string="Website Cart Minimum Total Amount", readonly=False,config_parameter='labicicletta.website_sale_cart_limit')