# -*- coding: utf-8 -*-
# from odoo import http


# class TutorialCategory(http.Controller):
#     @http.route('/tutorial_category/tutorial_category', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/tutorial_category/tutorial_category/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('tutorial_category.listing', {
#             'root': '/tutorial_category/tutorial_category',
#             'objects': http.request.env['tutorial_category.tutorial_category'].search([]),
#         })

#     @http.route('/tutorial_category/tutorial_category/objects/<model("tutorial_category.tutorial_category"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('tutorial_category.object', {
#             'object': obj
#         })
