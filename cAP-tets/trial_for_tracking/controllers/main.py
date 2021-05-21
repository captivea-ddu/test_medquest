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
		# for key, value in kw.items():
		# 	print(key,value)   
		return  request.render('website.layout')

	@http.route('/submit/service-request', type='http', auth='public', website=True, method='POST')
	def other_form(self, **kw):
		user_id = request.env.context.get('uid')
		existing_details = request.env['service.request'].sudo().search([('user_id', '=', user_id)], limit=1)

		contactname = None
		contactemail = None
		casename = None
		attorname = None
		attoremail = None
		attorphone = None
		cocounsname = None
		injsname = None
		plaintname = None
		plainrel = None
		plaintbday = None
		plaintcor = None
		addt1 = None
		adder2 = None
		city = None
		state = None
		zip_ = None
		contnumber = None
		extension = None
		plantifemail = None
		plantifgen = None
		plantifgen = None
		customRadioInline1 = None
		customRadioInline2 = None

		for key, value in kw.items():

			if key == "contactname":
				contactname = value
			elif key == "contactemail":
				contactemail = value
			elif key == "casename":
				casename = value
			elif key == "attorname":
				attorname = value
			elif key == "attoremail":
				attoremail = value
			elif key == "attorphone":
				attorphone = value
			elif key == "cocounsname":
				cocounsname = value
			elif key == "injsname":
				injsname = value
			elif key == "plaintname":
				plaintname = value
			elif key == "plainrel":
				plainrel = value
			elif key == "plaintbday":
				plaintbday = value
			elif key == "plaintcor":
				plaintcor = value
			elif key == "addt1":
				addt1 = value
		
			elif key == "adder2":
				adder2 = value
			elif key == "city":
				city = value
			elif key == "state":
				state = value
			elif key == "zip":
				zip_ = value


			elif key == "contnumber":
				contnumber = value
			elif key == "extension":
				extension = value
			elif key == "plantifemail":
				plantifemail = value
			elif key == "plantifgen":
				plantifgen = value
				
			elif key == "customRadioInline1":
				should_expidite = True
			elif key == "customRadioInline2":
				should_expidite = False
		
		value_dict = {'contactname' : contactname, 
					'contactemail' : contactemail, 
					'casename' : casename, 
					'attorname' : attorname, 
					'attoremail' : attoremail, 
					'attorphone' : attorphone, 
					'cocounsname' : cocounsname, 
					'injsname' : injsname, 
					'plaintname' : plaintname, 
					'plainrel' : plainrel, 
					'plaintbday' : plaintbday, 
					'plaintcor' : plaintcor, 
					'addt1' : addt1, 
					'adder2' : adder2, 
					'city' : city, 
					'state' : state, 
					'zip_' : zip_, 
					'contnumber' : contnumber, 
					'extension' : extension, 
					'plantifemail' : plantifemail, 
					'plantifgen' : plantifgen, 
					'plantifgen' : plantifgen, 
					'should_expidite' : should_expidite
					}
		if existing_details:
			existing_details.sudo().write(value_dict)
		else:
			service_request = request.env['service.request'].sudo().create(value_dict)
			request.env.cr.commit()
		return request.redirect('/case-details')


	@http.route('/submit/service-details/', type='http', auth='public', website=True, method='POST')
	def another_form(self, **kw):
		user_id = request.env.context.get('uid')
		existing_details = request.env['service.request'].sudo().search([('user_id', '=', user_id)], limit=1)
		nar = None
		binder = None
		maxtrix = None
		depo = None
		hotlink = None
		legterm = None
		medop = None
		found = None
		bill = None
		book = None
		lifecare = None
		demand = None
		scr = None
		pain = None
		suf = None
		synop = None
		fact = None
		res = None
		jury = None
		custom = None
		rev = None
		time = None
		cen = None
		ulc = None
		other = None
		should_expidite = None
		cost = None
		for key, value in kw.items():
			if key == 'nar':
				nar = value
			elif key == 'binder':
				binder = value
			elif key == 'maxtrix': 
				maxtrix = value
			elif key == 'depo':
				depo = value
			elif key == 'hotlink':
				hotlink = value
			elif key == 'legterm': 
				legterm = value
			elif key == 'medop':
				medop = value
			elif key == 'found':
				found = value
			elif key == 'bill':
				bill = value
			elif key == 'book':
				book = value
			elif key == 'lifecare': 
				lifecare = value
			elif key == 'demand':
				demand = value
			elif key == 'scr':
				scr = value
			elif key == 'pain': 
				pain = value
			elif key == 'suf':
				suf = value
			elif key == 'synop': 
				synop = value
			elif key == 'fact':
				fact = value
			elif key == 'res':
				res = value
			elif key == 'jury': 
				jury = value
			elif key == 'custom': 
				custom = value
			elif key == 'rev':
				rev = value
			elif key == 'time': 
				time = value
			elif key == 'cen':
				cen = value
			elif key == 'ulc':
				ulc = value
			elif key == 'other': 
				other = value
			elif key == 'customRadioInline1': 
				should_expidite = True
			elif key == 'customRadioInline2': 
				should_expidite = False
			elif key == 'cost':
				cost = value


		value_dict = {'nar' : nar, 
						'binder' : binder, 
						'maxtrix' : maxtrix, 
						'depo' : depo, 
						'hotlink' : hotlink, 
						'legterm' : legterm, 
						'medop' : medop, 
						'found' : found, 
						'bill' : bill, 
						'book' : book, 
						'lifecare' : lifecare, 
						'demand' : demand, 
						'scr' : scr, 
						'pain' : pain, 
						'suf' : suf, 
						'synop' : synop, 
						'fact' : fact, 
						'res' : res, 
						'jury' : jury, 
						'custom' : custom, 
						'rev' : rev, 
						'time' : time, 
						'cen' : cen, 
						'ulc' : ulc, 
						'other' : other, 
						'cost' : cost, 
					}
		if existing_details:
			existing_details.sudo().write(value_dict)
		else:
			service_request = request.env['service.request'].sudo().create(value_dict)
			request.env.cr.commit()
		return request.render('website.layout')

	@http.route('/case-details/', type='http', auth='private', website=True, method='GET')
	def case_details_form_controller(self, **kw):
		user_id = request.env.context.get('uid')
		return request.render('website.case_details')

	@http.route('/submit/case-details/', type='http', auth='public', website=True, method='POST')
	def case_details_form_submit_controller(self, **kw):
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


		return request.render("website.service_details")


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

		return request.render('website.home_page',{'var': True})




	@http.route('/', type='http', auth='public', website=True, method='GET')
	def homepage(self, **kw):

		return  request.render('website.home_page')





		