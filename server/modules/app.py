import os
import logging

import jinja2
import aiohttp_jinja2
import aiohttp_cors

from aiohttp import web

from .routes import routes
from .middlewares import middleware_factory

log = logging.getLogger('application')
template_folder = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'templates')


application = web.Application(middlewares=[middleware_factory])

cors = aiohttp_cors.setup(application, defaults={
    "*": aiohttp_cors.ResourceOptions(
            allow_credentials=True,
            expose_headers="*",
            allow_headers="*",
        )
})
aiohttp_jinja2.setup(application, loader=jinja2.FileSystemLoader(template_folder))

# todo remove in PROD environment
for route in routes:
    for method in ('get', 'post', 'delete', 'put'):
        handler = getattr(route['handler'], method, None)
        if not handler:
            continue
        application.router.add_route(method, route['path'], route['handler'])
