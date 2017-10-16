from aiohttp.web_response import json_response


def login_required(func):
    def wrapped(request):
        if not request.user:
            return json_response({'message': 'Auth required'}, status=401)
        return func(request)
    return wrapped
