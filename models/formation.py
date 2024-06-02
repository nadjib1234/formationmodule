# -*- coding:utf-8 -*-
from odoo import models,fields
class formation(models.Model):
	_name='formation.formation'
	name=fields.Char(string="name")
	nprix=fields.Float(string="prix")
	
