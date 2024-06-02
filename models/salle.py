# -*- coding:utf-8 -*-
from odoo import models,fields
class salle(models.Model):
	_name='formation.salle'
	name=fields.Char()
	libre=fields.Boolean()
	nb_place=fields.Integer()
