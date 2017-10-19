import logging
import asyncio
import aiohttp_jinja2

from aiohttp import web
from aiohttp.web_response import json_response

from ..cache import Cache
from ..exceptions import UserAlreadyExist
from ..mailer import Mailer
from ..models import Users
from .base import BaseView

log = logging.getLogger('application')


class RegistrationView(BaseView):

    async def get(self):
        confirm_key = self.request.query.get('confirm')
        user_email = await Cache.get(confirm_key)
        if not user_email:
            log.info("Somebody tried to register once again with %s key", confirm_key)
            error = "Registration link expired"
            return web.Response(body=error)
        try:
            await Users.confirm_registration(user_email)
            await Cache.delete(confirm_key)
        except UserAlreadyExist as e:
            return web.Response(body=str(e), status=400)
        return web.Response(body="Thanks for registration!", status=200)

    async def post(self):
        new_user = await self.request.json()
        try:
            register_link = await Users.create_new_user(**new_user)
        except UserAlreadyExist as e:
            return json_response({'error': e}, status=400)
        else:

            link = f'http://{self.request.host}{self.request.path}?confirm={register_link}'
            tpl = aiohttp_jinja2.render_string('registration.html', request=self.request, context={'link': link})
            asyncio.ensure_future(Cache.set(register_link, new_user['email'], 60*60*24))
            asyncio.ensure_future(Mailer.send_mail(receiver=new_user['email'],
                                                   subject='Mapified registration',
                                                   body=tpl))
        return json_response({'error': None})
