# -*- coding:utf-8 -*-
from odoo import models,fields,api
class wizard_attestation(models.Model):
	_name='formation.wizarattestation'
	date=fields.Date(string="date")
	description=fields.Text()
	def get_condidat(self):
		Sessid=self.env.context.get('active_id')
		session=self.env['formation.session'].browse(Sessid)
		return session.candidat_ids
	@api.multi
	def action_done(self):
		Sessid=self.env.context.get('active_id')
		session=self.env['formation.session'].browse(Sessid)
		for candidat in self.candidat_ids:
			self.env['formation.attestation'].create({
				'date': self.date,
				'description':self.description,
				'candidat_ids':candidat.id,
				'formation_id':session.formation_id.id,
				})


	candidat_ids=fields.Many2many('formation.candidat',default=get_condidat)    	


