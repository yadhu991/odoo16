"""website product visibility"""
from odoo.addons.website_sale.controllers.main import TableCompute
from odoo import http
from odoo.http import request
from odoo.addons.website_sale.controllers.main import WebsiteSale
from odoo.tools import lazy


class WebsiteProductVisibility(WebsiteSale):
    """product visibility based on selected product or category"""

    @http.route()
    def shop(self, page=0, products=None, category=None, search='',
             min_price=0.0, max_price=0.0, ppg=False, **post):
        """ website product visibility based on category & selected product"""

        res = super(WebsiteProductVisibility, self).shop(page=page,
                                                         category=category,
                                                         search=search,
                                                         min_price=min_price,
                                                         max_price=max_price,
                                                         products=products,
                                                         ppg=ppg,
                                                         **post)
        user = http.request.env.user
        price_list = res.qcontext.get('pricelist')
        if user.product_visibility_products:
            item = user.allowed_products_ids
            products_prices = lazy(
                lambda: item._get_sales_prices(price_list))
            get_product_prices = lambda product: lazy(
                lambda: products_prices[product.id])
            pager = request.website.pager(url='/shop', total=len(item.ids),
                                          page=page,
                                          step=20, scope=5)
            res.qcontext.update(
                {
                    'products': item,
                    'pager': pager,
                    'search_product': item,
                    'search_count': len(item),
                    'pricelist': price_list,
                    'products_prices': products_prices,
                    'get_product_prices': get_product_prices,
                    'bins': lazy(
                        lambda: TableCompute().process(item, 20, 4)),
                    'categories': None,
                    'attributes': None,

                })
        elif user.product_visibility_category:

            item = user.allowed_product_category_ids
            search_rec = request.env['product.template'].search(
                [('public_categ_ids', 'in', item.ids)])
            products_prices = lazy(
                lambda: search_rec._get_sales_prices(price_list))

            get_product_prices = lambda product: lazy(
                lambda: products_prices[product.id])
            pager = request.website.pager(url='/shop',
                                          total=len(search_rec.ids),
                                          page=page,
                                          step=20, scope=5)
            res.qcontext.update(
                {
                    'pricelist': price_list,
                    'products': search_rec,
                    'search_product': search_rec,
                    'pager': pager,
                    'products_prices': products_prices,
                    'get_product_prices': get_product_prices,
                    'bins': lazy(
                        lambda: TableCompute().process(search_rec, 20,
                                                       4)),
                    'categories': None,
                    'attributes': None,

                })
        else:
            item = False
        return res
