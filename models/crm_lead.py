from odoo import models, fields, api

class CrmLead(models.Model):
    _inherit = 'crm.lead'

    is_new_customer = fields.Boolean(string='Pelanggan Baru?')
    customer_segment = fields.Selection([
        ('construction', 'Konstruksi'),
        ('banking', 'Perbankan'),
        ('government', 'Pemerintah'),
        ('state_owned', 'BUMD/BUMN'),
        ('ministry', 'Kementrian'),
        ('other', 'Swasta Lainnya')
    ], string='Segment Pelanggan')
    
    segment_product_id = fields.Many2one('segment.product', string='Segment Product')
    
    task_ids = fields.One2many('crm.task.progress', 'lead_id', string='Task Progress')

class CrmTaskProgress(models.Model):
    _name = 'crm.task.progress'
    _description = 'CRM Task Progress'

    lead_id = fields.Many2one('crm.lead', string='Pipeline')
    task = fields.Char(string='Task', required=True)
    deadline = fields.Date(string='Deadline')
    status = fields.Selection([
        ('todo', 'To Do'),
        ('progress', 'Progress'),
        ('done', 'Done')
    ], string='Status', default='todo')

    progress = fields.Float(string='Progress', compute='_compute_progress', store=True)

    @api.depends('status')
    def _compute_progress(self):
        for record in self:
            if record.status == 'todo':
                record.progress = 0
            elif record.status == 'progress':
                record.progress = 50
            elif record.status == 'done':
                record.progress = 100