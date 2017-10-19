import asyncio
import datetime
import logging

import jwt
from aiohttp.web_response import json_response

from server.modules.cache import Cache
from server.modules.config import Config
from server.modules.exceptions import UserDoesNotExist, PasswordDoesNotMatch
from server.modules.models import Users
from server.modules.views.base import BaseView


log = logging.getLogger('application')


class LoginView(BaseView):

    async def post(self):
        credentials = await self.request.json()
        try:
            user = await Users.authorize(**credentials)
        except (UserDoesNotExist, PasswordDoesNotMatch):
            return json_response({'message': 'Wrong credentials'}, status=400)
        else:
            asyncio.ensure_future(Cache.set(user['user_id'], user, 60*60*24*2))  # Session in cache lasts for 2 days
            payload = {
                'user_id': user['user_id'],
                'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=60000)
            }
            jwt_token = jwt.encode(payload, Config.get('application', 'salt'), 'HS256')
            log.info('User %s has logged in', user['email'])
            return json_response({'token': jwt_token.decode('utf-8')})
