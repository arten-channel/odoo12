from odoo import api, fields, models
import akshare as ak

class TongjiToProvince(models.Model):
    _name = 'tongji.to.province'
    _description = '中国疫情分省统计详情'

    state_id = fields.Many2one('res.country.state', domain="[('country_id', '=', 48)]",string='省')
    total_confirm = fields.Integer(string='累计确诊')
    state_code = fields.Char(related='state_id.code')

    def get_akshare_data_tongji(self):
        covid_19_163_df = ak.covid_19_163(indicator="中国各地区累计数据")
        inxs = covid_19_163_df.index
        for inx in inxs:
            col = covid_19_163_df.loc[inx]
            state_obj = self.env['res.country.state'].search([('name', 'like', inx)])
            val = {'state_id': state_obj.id, 'total_confirm': col[0]}
            self.create(val)
        # print('返回值：', covid_19_163_df)
        # print('数据索引', inxs)