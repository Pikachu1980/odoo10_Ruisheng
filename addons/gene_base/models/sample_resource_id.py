# -*- coding:utf-8 -*-

from odoo import api,fields,models

class SampleResource(models.Model):

    _name = "sample.resource"
    name = fields.Char('檢體來源')