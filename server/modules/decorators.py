import os

from aiohttp.web_response import json_response


def login_required(func):
    def wrapped(request):
        if not request.request.user:
            return json_response({'message': 'Auth required'}, status=401)
        return func(request)
    return wrapped


class DummyValue:

    def __init__(self, val):
        self.val = val

    def __call__(self, func):
        def wrapped(*args, **kwargs):
            if os.environ.get('debug', False):
                return self.val
            else:
                return func(*args, **kwargs)
        return wrapped
