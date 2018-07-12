# -*- coding:utf-8 -*-

from odoo import api,fields,models

class SequencePlatform(models.Model):

    _name = "sequence.platform"
    name = fields.Char('定序平台')