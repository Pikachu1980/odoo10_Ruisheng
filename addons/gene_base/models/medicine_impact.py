# -*- coding:utf-8 -*-

from odoo import models,api,fields

class MedicineImpact(models.Model):
    _name = 'medicine.impact'

    gene = fields.Char('基因')
    sequence_variation = fields.Char('序列變異')
    variation_percent = fields.Char('變異比例')
    medicine_data_code = fields.One2many(comodel_name='medicine.data',inverse_name='medic_name',string='藥物')