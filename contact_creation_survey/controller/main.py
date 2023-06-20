# -*- coding: utf-8 -*-

"""contact creation from survey"""
from odoo.addons.survey.controllers.main import Survey
from odoo.http import request


class ContactCreationSurvey(Survey):

    def survey_submit(self, survey_token, answer_token, **post):
        """inherited controller from the survey for creating new contact
        after submission"""
        res = list(post.keys())[0]
        post.pop('csrf_token')
        post.pop('token')
        partner_fields = []
        question_id = request.env['survey.question'].browse(int(res))
        for item in question_id.survey_id.contact_relation_ids:
            data = {
                'question': item.questions_id.id,
                'field': item.res_partner_fields
            }
            partner_fields.append(data)
        for item in post:
            for each in partner_fields:
                if int(item) == each['question']:
                    field = each['field'].name
                    if field == 'name':
                        res_partner_vals = request.env['res.partner'].create([
                            {
                                'name': post[item]
                            },
                        ])
                    else:
                        res_partner_vals.write({field: post[item]})

        res = super(ContactCreationSurvey, self).survey_submit(
            survey_token=survey_token,
            answer_token=answer_token, **post)

        return res
