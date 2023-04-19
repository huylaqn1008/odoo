# -*- coding: utf-8 -*-
# from odoo import http


# class TutorialSnippet(http.Controller):
#     @http.route('/tutorial_snippet/tutorial_snippet', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/tutorial_snippet/tutorial_snippet/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('tutorial_snippet.listing', {
#             'root': '/tutorial_snippet/tutorial_snippet',
#             'objects': http.request.env['tutorial_snippet.tutorial_snippet'].search([]),
#         })

#     @http.route('/tutorial_snippet/tutorial_snippet/objects/<model("tutorial_snippet.tutorial_snippet"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('tutorial_snippet.object', {
#             'object': obj
#         })
