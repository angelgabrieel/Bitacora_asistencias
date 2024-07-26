# -*- coding: utf-8 -*-
# from odoo import http


# class BitacoraAsistencias(http.Controller):
#     @http.route('/bitacora_asistencias/bitacora_asistencias/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/bitacora_asistencias/bitacora_asistencias/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('bitacora_asistencias.listing', {
#             'root': '/bitacora_asistencias/bitacora_asistencias',
#             'objects': http.request.env['bitacora_asistencias.bitacora_asistencias'].search([]),
#         })

#     @http.route('/bitacora_asistencias/bitacora_asistencias/objects/<model("bitacora_asistencias.bitacora_asistencias"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('bitacora_asistencias.object', {
#             'object': obj
#         })
