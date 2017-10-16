import os
import logging

import jinja2
import aiohttp_jinja2
import aiohttp_cors

from aiohttp import web

from .routes import routes

log = logging.getLogger('application')
template_folder = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'templates')


application = web.Application()
# todo CBS don't work with CORS setup
# cors = aiohttp_cors.setup(application, defaults={
#     "*": aiohttp_cors.ResourceOptions(
#             allow_credentials=True,
#             expose_headers="*",
#             allow_headers="*",
#         )
# })
aiohttp_jinja2.setup(application, loader=jinja2.FileSystemLoader(template_folder))

for route in routes:
    application.router.add_route(**route)


