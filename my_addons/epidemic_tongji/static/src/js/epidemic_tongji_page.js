odoo.define('Epidemic.TongjiPage', function (require) {

    var AbstractAciton = require('web.AbstractAction');
    var core = require('web.core');

    var TongjiPage = AbstractAciton.extend({
        template: 'EpidemicTongjiPage',
        events: {
            'click .input': 'load_line_graph',

        },

        start: function () {
            var self = this;
            var data;
            this._rpc({route: '/data/map', params: []})
                .then(function (data) {
                    self._show_map_graph(data);
                    self._show_line_graph(data);
                    self._show_news_data(data);
                })
        },

        _show_news_data: function(data){
            console.log(data);
            var $newsdata = document.getElementById('newsdata');
            var node_news = new DOMParser().parseFromString(data.news_target, 'text/html').body.children[0];
            $newsdata.appendChild(node_news);
        },

        _show_map_graph: function (data) {
            var chartDom = document.getElementById('graphmap');
            var myChart = echarts.init(chartDom);
            var option;
            myChart.showLoading();
            $.get('/epidemic_tongji/static/src/json/china.json', function (geoJson) {
                myChart.hideLoading();
                echarts.registerMap('china', geoJson);
                myChart.setOption(option = {
                    title: {
                        text: '中国历史时点数据',
                        subtext: '数据来源akshare',
                        sublink: 'https://www.akshare.xyz/zh_CN/latest/data/event/event.html'
                    },
                    tooltip: {
                        trigger: 'item',
                        formatter: '{b}<br/>{c}'
                    },
                    toolbox: {
                        show: true,
                        orient: 'vertical',
                        left: 'right',
                        top: 'center',
                        feature: {
                            dataView: {readOnly: false},
                            restore: {},
                            saveAsImage: {}
                        }
                    },
                    visualMap: {
                        type: 'piecewise',
                        pieces: [
                            {min: 10000, max: 1000000, label: '大于等于10000人', color: '#372a28'},
                            {min: 1000, max: 9999, label: '确诊1000-9999', color: '#4e160f'},
                            {min: 500, max: 999, label: '确诊500-999人', color: '#974236'},
                            {min: 100, max: 499, label: '确诊100-499人', color: '#ee7263'},
                            {min: 1, max: 99, label: '确诊1-99人', color: '#f5bba7'},
                        ],
                        color: ['#E0022B', '#E09107', '#A3E00B']
                    },
                    textStyle: {fontSize: 10},

                    series: [
                        {
                            name: '中国历史时点数据',
                            type: 'map',
                            mapType: 'china', // 自定义扩展图表类型
                            label: {
                                show: true
                            },
                            data: data.province_data,
                            // 自定义名称映射
                            nameMap: {
                                '黑龙江省': '黑龙江',
                                '吉林省': '吉林',
                                '辽宁省': '辽宁',
                                '北京市': '北京',
                                '天津市': '天津',
                                '上海市': '上海',
                                '河北省': '河北',
                                '河南省': '河南',
                                '山东省': '山东',
                                '湖南省': '湖南',
                                '浙江省': '浙江',
                                '湖南省': '湖南',
                                '湖北省': '湖北',
                                '四川省': '四川',
                                '西藏自治区': '西藏',
                                '青海省': '青海',
                                '宁夏回族自治区': '宁夏',
                                '重庆市': '重庆',
                                '云南省': '云南',
                                '贵州省': '贵州',
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
                        }
                    ]
                });
            });
            option && myChart.setOption(option);
        },

        load_line_graph: function(event){
            var className = event.currentTarget.className;
            var self = this;
            if (className === 'input'){
                var params = {'domain': 'input'};
            } else{
                console.log('什么也不做');
            }
            this._rpc({route: 'data/line', params: params})
                .then(function (data) {
                    self._show_line_graph(data);
                })
        },

        _show_line_graph: function (data) {
            var chartDom = document.getElementById('graphline');
            var myChart = echarts.init(chartDom);
            var option;
            console.log(data);
            option = {
                title: {
                    text: '中国历史时点数据'
                },
                xAxis: {
                    name: '日期',
                    type: 'category',
                    data: data.history_data.date,
                },
                yAxis: {
                    name: '数量',
                    type: 'value'
                },
                series: [{
                    data: data.history_data.value,
                    type: 'line'
                }]
            };
            option && myChart.setOption(option);
        }

    });

    core.action_registry.add('epidemic.tongji.page', TongjiPage);

})