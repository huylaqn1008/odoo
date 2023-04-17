# -*- coding: utf-8 -*-

from odoo import models, fields


class Game(models.Model):
    _name = 'tutorial.game'
    _description = 'Game model of Tutorial App'

    name = fields.Char("Name", required=True)
    image = fields.Binary("Cover")

    released_date = fields.Date()
    publisher_ids = fields.Many2many(
        "res.partner", relation="publisher_rel", string="Publishers" 
    )
    developer_ids = fields.Many2many(
        "res.partner", relation="developer_rel", string="Developers"
    )
