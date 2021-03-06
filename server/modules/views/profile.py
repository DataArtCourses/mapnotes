import logging

from aiohttp.web_response import json_response

from .base import BaseView

from ..models import Users
from ..decorators import login_required

log = logging.getLogger('application')


class ProfileView(BaseView):

    @login_required
    async def get(self):
        user_id = self.request.user['user_id']
        try:
            profile = await Users.get_profile(user_id=user_id)
        except Exception as e:
            log.exception("Encountered error in %s (%s)", self.__class__, e)
            return json_response({}, status=400)
        return json_response(profile, status=200)

    @login_required
    async def post(self):
        log.info("User %s trying to modify self data", self.request.user['email'])
        user_data = await self.request.json()
        if not set(user_data.keys()) == Users.fields:
            return json_response({'error': 'Please fill in all fields'}, status=400)
        user_id = self.request.user.get('user_id')
        if not user_id:
            log.error('User in request obj has no user id')
            return json_response({}, status=400)
        await Users.update_profile(user_id, **user_data)
        return json_response({}, status=200)
