import logging

logger = logging.getLogger(__name__)

class SimpleLogMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        logger.info(f"アクセスログ: {request.method} {request.path}")
        return self.get_response(request)
