from aiohttp.web_exceptions import HTTPException


async def middleware_factory(app, next_handler):

    async def middleware(request):
        try:
            response = await next_handler(request)
        except HTTPException as exc:
            response = exc
        if not response.prepared:
            response.headers['SERVER'] = "Secured Server Software"
        return response

    return middleware
