from odoo import api, models, fields


class TestDepartment(models.Model):
    _name = 'test.department'

    name = fields.Char(string='部门名称')
    employee_ids = fields.One2many('test.employee', 'department_id', string='员工')