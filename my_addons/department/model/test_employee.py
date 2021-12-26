from odoo import api, models, fields


class TestEmployee(models.Model):
    _name = 'test.employee'

    name = fields.Char(string='姓名')
    department_id = fields.Many2one('test.department', string='部门')