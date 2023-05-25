from odoo.addons.website_sale.controllers import main
from odoo.http import request
from odoo import fields, http, SUPERUSER_ID, tools, _


class WebsiteSale(main.WebsiteSale):

    @http.route(['/shop/checkout'], type='http', auth="public", website=True, sitemap=False)
    def checkout(self, **post):
        res = super().checkout(**post)
        sale_order_id = request.session['sale_order_id']
        order = request.env['sale.order'].sudo().browse(sale_order_id)
        if order:
            cart_limit = request.env['ir.config_parameter'].sudo(
            ).get_param('labicicletta.website_sale_cart_limit')
            if cart_limit:
                if int(order.amount_total) <= int(cart_limit):
                    return request.redirect_query('/shop/cart', {'cart_limit_msg': 'exceeded', 'cart_limit': cart_limit})
        return res

    @ http.route(['/shop/address'], type='http', methods=['GET', 'POST'], auth="public", website=True, sitemap=False)
    def address(self, **kw):
        res = super().address(**kw)
        sale_order_id = request.session['sale_order_id']
        order = request.env['sale.order'].sudo().browse(sale_order_id)
        if order:
            cart_limit = request.env['ir.config_parameter'].sudo(
            ).get_param('labicicletta.website_sale_cart_limit')
            if cart_limit:
                if int(order.amount_total) <= int(cart_limit):
                    return request.redirect_query('/shop/cart', {'cart_limit_msg': 'exceeded', 'cart_limit': cart_limit})
        return res

    @ http.route(
        main.WebsiteSale._express_checkout_route, type='json', methods=['POST'], auth="public", website=True,
        sitemap=False
    )
    def process_express_checkout(self, billing_address, **kwargs):
        res = super().process_express_checkout(billing_address, **kwargs)
        sale_order_id = request.session['sale_order_id']
        order = request.env['sale.order'].sudo().browse(sale_order_id)
        if order:
            cart_limit = request.env['ir.config_parameter'].sudo(
            ).get_param('labicicletta.website_sale_cart_limit')
            if cart_limit:
                if int(order.amount_total) <= int(cart_limit):
                    return request.redirect_query('/shop/cart', {'cart_limit_msg': 'exceeded', 'cart_limit': cart_limit})
        return res

    @ http.route(['/shop/confirm_order'], type='http', auth="public", website=True, sitemap=False)
    def confirm_order(self, **post):
        res = super().confirm_order(**post)
        sale_order_id = request.session['sale_order_id']
        order = request.env['sale.order'].sudo().browse(sale_order_id)
        if order:
            cart_limit = request.env['ir.config_parameter'].sudo(
            ).get_param('labicicletta.website_sale_cart_limit')
            if cart_limit:
                if int(order.amount_total) <= int(cart_limit):
                    return request.redirect_query('/shop/cart', {'cart_limit_msg': 'exceeded', 'cart_limit': cart_limit})
        return res

    @ http.route('/shop/payment', type='http', auth='public', website=True, sitemap=False)
    def shop_payment(self, **post):
        res = super().shop_payment(**post)
        sale_order_id = request.session['sale_order_id']
        order = request.env['sale.order'].sudo().browse(sale_order_id)
        if order:
            cart_limit = request.env['ir.config_parameter'].sudo(
            ).get_param('labicicletta.website_sale_cart_limit')
            if cart_limit:
                if int(order.amount_total) <= int(cart_limit):
                    return request.redirect_query('/shop/cart', {'cart_limit_msg': 'exceeded', 'cart_limit': cart_limit})
        return res
