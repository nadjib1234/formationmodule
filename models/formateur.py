# -*- coding:utf-8 -*-
from odoo import models,fields
class formateur(models.Model):
	_name='formation.formateur'
	name=fields.Char(string="name")
	matricule=fields.Integer(string="matricule")
	diplome=fields.Char()
