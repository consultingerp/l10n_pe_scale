# -*- encoding: utf-8 -*-
from odoo import http
from odoo.http import request, Controller

class WebScale(Controller):


	@http.route('/test', type='json', methods=['POST'], auth="public")
	def test(self):
		return {
			'weight': 43.2
		}

	@http.route('/l10n_pe_scale', type='http', auth="public")
	def scale(self, **kw):
		purchase = request.env['purchase.order'].search([('id','=',kw['purchase'])])
		product = request.env['product.product'].search([('name','=','Propinas')])
		purchase.write({
			'order_line': [(0,0,{
				'date_planned': '2020-01-01',
				'product_id': product.id,
				'price_unit': product.list_price,
				'name': product.name,
				'product_uom': product.uom_id.id,
				'product_qty': float(kw['weight'])
			})]
		})
		return True