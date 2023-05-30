from odoo.addons.website_sale.controllers import main
from odoo.http import request
from odoo import fields, http, SUPERUSER_ID, tools, _
from datetime import datetime
from odoo.addons.website.models.ir_http import sitemap_qs2dom
from odoo.addons.http_routing.models.ir_http import slug


class WebsiteSale(main.WebsiteSale):
    def sitemap_shop(env, rule, qs):
        if not qs or qs.lower() in '/shop':
            yield {'loc': '/shop'}

        Category = env['product.public.category']
        dom = sitemap_qs2dom(qs, '/shop/category', Category._rec_name)
        dom += env['website'].get_current_website().website_domain()
        for cat in Category.search(dom):
            loc = '/shop/category/%s' % slug(cat)
            if not qs or qs.lower() in loc:
                yield {'loc': loc}

    @http.route(['/shop/checkout'], type='http', auth="public", website=True, sitemap=False)
    def checkout(self, **post):
        res = super().checkout(**post)

        website_start_working_hour = request.env['ir.config_parameter'].sudo(
        ).get_param('labicicletta.website_start_working_hour')

        website_end_working_hour = request.env['ir.config_parameter'].sudo(
        ).get_param('labicicletta.website_end_working_hour')

        now = datetime.now().time()
        current_time = now.hour+now.minute/60.0

        current_time_is_between = float(current_time) >= float(
            website_start_working_hour) and float(current_time) <= float(website_end_working_hour)

        if not current_time_is_between:
            return request.redirect('/?working_hours=outside')

        sale_order_id = request.session['sale_order_id']
        order = request.env['sale.order'].sudo().browse(sale_order_id)
        if order:
            cart_limit = request.env['ir.config_parameter'].sudo(
            ).get_param('labicicletta.website_sale_cart_limit')
            if cart_limit:
                if float(order.amount_total) <= float(cart_limit):
                    return request.redirect_query('/shop/cart', {'cart_limit_msg': 'exceeded', 'cart_limit': cart_limit})
        return res

    @ http.route(['/shop/address'], type='http', methods=['GET', 'POST'], auth="public", website=True, sitemap=False)
    def address(self, **kw):
        res = super().address(**kw)

        website_start_working_hour = request.env['ir.config_parameter'].sudo(
        ).get_param('labicicletta.website_start_working_hour')

        website_end_working_hour = request.env['ir.config_parameter'].sudo(
        ).get_param('labicicletta.website_end_working_hour')

        now = datetime.now().time()
        current_time = now.hour+now.minute/60.0

        current_time_is_between = float(current_time) >= float(
            website_start_working_hour) and float(current_time) <= float(website_end_working_hour)

        if not current_time_is_between:
            return request.redirect('/?working_hours=outside')

        sale_order_id = request.session['sale_order_id']
        order = request.env['sale.order'].sudo().browse(sale_order_id)
        if order:
            cart_limit = request.env['ir.config_parameter'].sudo(
            ).get_param('labicicletta.website_sale_cart_limit')
            if cart_limit:
                if float(order.amount_total) <= float(cart_limit):
                    return request.redirect_query('/shop/cart', {'cart_limit_msg': 'exceeded', 'cart_limit': cart_limit})
        return res

    @ http.route(
        main.WebsiteSale._express_checkout_route, type='json', methods=['POST'], auth="public", website=True,
        sitemap=False
    )
    def process_express_checkout(self, billing_address, **kwargs):
        res = super().process_express_checkout(billing_address, **kwargs)

        website_start_working_hour = request.env['ir.config_parameter'].sudo(
        ).get_param('labicicletta.website_start_working_hour')

        website_end_working_hour = request.env['ir.config_parameter'].sudo(
        ).get_param('labicicletta.website_end_working_hour')

        now = datetime.now().time()
        current_time = now.hour+now.minute/60.0

        current_time_is_between = float(current_time) >= float(
            website_start_working_hour) and float(current_time) <= float(website_end_working_hour)

        if not current_time_is_between:
            return request.redirect('/?working_hours=outside')

        sale_order_id = request.session['sale_order_id']
        order = request.env['sale.order'].sudo().browse(sale_order_id)
        if order:
            cart_limit = request.env['ir.config_parameter'].sudo(
            ).get_param('labicicletta.website_sale_cart_limit')
            if cart_limit:
                if float(order.amount_total) <= float(cart_limit):
                    return request.redirect_query('/shop/cart', {'cart_limit_msg': 'exceeded', 'cart_limit': cart_limit})
        return res

    @ http.route(['/shop/confirm_order'], type='http', auth="public", website=True, sitemap=False)
    def confirm_order(self, **post):
        res = super().confirm_order(**post)

        website_start_working_hour = request.env['ir.config_parameter'].sudo(
        ).get_param('labicicletta.website_start_working_hour')

        website_end_working_hour = request.env['ir.config_parameter'].sudo(
        ).get_param('labicicletta.website_end_working_hour')

        now = datetime.now().time()
        current_time = now.hour+now.minute/60.0

        current_time_is_between = float(current_time) >= float(
            website_start_working_hour) and float(current_time) <= float(website_end_working_hour)

        if not current_time_is_between:
            return request.redirect('/?working_hours=outside')

        sale_order_id = request.session['sale_order_id']
        order = request.env['sale.order'].sudo().browse(sale_order_id)
        if order:
            cart_limit = request.env['ir.config_parameter'].sudo(
            ).get_param('labicicletta.website_sale_cart_limit')
            if cart_limit:
                if float(order.amount_total) <= float(cart_limit):
                    return request.redirect_query('/shop/cart', {'cart_limit_msg': 'exceeded', 'cart_limit': cart_limit})
        return res

    @ http.route('/shop/payment', type='http', auth='public', website=True, sitemap=False)
    def shop_payment(self, **post):
        res = super().shop_payment(**post)

        website_start_working_hour = request.env['ir.config_parameter'].sudo(
        ).get_param('labicicletta.website_start_working_hour')

        website_end_working_hour = request.env['ir.config_parameter'].sudo(
        ).get_param('labicicletta.website_end_working_hour')

        now = datetime.now().time()
        current_time = now.hour+now.minute/60.0

        current_time_is_between = float(current_time) >= float(
            website_start_working_hour) and float(current_time) <= float(website_end_working_hour)

        if not current_time_is_between:
            return request.redirect('/?working_hours=outside')

        sale_order_id = request.session['sale_order_id']
        order = request.env['sale.order'].sudo().browse(sale_order_id)
        if order:
            cart_limit = request.env['ir.config_parameter'].sudo(
            ).get_param('labicicletta.website_sale_cart_limit')
            if cart_limit:
                if float(order.amount_total) <= float(cart_limit):
                    return request.redirect_query('/shop/cart', {'cart_limit_msg': 'exceeded', 'cart_limit': cart_limit})
        return res

    @http.route(['/shop/cart'], type='http', auth="public", website=True, sitemap=False)
    def cart(self, access_token=None, revive='', **post):
        res = super().cart(**post)

        website_start_working_hour = request.env['ir.config_parameter'].sudo(
        ).get_param('labicicletta.website_start_working_hour')

        website_end_working_hour = request.env['ir.config_parameter'].sudo(
        ).get_param('labicicletta.website_end_working_hour')

        now = datetime.now().time()
        current_time = now.hour+now.minute/60.0

        current_time_is_between = float(current_time) >= float(
            website_start_working_hour) and float(current_time) <= float(website_end_working_hour)

        if not current_time_is_between:
            return request.redirect('/?working_hours=outside')

        return res

    @http.route([
        '/shop',
        '/shop/page/<int:page>',
        '/shop/category/<model("product.public.category"):category>',
        '/shop/category/<model("product.public.category"):category>/page/<int:page>',
    ], type='http', auth="public", website=True, sitemap=sitemap_shop)
    def shop(self, page=0, category=None, search='', min_price=0.0, max_price=0.0, ppg=False, **post):
        res = super().shop(page, category, search, min_price, max_price, ppg, **post)
        website_start_working_hour = request.env['ir.config_parameter'].sudo(
        ).get_param('labicicletta.website_start_working_hour')

        website_end_working_hour = request.env['ir.config_parameter'].sudo(
        ).get_param('labicicletta.website_end_working_hour')

        now = datetime.now().time()
        current_time = now.hour+now.minute/60.0

        current_time_is_between = float(current_time) >= float(
            website_start_working_hour) and float(current_time) <= float(website_end_working_hour)

        if not current_time_is_between:
            return request.redirect('/?working_hours=outside')

        return res
