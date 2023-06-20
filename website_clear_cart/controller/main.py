"""clear cart"""
from odoo import http
from odoo.http import request


class WebsiteClearCart(http.Controller):
    """clear cart"""

    @http.route(['/shop/clear_cart'], type='json', auth="public", website=True)
    def clear_cart(self):
        """clear cart website"""
        order = request.website.sale_get_order()
        if order:
            for line in order.website_order_line:
                line.unlink()
