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

    cron = fields.Boolean()

    nar = fields.Boolean()

    binder = fields.Boolean()

    maxtrix = fields.Boolean()

    depo = fields.Boolean()

    hotlink = fields.Boolean()

    legterm = fields.Boolean()

    medop = fields.Boolean()

    found = fields.Boolean()

    bill = fields.Boolean()

    book = fields.Boolean()

    lifecare = fields.Boolean()

    demand = fields.Boolean()

    scr = fields.Boolean()

    pain = fields.Boolean()

    suf = fields.Boolean()

    synop = fields.Boolean()

    fact = fields.Boolean()

    res = fields.Boolean()

    jury = fields.Boolean()

    custom = fields.Boolean()

    rev = fields.Boolean()

    time = fields.Boolean()

    cen = fields.Boolean()

    ulc = fields.Boolean()

    other = fields.Boolean()

    should_expidite = fields.Boolean()

    cost = fields.Boolean()

    contactname = fields.Char(size=70)

    contactemail = fields.Char(size=70)

    contactphone = fields.Char(size=80)

    attorname = fields.Char(size=70)

    attoremail = fields.Char(size=70)

    attorphone = fields.Char(size=70)

    cocounsname = fields.Char(size=70)

    injsname = fields.Char(size=70)

    plaintname = fields.Char(size=70)

    plainrel = fields.Char(size=70)

    plaintbday = fields.Char(size=70)

    plaintcor = fields.Char(size=70)

    addt1 = fields.Char(size=70)

    adder2 = fields.Char(size=70)

    city = fields.Char(size=70)

    state = fields.Char(size=70)

    zip_ = fields.Char(size=70)

    contnumber = fields.Char(size=70)

    extension = fields.Char(size=70)

    plantifemail = fields.Char(size=70)

    plantifgen = fields.Char(size=70)

    plantifgen = fields.Char(size=70)



    # documents = fields.One2many('ir.attachment', 'service_request_id', string="Attachments")

    # contact_name = fields.Char(string="Contact Name")

    # document_name = fields.Text()


class ServiceRequest(models.Model):
    _name = "other.model"


    contactname = fields.Char(size=70)

    contactname = fields.Char(size=70)

    contactemail = fields.Char(size=70)

    contactphone = fields.Char(size=80)

    attorname = fields.Char(size=70)

    attoremail = fields.Char(size=70)

    attorphone = fields.Char(size=70)

    firmname

    plaintname = fields.Char(size=70)

    plainrel = fields.Char(size=70)

    plaintbday = fields.Char(size=70)

    plaintcor = fields.Char(size=70)

    addt1 = fields.Char(size=70)

    adder2 = fields.Char(size=70)

    city = fields.Char(size=70)

    state = fields.Char(size=70)

    zip_ = fields.Char(size=70)

    contnumber = fields.Char(size=70)

    extension = fields.Char(size=70)

    plantifemail = fields.Char(size=70)

    plantifgen = fields.Char(size=70)

    plantifgen = fields.Char(size=70)