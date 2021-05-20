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
		user_id = request.env.context.get('uid')
		existing_details = request.env['service.request'].sudo().search([('user_id', '=', user_id)], limit=1)
		case_type = None
		case_issues = None
		case_overview = None
		document_name = None
		documents = None

		for key, value in kw.items():
			# contact_name

			if key == "case_type":
				case_type = value
			elif key == "case_overview":
				case_overview = value
			elif key == "case_issues":
				case_issues = value
			elif key == "document_name":
				document_name = value
			elif key == "documents":
				documents = value
		
		if existing_details:
			#  Update
			existing_details.sudo().write({
				'case_type': case_type,
				'case_overview': case_overview,
				'case_issues' : case_issues,
			})
			i = 1
			if documents:
				for d in documents:
					request.env['ir.attachment'].sudo().create({
						'name': str(document_name) + "_" + str(i),
						'type': 'binary',
						'datas': d,
						'res_model': 'service.request',
						'res_id': existing_details.id,
					})
					i += 1

		else:
			# Create
			service_request = request.env['service.request'].sudo().create({
				'user_id': user_id,
				'case_type': case_type,
				'case_overview': case_overview,
				'case_issues' : case_issues,
			})
			request.env.cr.commit()
			i = 1
			if documents:
				for d in documents:
					request.env['ir.attachment'].sudo().create({
						'name': str(document_name) + "_" + str(i),
						'type': 'binary',
						'datas': d,
						'res_model': 'service.request',
						'res_id': service_request.id,
					})
					i += 1

		# print("$$$$$$$$$$$$$$$$ form submitted $$$$$$$$$$$$$$$$$",kw)
		# _logger.warning("$$$$$$$$$$$$$$$$ form submitted $$$$$$$$$$$$$$$$$\n" + str(kw))
		# for key, value in kw.items():
		# 	print(key,value)
		# 	_logger.warning(str(key) + " - " + str(value) + "\n")
		# return  request.redirect('/service-details', {'var': 'this is a context test'})
		# values = 
		# return request.route('/service-details/3', {'var': 'this is a context test'})
		return  request.redirect('/service-details')


	@http.route('/service-details/cancel', type='http', auth='public', website=True, method='POST')
	def other_form(self, **kw):
		user_id = request.env.context.get('uid')
		existing_details = request.env['service.request'].sudo().search([('user_id', '=', user_id)], limit=1)
		case_type = None
		case_issues = None
		case_overview = None
		document_name = None
		documents = None

		for key, value in kw.items():

			if key == "case_type":
				case_type = value
			elif key == "case_overview":
				case_overview = value
			elif key == "case_issues":
				case_issues = value
			elif key == "document_name":
				document_name = value
			elif key == "documents":
				documents = value
		
		if existing_details:
			#  Update
			existing_details.sudo().write({
				'case_type': case_type,
				'case_overview': case_overview,
				'case_issues' : case_issues,
			})
			i = 1
			if documents:
				for d in documents:
					request.env['ir.attachment'].sudo().create({
						'name': str(document_name) + "_" + str(i),
						'type': 'binary',
						'datas': d,
						'res_model': 'service.request',
						'res_id': existing_details.id,
					})
					i += 1

		else:
			# Create
			service_request = request.env['service.request'].sudo().create({
				'user_id': user_id,
				'case_type': case_type,
				'case_overview': case_overview,
				'case_issues' : case_issues,
			})
			request.env.cr.commit()
			i = 1
			if documents:
				for d in documents:
					request.env['ir.attachment'].sudo().create({
						'name': str(document_name) + "_" + str(i),
						'type': 'binary',
						'datas': d,
						'res_model': 'service.request',
						'res_id': service_request.id,
					})
					i += 1

		# print("$$$$$$$$$$$$$$$$ form submitted $$$$$$$$$$$$$$$$$",kw)
		# _logger.warning("$$$$$$$$$$$$$$$$ form submitted $$$$$$$$$$$$$$$$$\n" + str(kw))
		# for key, value in kw.items():
		# 	print(key,value)
		# 	_logger.warning(str(key) + " - " + str(value) + "\n")
		# return  request.redirect('/service-details', {'var': 'this is a context test'})
		# values = 
		# return request.route('/service-details/3', {'var': 'this is a context test'})
		return request.render('website.service_details',{'var': True})

	# @http.route('/service-details/cancel/', type='http', auth='public', website=True, method='GET')
	# def formsubmit(self, **kw):
	# 	print("########### Form Submitted ###########")
	# 	for key, value in kw.items():
	# 		print(key,value)
	# 	return  request.render('website.service_details',{'var': True})


	@http.route('/', type='http', auth='public', website=True, method='GET')
	def formsubmit(self, **kw):
		print("########### Form Submitted ###########")
		for key, value in kw.items():
			print(key,value)
		return  request.redirect('/medquest_home')





		