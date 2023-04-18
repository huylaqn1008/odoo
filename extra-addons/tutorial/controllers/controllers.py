# -*- coding: utf-8 -*-
from odoo import http

class Sports(http.Controller):
    @http.route('/tutorial/sports')
    def list(self):
        Sport = http.request.env["tutorial.game"]
        sports = Sport.search([])
        sports = sports.filtered(lambda g: g.hidden == False)
        return http.request.render(
            "tutorial.game_list_template",
            {"sports": sports},
        )