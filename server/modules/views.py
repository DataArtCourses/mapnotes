import logging
import asyncio
import aiohttp_jinja2

from aiohttp import web
from aiohttp.web_response import json_response

from .dao import *
from .mailer import Mailer

log = logging.getLogger('application')


class BaseView(web.View):

    user_dao = UserDao()
    pin_dao = PinDao()
    chat_dao = ChatDao()
    chat_message_dao = ChatMessageDao()
    pin_message_dao = PinMessageDao()

    @aiohttp_jinja2.template('index.html')
    async def get(self):
        return {}


class RegistrationView(BaseView):

    async def get(self):
        confirm_key = self.request.query.get('confirm')
        error = await self.user_dao.confirm_registration(confirm_key)
        return json_response({'error': error})

    async def post(self):
        new_user = await self.request.json()
        error, register_link = await self.user_dao.create_new_user(**new_user)
        if error is None:
            link = f'http://{self.request.host}{self.request.path}?confirm={register_link}'
            tpl = aiohttp_jinja2.render_string('registration.html', request=self.request, context={'link': link})
            asyncio.ensure_future(Mailer.send_mail(receiver=new_user['email'],
                                                   subject='Mapified registration', body=tpl))
        return json_response({'error': error})
