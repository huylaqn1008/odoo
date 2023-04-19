# -*- coding: utf-8 -*-
# from odoo import http


# class TutorialTheme(http.Controller):
#     @http.route('/tutorial_theme/tutorial_theme', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/tutorial_theme/tutorial_theme/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('tutorial_theme.listing', {
#             'root': '/tutorial_theme/tutorial_theme',
#             'objects': http.request.env['tutorial_theme.tutorial_theme'].search([]),
#         })

#     @http.route('/tutorial_theme/tutorial_theme/objects/<model("tutorial_theme.tutorial_theme"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('tutorial_theme.object', {
#             'object': obj
#         })
