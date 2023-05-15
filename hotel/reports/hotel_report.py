from odoo import models, api


class HotelReport(models.AbstractModel):
    _name = 'report.hotel.report_hotel_guest'

    @api.model
    def _get_report_values(self, docids, data=None):
        print(data)
        return {
            'doc_ids': docids,
            'doc_model': 'hotel.property',
            'data': data,
        }
