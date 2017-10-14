import logging
import aiohttp_jinja2

from aiohttp import web
from aiohttp.web_response import json_response

from .dao import *


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
        log.info(new_user)
        user_id = await self.user_dao.create_new_user(**new_user)
        log.info(user_id)
        if user_id:
            return json_response({'ok': True})
        else:
            return json_response({'ok': False})

    async def put(self):
        log.info(self.request)
        return json_response({'ok': True})
