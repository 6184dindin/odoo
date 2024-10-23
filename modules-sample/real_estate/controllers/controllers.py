# -*- coding: utf-8 -*-
# from odoo import http


# class Module-estate(http.Controller):
#     @http.route('/module-estate/module-estate', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module-estate/module-estate/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('module-estate.listing', {
#             'root': '/module-estate/module-estate',
#             'objects': http.request.env['module-estate.module-estate'].search([]),
#         })

#     @http.route('/module-estate/module-estate/objects/<model("module-estate.module-estate"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module-estate.object', {
#             'object': obj
#         })

