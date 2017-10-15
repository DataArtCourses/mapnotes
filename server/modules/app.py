import os
import logging

import jinja2
import aiohttp_jinja2

from aiohttp import web
import aiohttp_cors

from .routes import routes

log = logging.getLogger('application')
template_folder = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'templates')


application = web.Application()
cors = aiohttp_cors.setup(application, defaults={
    "*": aiohttp_cors.ResourceOptions(
            allow_credentials=True,
            expose_headers="*",
            allow_headers="*",
        )
})
aiohttp_jinja2.setup(application, loader=jinja2.FileSystemLoader(template_folder))

for route in routes:
    app = application.router.add_route(route[0], route[1], route[2], name=route[3])
    cors.add(app)

