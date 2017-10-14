import os
import logging

import jinja2
import aiohttp_jinja2

from aiohttp import web

from .routes import routes

log = logging.getLogger('application')
template_folder = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'templates')


application = web.Application()
aiohttp_jinja2.setup(application, loader=jinja2.FileSystemLoader(template_folder))

for route in routes:
    application.router.add_route(route[0], route[1], route[2], name=route[3])

