from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin

from proxy.services import get_proxy_response


class ProxyMiddleware(MiddlewareMixin):
    def process_request(self, request) -> HttpResponse:
        if request.method == 'GET':
            proxy_response = get_proxy_response(request)

            return HttpResponse(
                proxy_response.content,
                content_type=proxy_response.headers['content-type'],
                status=proxy_response.status_code,
            )
