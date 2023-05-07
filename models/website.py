
from odoo import api, fields, models, tools, SUPERUSER_ID, _

class Website(models.Model):
    _inherit = 'website'

    def sale_get_order(self, force_create=False, update_pricelist=False):
        sale_order_sudo = super().sale_get_order(force_create,update_pricelist)
        if sale_order_sudo:
            discount_code = self.env['ir.config_parameter'].sudo().get_param('labicicletta.website_sale_whole_discount_code')
            if discount_code:
                sale_order_sudo._try_apply_code(discount_code)
        return sale_order_sudo