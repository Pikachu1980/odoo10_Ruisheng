# -*- coding:utf-8 -*-

from odoo import api,fields,models

class SubjectBase(models.Model):

    _name = "subject.base"

    name = fields.Char('姓名')
    sex = fields.Selection([(1,'男'),(2,'女')])
    age = fields.Integer('年齡')
    case_description = fields.Text('病例簡述')