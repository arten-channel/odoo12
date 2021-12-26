from odoo import http
import akshare as ak
from odoo.http import request

nameMap = {
    '黑龙江省': '黑龙江',
    '吉林省': '吉林',
    '辽宁省': '辽宁',
    '北京市': '北京',
    '天津市': '天津',
    '上海市': '上海',
    '河北省': '河北',
    '河南省': '河南',
    '山东省': '山东',
    '浙江省': '浙江',
    '湖南省': '湖南',
    '湖北省': '湖北',
    '四川省': '四川',
    '西藏自治区': '西藏',
    '青海省': '青海',
    '宁夏回族自治区': '宁夏',
    '重庆市': '重庆',
    '云南省': '云南',
    '广西壮族自治区': '广西',
    '广东省': '广东',
    '内蒙古自治区': '内蒙古',
    '山西省': '山西',
    '江苏省': '江苏',
    '陕西省': '陕西',
    '甘肃省': '甘肃',
    '江西省': '江西',
    '海南省': '海南',
    '安徽省': '安徽',
    '福建省': '福建',
    '贵州省': '贵州',
    '台湾省': '台湾',
    '香港特别行政区': '香港',
    '澳门特别行政区': '澳门',
    '新疆维吾尔自治区': '新疆',
}


class EpidemicTongjiPage(http.Controller):

    @http.route('/data/map', type='json', auth='user')
    def data_tongji(self, **kwargs):
        data = dict()
        news_target = self._data_news()
        province_data = self._data_hot_map()
        history_data = self._history_data(kwargs)
        data['news_target'] = news_target
        data['province_data'] = province_data
        data['history_data'] = history_data
        return data

    @http.route('/data/line', type='json', auth='user')
    def data_line(self, **kwargs):
        data = dict()
        history_data = self._history_data(kwargs)
        data['history_data'] = history_data
        return data

    def _data_news(self):
        """获取新闻"""
        news = ak.covid_19_163(indicator="实时资讯新闻播报")
        inxs = news.index
        a_target = """<a href="{}">{}</a> <br/>"""
        news_target = ''
        for inx in inxs:
            col = news.loc[inx]
            current_a = a_target.format(col[-1], col[0])
            news_target += current_a
            if inx >= 10: break
        news_target = """<div>{}</div>""".format(news_target)
        return news_target

    def _data_hot_map(self):
        objs = request.env['tongji.to.province'].search([])
        data = []
        for obj in objs:
            data.append({'name': nameMap[obj.state_id.name], 'value': obj.total_confirm})
        return data

    def _history_data(self, kw):
        data = {'date': [], 'value': []}
        objs = request.env['history.data.days'].search([], order='date')
        if kw.get('domain', False) == 'input':
            for obj in objs:
                data['date'].append(obj.date)
                data['value'].append(obj.import_abroad)
        else:
            for obj in objs:
                data['date'].append(obj.date)
                data['value'].append(obj.confirm)
        return data