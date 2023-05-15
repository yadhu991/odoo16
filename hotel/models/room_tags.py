from odoo import fields, models


class RoomTags(models.Model):
    _name = "room.tags"
    _description = "tags_of_room"

    name = fields.Char(string="facility", )
    color = fields.Integer(string="Color Picker")
