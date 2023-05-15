"""top 10 customers"""
from operator import itemgetter

from odoo import http
from odoo.http import request


class TopCustomers(http.Controller):
    """top 10 customers"""

    @http.route('/store/<model("res.partner"):product>', type='http',
                auth="user", website=True)
    def customer_details(self, product):
        """for showing customer details on website"""
        values = {
            'user': product,
        }
        return request.render('hotel.customer_details', values)

    @http.route(['/total_product_sold'], type="json", auth="public")
    def sold_total(self):
        """for getting top 10 customers based on  sales count"""

        web_sites = []
        customers = []
        counts = []

        def count_item(lst, value):
            """for getting the count """
            count = 0
            for ele in lst:
                if ele == value:
                    count = count + 1
            return count

        websites = request.env['website'].search([])
        for i in websites:
            web_sites.append(i.id)
        sale_order = request.env['sale.order'].sudo().search(
            [('state', 'in', ['sale']), ('website_id', 'in', web_sites)]
        )
        for item in sale_order:
            customers.append(item.partner_id)
        for rec in customers:
            counts.append({'customer': rec,
                           'id': rec.id,
                           'name': rec.name,
                           'email': rec.email,
                           'count': count_item(customers, rec),
                           'image': rec.image_1920
                           })
        sorted_list = sorted(counts, key=itemgetter('count'), reverse=True)
        customer_list = []

        for i in range(len(sorted_list)):
            if sorted_list[i] not in sorted_list[i + 1:]:
                customer_list.append(sorted_list[i])
        top_10_customers = customer_list[0:10]
        return top_10_customers
