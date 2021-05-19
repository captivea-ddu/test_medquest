from odoo import api, models, fields, _


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
    # name = fields.Char(String="Name")
    # name = fields.Char(String="Name")
    # name = fields.Char(String="Name")
    # name = fields.Char(String="Name")
    # name = fields.Char(String="Name")
    # name = fields.Char(String="Name")
    # name = fields.Char(String="Name")
    # name = fields.Char(String="Name")
    # name = fields.Char(String="Name")
    # name = fields.Char(String="Name")