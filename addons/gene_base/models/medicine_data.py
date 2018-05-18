# -*- coding:utf-8 -*-

from odoo import models,api,fields

class MedicineImpact(models.Model):
    _name = 'medicine.data'

    medic_react = fields.Char('藥物反應')
    medic_name = fields.Char('藥物名')
    medic_attrs = fields.Char('藥物屬性')
    treat_target = fields.Char('治療目標')