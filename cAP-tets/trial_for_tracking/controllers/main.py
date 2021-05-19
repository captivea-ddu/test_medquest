# -*- coding: utf-8 -*-
import json
import logging
from odoo import http
from odoo.http import request
from odoo.addons.website_sale.controllers.main import WebsiteSale

_logger = logging.getLogger(__name__)

class WebsiteSaleCustom(http.Controller):

	@http.route('/service/', type='http', auth='public', website=True, method='GET')
	def formsubmit(self, **kw):
		print("########### Form Submitted ###########")
		for key, value in kw.items():
			print(key,value)
		return  request.render('website.layout')

	@http.route('/submit/service-request/', type='http', auth='public', website=True, method='POST')
	def other_form(self, **kw):
		print("$$$$$$$$$$$$$$$$ form submitted $$$$$$$$$$$$$$$$$",kw)
		_logger.warning("$$$$$$$$$$$$$$$$ form submitted $$$$$$$$$$$$$$$$$\n" + str(kw))
		for key, value in kw.items():
			print(key,value)
			_logger.warning(str(key) + " - " + str(value) + "\n")
		return  request.render('website.layout')


	@http.route('/submit/service-select/', type='http', auth='public', website=True, method='POST' )
	def another_form(self, **kw):
		for key, value in kw.items():
			print(key,value)
		return  request.render('website.layout')

	@http.route('/submit/case-details/', type='http', auth='public', website=True, method='POST')
	def other_form(self, **kw):
		for key, value in kw.items():
			print(key,value)

		user_id = request.env.context.get('uid')
		existing_details = request.env['service.request'].sudo().search([('user_id', '=', user_id)], limit=1)
		if existing_details:
			test = 1
			#  Update
		else:
			test = 2
			# Create

		print("$$$$$$$$$$$$$$$$ form submitted $$$$$$$$$$$$$$$$$",kw)
		_logger.warning("$$$$$$$$$$$$$$$$ form submitted $$$$$$$$$$$$$$$$$\n" + str(kw))
		for key, value in kw.items():
			print(key,value)
			_logger.warning(str(key) + " - " + str(value) + "\n")
		return  request.render('website.layout')

	@http.route('/', type='http', auth='public', website=True, method='GET')
	def formsubmit(self, **kw):
		print("########### Form Submitted ###########")
		for key, value in kw.items():
			print(key,value)
		return  request.redirect('/medquest_home')