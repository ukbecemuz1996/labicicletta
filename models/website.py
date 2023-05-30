
from odoo import api, fields, models, tools, SUPERUSER_ID, _
from odoo.http import request
from datetime import datetime

class Website(models.Model):
    _inherit = 'website'

    shop_is_opened = fields.Boolean(
        String='Shop Is Open', compute='_compute_shop_is_opened')

    def sale_get_order(self, force_create=False, update_pricelist=False):
        sale_order_sudo = super().sale_get_order(force_create, update_pricelist)
        if sale_order_sudo:
            discount_code = self.env['ir.config_parameter'].sudo().get_param(
                'labicicletta.website_sale_whole_discount_code')
            if discount_code:
                sale_order_sudo._try_apply_code(discount_code)
        return sale_order_sudo

    def get_cart_sale_order_id(self):
        return super().sale_get_order()

    def _compute_shop_is_opened(self):
        for record in self:
            website_start_working_hour = request.env['ir.config_parameter'].sudo(
            ).get_param('labicicletta.website_start_working_hour')

            website_end_working_hour = request.env['ir.config_parameter'].sudo(
            ).get_param('labicicletta.website_end_working_hour')

            now = datetime.now().time()
            current_time = now.hour+now.minute/60.0

            current_time_is_between = float(current_time) >= float(
                website_start_working_hour) and float(current_time) <= float(website_end_working_hour)
            record.shop_is_opened = current_time_is_between
