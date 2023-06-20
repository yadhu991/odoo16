# -*- coding: utf-8 -*-

from odoo import fields, models


class SurveySurvey(models.Model):
    _inherit = 'survey.survey'

    contact_relation_ids = fields.One2many('contact.relation', 'survey_id')

