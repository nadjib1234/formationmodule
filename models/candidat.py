# -*- coding:utf-8 -*-
from odoo import models,fields
class candidat(models.Model):
	_name='formation.candidat'
	name=fields.Char()
	num_ins=fields.Integer()
	
