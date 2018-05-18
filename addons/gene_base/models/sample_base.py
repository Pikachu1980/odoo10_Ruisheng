# -*- coding:utf-8 -*-

from odoo import models,api,fields

class SampleBase(models.Model):
    _name = "sample.base"
    sample_id = fields.Char('檢體編號')
    datelanded = fields.Date('送樣日期')
    sample_type = fields.Char('檢體形式')
    sample_num = fields.Integer('檢體數量')

    # 檢測結果摘要
    sequence_variation_text = fields.Text('高影響力序列變異')
    medicine_impact_text = fields.Text('藥物使用影響評估')
    disease_prognosis_text = fields.Text('疾病預後評估')

    # 定序實驗結果說明
    dna_source = fields.Char('DNA來源')
    dna_method = fields.Char('DNA萃取方式')
    Continu_sequel_preparation = fields.Char('定續集庫備製')
    sequence_platform = fields.Char('定序平台')
    sequence_mode = fields.Char('定序模式')
    preliminary_num = fields.Char('初步集庫讀數')
    comparison_database = fields.Char('比對資料庫')
    human_num = fields.Char('比對至人類序列讀數')
    human_percent = fields.Char('比對至人類序列讀數')
    target_num = fields.Char('比對至目標序列讀數')
    target_percent = fields.Char('比對至目標序列讀數')
    ten_percent_cover = fields.Char('10%分位序列覆蓋率')

    #關聯欄位
    subject_code = fields.Many2one(comodel_name='subject.base',string='受測者')
    squence_variation_code = fields.One2many(comodel_name='sequence.variation.table',inverse_name='sample_code')
    gene_impact_code = fields.One2many(comodel_name='gene.impact', inverse_name='gene',string="基因功能影響評估")
    medicine_impact_code = fields.One2many(comodel_name='medicine.impact',inverse_name='gene',string='藥物使用影響評估')

