import jwt

from aiohttp.web_response import json_response

from .config import Config
from .cache import Cache
from .dao import UserDao


async def auth_middleware(_, handler):
    async def middleware(request):
        request.user = None
        jwt_token = request.headers.get('authorization', None)
        if jwt_token:
            try:
                payload = jwt.decode(jwt_token, Config.get('application', 'salt'), algorithms=['HS256'])
            except (jwt.DecodeError, jwt.ExpiredSignatureError):
                return json_response({'message': 'Token is invalid'}, status=400)

            user = await Cache.get(payload['user_id']) or await UserDao().get_user(payload['user_id'])  # todo don't create DAO object on each
            request.user = user
        return await handler(request)
    return middleware
