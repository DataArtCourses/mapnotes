import logging

from aiohttp.web_response import json_response

from .base import BaseView

from ..models import (Pins, PinComments, PinPhotos)
from ..decorators import login_required

log = logging.getLogger('application')

class PinsView(BaseView):

    @login_required
    async def get(self):
        user_id = self.request.user['user_id']
        try:
            pins = await Pins.get_pins(user_id)
        except Exception as e:
            log.exception("Encountered error in %s (%s)", self.__class__, e)
            return json_response({}, status=400)
        for pin in pins:
            pin['lat'] = float(pin['lat'])
            pin['lng'] = float(pin['lng'])
        return json_response(pins, status=200)

    @login_required
    async def post(self):
        log.info("User %s trying add pin", self.request.user['email'])
        pin_data = await self.request.json()
        if not set(pin_data.keys()) == Pins.fields:
            return json_response({'error': 'Please fill in all fields'}, status=400)
        resp = await Pins.create_pin(**pin_data)
        return json_response(resp, status=200)