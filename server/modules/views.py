import datetime
import logging
import asyncio
import aiohttp_jinja2
import jwt

from aiohttp import web
from aiohttp.web_response import json_response

from .cache import Cache
from .config import Config
from .dao import *
from .mailer import Mailer
from .exceptions import *

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


class LoginView(BaseView):

    async def post(self):
        credentials = await self.request.json()
        try:
            user = await self.user_dao.authorize(**credentials)
        except (UserDoesNotExist, PasswordDoesNotMatch):
            return json_response({'message': 'Wrong credentials'}, status=400)
        else:
            # asyncio.ensure_future(Cache.set(user['user_id'], user, 60000))
            payload = {
                'user_id': user['user_id'],
                'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=60000)
            }
            jwt_token = jwt.encode(payload, Config.get('application', 'salt'), 'HS256')
            log.info('User %s has logged in', user['email'])
            return json_response({'token': jwt_token.decode('utf-8')})


class RegistrationView(BaseView):

    async def get(self):
        confirm_key = self.request.query.get('confirm')
        try:
            error = await self.user_dao.confirm_registration(confirm_key)
        except RegistrationLinkExpired as e:
            return json_response({'error': e}, status=400)
        return json_response({'error': error},)

    async def post(self):
        new_user = await self.request.json()
        error, register_link = await self.user_dao.create_new_user(**new_user)
        if error is None:
            link = f'http://{self.request.host}{self.request.path}?confirm={register_link}'
            tpl = aiohttp_jinja2.render_string('registration.html', request=self.request, context={'link': link})
            asyncio.ensure_future(Mailer.send_mail(receiver=new_user['email'],
                                                   subject='Mapified registration', body=tpl))
        return json_response({'error': error})
