# -*- coding:utf-8 -*-

from odoo import api,fields,models

class DnaExtract(models.Model):

    _name = "dna.extract"
    name = fields.Char('DNA萃取方式')