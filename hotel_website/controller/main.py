"""hotel booking from website"""
from odoo import http
from odoo.http import request


class HotelWebsiteForm(http.Controller):
    """website hotel"""

    @http.route(['/appointment'], type='http', auth="user", website=True)
    def appointment(self):
        """hotel booking form"""
        partners = request.env['res.partner'].sudo().search([])
        return request.render("hotel_website.online_appointment_form", {
            'partners': partners})

    @http.route(['/partner_details'], type="json", auth="public")
    def partner_details(self, **post):
        """to get the partner details"""
        customer = int(post['id'])
        search_partner = request.env['res.partner'].browse(customer)
        data = {
            'email': search_partner.email,
            'phone': search_partner.phone,
            'name': search_partner.name,
            'id': search_partner.id
        }
        return data

    @http.route(['/appointment/submit/'], type='http', auth="public",
                website=True)
    def customer_form_submit(self, **post):
        """action for the submit button"""
        if post['cust_id']:
            customer_id = int(post['cust_id'])
        else:
            customer_id = request.env['res.partner'].sudo().create(
                {'name': post['partner_id'],
                 'email': post['email'],
                 'phone': post['phone']
                 }).id

        booking = request.env['hotel.property'].sudo().create({
            'partner_id': customer_id, 'email': post['email'],
            'phone': post['phone'],
            'number_of_guests': post['number_of_guests'],
            'expected_days': post['expected_days'], 'type': post['type'],
            'created_date': post['created_date']}
        )
        return request.render(
            "hotel_website.tmp_customer_form_success",
            {'booking_id': booking.reference_no,
             'booking_date': booking.created_date})
