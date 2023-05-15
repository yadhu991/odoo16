from odoo import fields, models


class AttendanceList(models.Model):
    _name = "attendance.list"
    _description = "days wise attendance"
    _rec_name = 'employee_id'

    employee_id = fields.Many2one('hr.employee', string="Employee")
    department_id = fields.Many2one('hr.department', string="Department")
    date_list = fields.Date(string="Date")
    phone = fields.Char(related="employee_id.work_phone")
    mail = fields.Char(related="employee_id.work_email")
    image = fields.Image(related="employee_id.image_128", string="")
    manager_id = fields.Many2one(related="employee_id.parent_id", string="Manager")
    work_address_id = fields.Many2one(related="employee_id.address_id")
    work_location_id = fields.Many2one(related="employee_id.work_location_id")

    def get_details(self):
        today = fields.Datetime.now()
        current_date = today.date()
        search = self.env['hr.employee'].search([])
        for employee in search:
            if employee.hr_presence_state != 'present':
                self.create({'employee_id': employee.id,
                             'date_list': current_date,
                             'department_id': employee.department_id.id
                             })

