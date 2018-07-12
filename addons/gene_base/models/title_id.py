# -*- coding:utf-8 -*-

from odoo import api,fields,models

class SubjectBase(models.Model):

    _name = "title.id"

    name = fields.Char('癌症中文名稱')
    name_eng = fields.Char('癌症英文名稱')