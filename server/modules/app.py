import os
import logging
import asyncio

import jinja2
import aiohttp_jinja2
import aiohttp_cors

from aiohttp import web

from .routes import routes
from .middlewares import auth_middleware
from .mailer import Mailer
from .dao import Dao
from .cache import Cache

log = logging.getLogger('application')
template_folder = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'templates')


async def initialize(_):
    log.info('Initializing external services')
    await asyncio.gather(Mailer.connect(),
                         Dao.connect())
                         # Cache.connect())
    log.info('External services initialized')


async def on_shutdown(_):
    log.info('Shutting down server...')
    await Mailer.close()

application = web.Application(middlewares=[auth_middleware])
application.on_startup.append(initialize)
application.on_shutdown.append(on_shutdown)

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
