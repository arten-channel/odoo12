from odoo import api, fields, models


class EpidemicRecord(models.Model):
    _name = 'epidemic.record'

    def _default_create_user_id(self):
        return self.env.uid

    # 姓名、日期、省、市、区/县、性别、年龄、就业状态、具体地址、感染方式、境内/境外感染
    name = fields.Char(string='姓名')
    date = fields.Date(string='确诊日期')   # xxxx年xx月xx日
    state = fields.Char(string='省')
    city = fields.Char(string='市')
    county = fields.Char(string='区/县')
    street = fields.Char(string='具体地址')
    ill_type = fields.Char(string='感染方式')
    within_or_abroad = fields.Selection([('within', '境内'), ('abroad', '境外')], default='within', string='境内/境外感染')
    is_ill = fields.Boolean(string='是否确诊', default=False)
    begin_lsolation_date = fields.Date(string='起始隔离日期')
    lsolation_mode = fields.Selection([('home', '居家隔离'), ('focus', '集中隔离')], string='隔离方式')
    create_user_id = fields.Many2one('res.users', string='填报人', default=_default_create_user_id)
    note = fields.Text(string='说明')
    test_float = fields.Float(string='测试浮点字段')
    test_int = fields.Integer(string='测试整型字段')

    fuzhu_create_user_ids = fields.Many2many('res.users', 'epidemie_record_res_users_rel', column1='record_id', column2='user_id', string='辅助填报人')

    active = fields.Boolean(default=True)

    @api.model
    def create(self, vals_list):
        res = super(EpidemicRecord, self).create(vals_list)
        return res

    @api.multi
    def write(self, vals):
        old_test_int = self.test_int
        res = super(EpidemicRecord, self).write(vals)
        new_test_int = self.test_int
        return res

    @api.multi
    def unlink(self):
        # 伪删除
        for obj in self:
            obj.active = False

    @api.onchange('state', 'city', 'name')
    def onchange_note(self):
        self.note = '{}省{}市，隔离人员姓名{}'.format(self.state, self.city, self.name)

    def myunlink(self):
        self.active = False

    def mysearch(self):
        # domain = [('is_ill', '=', True)]
        # objs = self.search(domain)
        # objs2 = self.browse([14, 15])
        # print(objs, objs2)
        users_objs = self.env['res.users'].sudo().browse([2,2])
        print('users_objs', users_objs)

    def create_or_write(self):
        """演示 orm操作 write和create"""
        # res = self.env['res.users'].create({
        #     'name': '测试账户1',
        #     'email': 'ceshizhanghu@1.com',
        #     'login': 'ceshizhanghu@1.com'
        # })
        users_env = self.env['res.users']
        user_id = users_env.search([('name', '=', '测试账户1')])
        # 记录集在调用write方法时，只能是一条记录，如果记录集中包含多条记录则需要遍历
        res = user_id.write({
            'login': 'ceshizhanghu@163.com'
        })


