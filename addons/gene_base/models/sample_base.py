# -*- coding:utf-8 -*-

from odoo import models,api,fields

class SampleBase(models.Model):
    _name = "sample.base"
    sample_id = fields.Char('檢體編號')
    datelanded = fields.Date('送樣日期')
    sample_type = fields.Char('檢體形式')
    sample_num = fields.Integer('檢體數量')

    subject_code = fields.Many2one(comodel_name='subject.base',string='受測者')
    squence_variation_code = fields.One2many(comodel_name='sequence.variation.table',inverse_name='sample_code')
    gene_impact_code = fields.One2many(comodel_name='gene.impact', inverse_name='gene',string="基因功能影響評估")

