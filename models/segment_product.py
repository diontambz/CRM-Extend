from odoo import models, fields

class SegmentProduct(models.Model):
    _name = 'segment.product'
    _description = 'Product Segment'

    name = fields.Char(string='Name', required=True)
    description = fields.Text(string='Description')