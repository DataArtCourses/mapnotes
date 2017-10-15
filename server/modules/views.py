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


class UserView(BaseView):

    async def post(self):
        new_user = await self.request.json()
        error = await self.user_dao.create_new_user(**new_user)
        body = f'Hello, {new_user["email"]}'
        asyncio.ensure_future(Mailer.send_mail(receiver=new_user['email'], subject='Mapified registration', body=body))
        return json_response({'error': error})

    async def put(self):
        log.info(self.request)
        return json_response({'ok': True})
