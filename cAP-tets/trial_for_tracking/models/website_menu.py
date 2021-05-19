from odoo import api, models, fields, _

# class Attachments(models.Model):
#     _inherit = 'ir.attachment'

#     service_request_id = fields.Many2one('service.request', string='Service Request Form')

class SaleOrder(models.Model):
    _inherit = "website.menu"

    image = fields.Binary(string='Image')


class ServiceRequest(models.Model):
    _name = "service.request"

    name = fields.Char(String="Name")
    user_id = fields.Many2one(
        'res.users',
        string='User',
        help='User',
    )

    case_type = fields.Selection([( 'motor','Motor Vehicle Accident'), 
                                  ('nurse' , 'Nursing Home'),
                                  ('defective','Defective Product'),
                                  ('wrong','Wrongful Death'),
                                  ('mal' ,'Medical Malpractice and Premises')])

    case_overview = fields.Text(string='Overview')

    case_issues = fields.Text(string='Case Issues and Focus')

    documents = fields.One2many('ir.attachment', 'service_request_id', string="Attachments")

    # contact_name = fields.Char(string="Contact Name")

    # document_name = fields.Text()