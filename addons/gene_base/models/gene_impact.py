# -*- coding:utf-8 -*-
from odoo import models,api,fields

class gene_impact(models.Model):
    _name = 'gene.impact'


    effect = fields.Char('影響程度')
    gene = fields.Char('基因')
    sequence_variation = fields.Char('序列變異')
    gene_variation = fields.Char('基因變異')
    variation_percent = fields.Char('變異比例')
    sequence_variation_text = fields.Char('序列變異說明')
    protein_variation_text = fields.Char('蛋白質變異說明')
    filter = fields.Char('')

    sample_code = fields.Many2one(comodel_name='sample.base', string='檢體資料')