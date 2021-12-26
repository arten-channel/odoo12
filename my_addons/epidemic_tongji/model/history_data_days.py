from odoo import api, fields, models
import akshare as ak


class HistoryDataDays(models.Model):
    _name = 'history.data.days'
    _description = '中国历史时点数据'

    date = fields.Date(string='日期')
    confirm = fields.Integer(string='新增确诊人数')
    suspect = fields.Integer(string='新增疑似人数')
    heal = fields.Integer(string='新增治愈人数')
    dead = fields.Integer(string='新增死亡人数')
    severe = fields.Integer(string='新增重症人数')
    import_abroad = fields.Integer(string='境外输入')

    def get_akshare_data(self):
        covid_19_163_df = ak.covid_19_163(indicator="中国历史时点数据")
        inxs = covid_19_163_df.index
        for inx in inxs:
            col = covid_19_163_df.loc[inx]
            val = {
                'date': inx,
                'confirm': col[0],
                'suspect': col[1],
                'heal': col[2],
                'dead': col[3],
                'severe': col[4],
                'import_abroad': col[6]
            }
            self.create(val)

        print(covid_19_163_df.columns)
        print(inxs)


