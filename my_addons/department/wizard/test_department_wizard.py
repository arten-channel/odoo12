from odoo import api, models, fields


class TestDepartmeentWizard(models.TransientModel):
    _name = 'test.department.wizard'

    line_ids = fields.One2many('test.department.wizard.line', 'wizard_id')

    @api.model
    def default_get(self, fields_list):
        res = super(TestDepartmeentWizard, self).default_get(fields_list)
        department_ids = self._context.get('department_ids', False)
        if department_ids:
            lines = self.create_line(department_ids)
            res['line_ids'] = lines
        return res

    def create_line(self, department_ids):
        department_objs = self.env['test.department'].browse(department_ids)
        line_obj = self.env['test.department.wizard.line']
        lines = []
        for dept in department_objs:
            val = {'department_id': dept.id, 'employee_ids': [(6, 0, dept.employee_ids.ids)]}
            lines.append(line_obj.create(val).id)
        return lines

    # ===========================================
    def update_department(self):
        for line in self.line_ids:
            if line.department_id.employee_ids != line.employee_ids:
                # line.department_id.employee_ids = line.employee_ids
                line.department_id.update({'employee_ids': [(6, 0, line.employee_ids.ids)]})


class TestDepartmeentWizardLine(models.TransientModel):
    _name = 'test.department.wizard.line'

    wizard_id = fields.Many2one('test.department.wizard')
    department_id = fields.Many2one('test.department', string='所选部门')
    employee_ids = fields.Many2many('test.employee', string='员工')
