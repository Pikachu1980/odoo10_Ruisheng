# -*- coding:utf-8 -*-

from odoo import models,api,fields

class SequenceVariationTable(models.Model):
    _name = 'sequence.variation.table'

    chromosome = fields.Char('染色體')
    gene = fields.Char('基因')
    total_sequence_variation = fields.Char('總序列變異數')
    SNV = fields.Integer(string='SNV')
    INDEL = fields.Integer(string='INDEL')
    MIS = fields.Integer(string='MIS')
    SYN = fields.Integer(string='SYN')
    UTR1 = fields.Integer(string='3UTR')
    UTR2 = fields.Integer(string='5UTR')
    INTR = fields.Integer(string='INTR')
    A = fields.Boolean()
    B = fields.Boolean()
    C = fields.Boolean()
    D = fields.Boolean()

    sample_code = fields.Many2one(comodel_name='sample.base',string='檢體資料')