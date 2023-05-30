# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, models, fields, _
from datetime import datetime
from odoo.exceptions import ValidationError

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    website_sale_whole_discount_code = fields.Char(
        string="Website Discount Code", readonly=False, config_parameter='labicicletta.website_sale_whole_discount_code')
    website_sale_cart_limit = fields.Float(
        string="Website Cart Minimum Total Amount", readonly=False, config_parameter='labicicletta.website_sale_cart_limit')
    website_start_working_hour = fields.Float(String='Start working hour',
                                              readonly=False, config_parameter='labicicletta.website_start_working_hour')
    website_end_working_hour = fields.Float(String='End working hour',
                                            readonly=False, config_parameter='labicicletta.website_end_working_hour')

    
    @api.constrains('website_start_working_hour', 'website_end_working_hour')
    def _check_start_end_working_hours(self):
        for record in self:
            if record.website_start_working_hour >= record.website_end_working_hour:
                raise ValidationError("Start working hour must be less than end working")
