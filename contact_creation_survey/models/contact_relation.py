# -*- coding: utf-8 -*-

from odoo import fields, models


class ContactRelation(models.Model):
    _name = "contact.relation"
    _description = "Contact & Questions"

    questions_id = fields.Many2one('survey.question', "Question")
    res_partner_fields = fields.Many2one('ir.model.fields', "Field",
                                         domain="[('model_id', '=', 85),"
                                                "('ttype','=','char'),"
                                                "('store','=',True),"
                                                "('readonly','=',False)]")
    survey_id = fields.Many2one('survey.survey')
