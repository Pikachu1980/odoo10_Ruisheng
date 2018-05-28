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
    sequence_variation_code = fields.One2many(comodel_name='sequence.variation.table',inverse_name='sample_code')
    gene_impact_code = fields.One2many(comodel_name='gene.impact', inverse_name='sample_code',string="基因功能影響評估")
    medicine_impact_code = fields.One2many(comodel_name='medicine.impact',inverse_name='gene',string='藥物使用影響評估')

    @api.multi
    def name_get(self):
        result = []
        for record in self:
            name = "[%s] %s" % (record.sample_id, record.subject_code.name)
            result.append((record.id, name))
        return result

    def import_gene_impact(self):
        action = self.env.ref('gene_base.gene_impact_action').read()[0]
        action['context'] = {'default_sample_code': self.id}
        action['domain'] = [('sample_code', '=', self.id)]
        return action

    def delete_off_target_data(self):
        self.env['gene.impact'].search([('sample_code','=',self.id),('filter','like','off_target%')]).unlink()

from odoo.addons.report_doc.report.report_doc import GeneReportWord

class GeneReportDocx(GeneReportWord):

    def generate_word_report(self, document, data, objs, report):

        gene_data = list()
        gene_impact = list()

        for line in objs:
                for data in line.sequence_variation_code:
                    gene_data.append({'chromosome' : str(data.chromosome),'gene':data.gene})
                for data in line.gene_impact_code:
                    gene_impact.append({'gene': data.gene,'sequence_variation': data.sequence_variation,'gene_variation':data.gene_variation,'variation_percent':data.variation_percent,'sequence_variation_text':data.sequence_variation_text,'protein_variation_text':data.protein_variation_text})

                document.merge(
                    name=line.subject_code.name,
                    age=str(line.subject_code.age),
                    sex=str(line.subject_code.sex),
                    case_description=line.subject_code.case_description,
                    sample_id=line.sample_id,
                    datelanded=line.datelanded,
                    sample_type=line.sample_type,
                    sample_num=str(line.sample_num),
                )
                document.merge_rows('chromosome', gene_data)
                document.merge_rows('gene', gene_impact)


GeneReportDocx('report.gene_base.cancer_report', 'sample.base')



