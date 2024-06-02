# -*- coding:utf-8 -*-
from odoo import models,fields,api
from datetime import datetime
class session(models.Model):

	_name='formation.session'
	name=fields.Char(string="name")
	nb_participant=fields.Integer(string="nombre de participant")
	date_debut=fields.Date(string="date de debut")
	date_fin=fields.Date(string="date de fin")
	duree=fields.Char(string="duree",compute="compute_duree")
	state=fields.Selection([
		('good','good')])
	formation_id=fields.Many2one('formation.formation')
	formateur_ids=fields.Many2many('formation.formateur')
	salle_ids=fields.Many2many('formation.salle')
	candidat_ids=fields.Many2many('formation.candidat')
	@api.depends('duree')
	def compute_duree(self):
		if(self.date_debut and self.date_fin):
		    debut=datetime.strptime(self.date_debut,"%Y-%m-%d")
		    fin=datetime.strptime(self.date_fin,"%Y-%m-%d")
		    self.duree=fin-debut
		