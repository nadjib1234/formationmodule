# -*- coding:utf-8 -*-
from odoo import models,fields
class attestation(models.Model):
	_name='formation.attestation'
	date=fields.Date(string="date")
	description=fields.Text()
	candidat_ids=fields.Many2one('formation.candidat')
	formation_id=fields.Many2one('formation.formation')