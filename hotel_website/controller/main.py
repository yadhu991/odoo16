from odoo import http
from odoo.http import request


class HotelWebsiteForm(http.Controller):
    @http.route(['/appointment'], type='http', auth="user", website=True)
    def appointment(self):
        partners = request.env['res.partner'].sudo().search([])
        values = {}
        values.update({
            'partners': partners
        })
        return request.render("hotel_website.online_appointment_form", values)
