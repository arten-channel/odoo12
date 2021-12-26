from odoo import fields, api, models
from odoo import tools


class MySaleReport(models.Model):
    _name = 'my.sale.report'
    _auto = False
    _description = '销售报表'

    """
    展开：产品、产品变体、价格表、客户、销售单、销售员、销售团队
    数值字段：含税总计、不含税总计、数量
    """

    product_tmpl_id = fields.Many2one('product.template', string='产品')
    product_id = fields.Many2one('product.product', string='产品SKU')
    pricelist_id = fields.Many2one('product.pricelist', string='价格表')
    partner_id = fields.Many2one('res.partner', string='客户')
    user_id = fields.Many2one('res.users', string='销售员')
    team_id = fields.Many2one('crm.team', string='销售团队')
    order_id = fields.Many2one('sale.order', string='销售订单')
    amount_untaxed = fields.Float(string='不含税金额')
    amount_taxed = fields.Float(string='含税金额')
    product_uom_qty = fields.Float(string='数量')
    confirmation_date = fields.Datetime('确认日期', readonly=True)

    def _query(self, with_clause='', fields={}, groupby='', from_clause=''):
        select_ = """
            min(l.id) as id,
            l.order_id as order_id,
            s.partner_id as partner_id,
            s.user_id as user_id,
            s.pricelist_id as pricelist_id,
            s.team_id as team_id,
            l.product_id as product_id,
            p.product_tmpl_id as product_tmpl_id,
            sum(l.product_uom_qty) as product_uom_qty,
            sum(price_unit * l.product_uom_qty) as amount_taxed,  
            s.confirmation_date as confirmation_date,
            0.0 as amount_untaxed     
        """
        from_ = """
            sale_order_line l
            join sale_order s on l.order_id=s.id
            left join res_partner partner on s.partner_id=partner.id
            left join crm_team c on s.team_id=c.id
            left join res_users r on s.user_id=r.id
            left join product_pricelist pricelist on s.pricelist_id=pricelist.id
            left join product_product p on l.product_id=p.id
            left join product_template t on p.product_tmpl_id=t.id   
        """
        groupby_ = """
            l.id,
            l.product_id,
            l.order_id,
            s.partner_id,
            s.user_id,
            s.pricelist_id,
            s.team_id,
            p.product_tmpl_id,
            s.confirmation_date
        """

        return '(SELECT %s FROM %s WHERE l.product_id IS NOT NULL GROUP BY %s)' % (select_, from_, groupby_)

    @api.model_cr
    def init(self):
        tools.drop_view_if_exists(self.env.cr, self._table)
        self.env.cr.execute("""CREATE or REPLACE VIEW %s as (%s)""" % (self._table, self._query()))
